package org.example.backend.service;

import org.example.backend.entity.PaymentTransaction;
import org.example.backend.entity.Role;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.repository.AiConfigRepository;
import org.example.backend.repository.GoalRepository;
import org.example.backend.repository.InterGroupOrderRepository;
import org.example.backend.repository.PaymentTransactionRepository;
import org.example.backend.repository.ProductionBatchRepository;
import org.example.backend.repository.ProductionOrderRepository;
import org.example.backend.repository.SubscriptionPlanRepository;
import org.example.backend.repository.SystemLogRepository;
import org.example.backend.repository.TaskRepository;
import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.UserRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.lang.reflect.Field;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

class AdminServiceOverviewTest {

    private UserRepository userRepository;
    private TeamRepository teamRepository;
    private PaymentTransactionRepository paymentRepository;
    private AdminService service;

    @BeforeEach
    void setUp() {
        userRepository = mock(UserRepository.class);
        teamRepository = mock(TeamRepository.class);
        TeamMemberRepository teamMemberRepository = mock(TeamMemberRepository.class);
        GoalRepository goalRepository = mock(GoalRepository.class);
        TaskRepository taskRepository = mock(TaskRepository.class);
        InterGroupOrderRepository orderRepository = mock(InterGroupOrderRepository.class);
        ProductionOrderRepository productionOrderRepository = mock(ProductionOrderRepository.class);
        ProductionBatchRepository productionBatchRepository = mock(ProductionBatchRepository.class);
        paymentRepository = mock(PaymentTransactionRepository.class);

        service = new AdminService(
                userRepository,
                teamRepository,
                teamMemberRepository,
                goalRepository,
                taskRepository,
                orderRepository,
                productionOrderRepository,
                productionBatchRepository,
                paymentRepository,
                mock(TaskService.class),
                mock(PasswordEncoder.class),
                mock(SubscriptionPlanRepository.class),
                mock(AiConfigRepository.class),
                mock(SystemLogRepository.class));

        when(goalRepository.findAll()).thenReturn(List.of());
        when(taskRepository.findAll()).thenReturn(List.of());
        when(orderRepository.findAll()).thenReturn(List.of());
        when(productionOrderRepository.findAll()).thenReturn(List.of());
        when(productionBatchRepository.findAll()).thenReturn(List.of());
        when(teamRepository.findByOwnerId(any())).thenReturn(List.of());
        when(teamMemberRepository.findByTeamId(any())).thenReturn(List.of());
    }

    @Test
    void overviewUsesMonthlyIncrementsAndVerifiedPaymentsOnly() throws Exception {
        LocalDateTime currentMonth = LocalDate.now().withDayOfMonth(1).atStartOfDay();
        LocalDateTime previousMonth = currentMonth.minusMonths(1).plusDays(1);

        User currentUser = user("current-user", currentMonth);
        User previousUser = user("previous-user", previousMonth);
        Team currentTeam = team("Current team", currentMonth);
        Team previousTeam = team("Previous team", previousMonth);

        PaymentTransaction verified = payment("ORCA-VERIFIED", "NCB", 129_000, currentMonth);
        PaymentTransaction demo = payment("DEMO-001", "NCB", 249_000, currentMonth);
        PaymentTransaction virtualQr = payment("PAYOS-VIRTUAL", "PAYOS_QR", 129_000, currentMonth);

        when(userRepository.findAll()).thenReturn(List.of(currentUser, previousUser));
        when(teamRepository.findAll()).thenReturn(List.of(currentTeam, previousTeam));
        when(paymentRepository.findAll()).thenReturn(List.of(verified, demo, virtualQr));

        Map<String, Object> overview = service.getOverview();

        assertThat(overview.get("paidPayments")).isEqualTo(1L);
        assertThat(overview.get("totalPayments")).isEqualTo(1);
        assertThat(overview.get("revenueThisMonth")).isEqualTo(129_000L);
        assertThat(overview.get("revenueTotal")).isEqualTo(129_000L);

        @SuppressWarnings("unchecked")
        List<Map<String, Object>> trend = (List<Map<String, Object>>) overview.get("systemTrendData");
        Map<String, Object> previousPoint = trend.get(trend.size() - 2);
        Map<String, Object> currentPoint = trend.get(trend.size() - 1);

        assertThat(previousPoint.get("users")).isEqualTo(1L);
        assertThat(previousPoint.get("companies")).isEqualTo(1L);
        assertThat(currentPoint.get("users")).isEqualTo(1L);
        assertThat(currentPoint.get("companies")).isEqualTo(1L);
        assertThat(currentPoint.get("revenue")).isEqualTo(0.129d);
    }

    private User user(String username, LocalDateTime createdAt) throws Exception {
        User user = User.builder()
                .username(username)
                .password("encoded-password")
                .role(Role.MEMBER)
                .chipId("USR-" + UUID.randomUUID())
                .build();
        user.setId(UUID.randomUUID());
        setField(user, "createdAt", createdAt);
        return user;
    }

    private Team team(String name, LocalDateTime createdAt) throws Exception {
        Team team = new Team();
        team.setId(UUID.randomUUID());
        team.setName(name);
        setField(team, "createdAt", createdAt);
        return team;
    }

    private PaymentTransaction payment(String txnRef, String bankCode, long amount, LocalDateTime paidAt) {
        PaymentTransaction payment = new PaymentTransaction();
        payment.setTxnRef(txnRef);
        payment.setBankCode(bankCode);
        payment.setAmount(amount);
        payment.setStatus("PAID");
        payment.setPaidAt(paidAt);
        return payment;
    }

    private static void setField(Object target, String name, Object value) throws Exception {
        Field field = target.getClass().getDeclaredField(name);
        field.setAccessible(true);
        field.set(target, value);
    }
}
