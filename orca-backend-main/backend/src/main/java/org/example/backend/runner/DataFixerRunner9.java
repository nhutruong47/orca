package org.example.backend.runner;

import org.example.backend.entity.PaymentTransaction;
import org.example.backend.entity.Role;
import org.example.backend.entity.User;
import org.example.backend.repository.PaymentTransactionRepository;
import org.example.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Random;

@Component
public class DataFixerRunner9 implements CommandLineRunner {

    @Autowired
    private PaymentTransactionRepository paymentRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Override
    @Transactional
    public void run(String... args) throws Exception {
        System.out.println("=== Running DataFixerRunner9 ===");

        // 1. Ensure admin user exists and has admin123 password
        User admin = userRepository.findByUsername("admin").orElse(new User());
        admin.setUsername("admin");
        admin.setPassword(passwordEncoder.encode("Admin@123"));
        admin.setRole(Role.ADMIN);
        admin.setFullName("Administrator");
        userRepository.save(admin);

        // 2. Fix PaymentTransactions to have different users
        List<PaymentTransaction> payments = paymentRepository.findAll();
        List<User> users = userRepository.findAll().stream()
                .filter(u -> !u.getUsername().equals("admin"))
                .toList();
        
        if (!users.isEmpty() && !payments.isEmpty()) {
            Random random = new Random();
            for (PaymentTransaction p : payments) {
                User randomUser = users.get(random.nextInt(users.size()));
                p.setUser(randomUser);
                paymentRepository.save(p);
            }
            System.out.println("=== DataFixerRunner9: Updated " + payments.size() + " payments with random users ===");
        }

        System.out.println("=== DataFixerRunner9 finished ===");
    }
}
