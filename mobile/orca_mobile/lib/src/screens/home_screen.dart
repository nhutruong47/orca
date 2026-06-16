import 'package:flutter/material.dart';

import '../api/orca_api.dart';
import '../models.dart';

enum OrderMode { inbound, outbound }

class HomeScreen extends StatefulWidget {
  const HomeScreen({
    required this.api,
    required this.session,
    required this.onLogout,
    super.key,
  });

  final OrcaApi api;
  final AuthSession session;
  final VoidCallback onLogout;

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int tabIndex = 0;
  bool loading = true;
  String? error;
  List<TeamSummary> teams = const [];
  TeamSummary? selectedTeam;
  List<InterOrder> orders = const [];
  List<OrcaNotification> notifications = const [];
  int unreadCount = 0;
  OrderMode orderMode = OrderMode.inbound;

  @override
  void initState() {
    super.initState();
    refreshAll();
  }

  Future<void> refreshAll() async {
    setState(() {
      loading = true;
      error = null;
    });
    try {
      final nextTeams = await widget.api.getMyTeams();
      final currentSelection = selectedTeam;
      final matchingSelection = currentSelection == null
          ? null
          : _findTeam(nextTeams, currentSelection.id);
      final nextSelected =
          matchingSelection ?? (nextTeams.isNotEmpty ? nextTeams.first : null);

      final nextUnread = await widget.api.getUnreadCount();
      final nextNotifications = await widget.api.getNotifications();

      setState(() {
        teams = nextTeams;
        selectedTeam = nextSelected;
        unreadCount = nextUnread;
        notifications = nextNotifications;
      });
      await refreshOrders();
    } catch (exception) {
      setState(() => error = exception.toString());
    } finally {
      if (mounted) setState(() => loading = false);
    }
  }

  Future<void> refreshOrders() async {
    final team = selectedTeam;
    if (team == null) {
      setState(() => orders = const []);
      return;
    }
    final nextOrders = orderMode == OrderMode.inbound
        ? await widget.api.getInboundOrders(team.id)
        : await widget.api.getOutboundOrders(team.id);
    if (!mounted) return;
    setState(() => orders = nextOrders);
  }

  Future<void> runOrderAction(
    InterOrder order,
    Future<void> Function(String id) action,
    String successMessage,
  ) async {
    try {
      await action(order.id);
      await refreshOrders();
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(successMessage)),
      );
    } catch (exception) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(exception.toString())),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final pages = [
      _OverviewTab(
        session: widget.session,
        teams: teams,
        selectedTeam: selectedTeam,
        unreadCount: unreadCount,
        onTeamChanged: (team) async {
          setState(() => selectedTeam = team);
          await refreshOrders();
        },
      ),
      _OrdersTab(
        loading: loading,
        selectedTeam: selectedTeam,
        orders: orders,
        mode: orderMode,
        onModeChanged: (mode) async {
          setState(() => orderMode = mode);
          await refreshOrders();
        },
        onRefresh: refreshOrders,
        onAccept: (order) => runOrderAction(
          order,
          widget.api.acceptOrder,
          'Đã chấp nhận đơn đặt hàng.',
        ),
        onReject: (order) => runOrderAction(
          order,
          widget.api.rejectOrder,
          'Đã từ chối đơn đặt hàng.',
        ),
        onCancel: (order) => runOrderAction(
          order,
          widget.api.cancelOrder,
          'Đã hủy đơn đặt hàng.',
        ),
        onComplete: (order) => runOrderAction(
          order,
          widget.api.completeOrder,
          'Đã đánh dấu hoàn thành.',
        ),
      ),
      _NotificationsTab(
        notifications: notifications,
        unreadCount: unreadCount,
        onRefresh: refreshAll,
        onMarkAllRead: () async {
          await widget.api.markAllNotificationsRead();
          await refreshAll();
        },
      ),
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'ORCA Mobile',
          style: TextStyle(fontWeight: FontWeight.w800),
        ),
        actions: [
          IconButton(
            tooltip: 'Tải lại',
            onPressed: refreshAll,
            icon: const Icon(Icons.refresh),
          ),
          IconButton(
            tooltip: 'Đăng xuất',
            onPressed: widget.onLogout,
            icon: const Icon(Icons.logout),
          ),
        ],
      ),
      body: SafeArea(
        child: error != null
            ? _ErrorState(message: error!, onRetry: refreshAll)
            : RefreshIndicator(
                onRefresh: refreshAll,
                child: ListView(
                  padding: const EdgeInsets.fromLTRB(16, 8, 16, 24),
                  children: [
                    if (loading) const LinearProgressIndicator(),
                    pages[tabIndex],
                  ],
                ),
              ),
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: tabIndex,
        onDestinationSelected: (index) => setState(() => tabIndex = index),
        destinations: [
          const NavigationDestination(
            icon: Icon(Icons.dashboard_outlined),
            selectedIcon: Icon(Icons.dashboard),
            label: 'Tổng quan',
          ),
          const NavigationDestination(
            icon: Icon(Icons.inventory_2_outlined),
            selectedIcon: Icon(Icons.inventory_2),
            label: 'Đơn hàng',
          ),
          NavigationDestination(
            icon: Badge.count(
              count: unreadCount,
              isLabelVisible: unreadCount > 0,
              child: const Icon(Icons.notifications_outlined),
            ),
            selectedIcon: Badge.count(
              count: unreadCount,
              isLabelVisible: unreadCount > 0,
              child: const Icon(Icons.notifications),
            ),
            label: 'Thông báo',
          ),
        ],
      ),
    );
  }
}

class _OverviewTab extends StatelessWidget {
  const _OverviewTab({
    required this.session,
    required this.teams,
    required this.selectedTeam,
    required this.unreadCount,
    required this.onTeamChanged,
  });

  final AuthSession session;
  final List<TeamSummary> teams;
  final TeamSummary? selectedTeam;
  final int unreadCount;
  final ValueChanged<TeamSummary> onTeamChanged;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        _GreetingCard(session: session),
        const SizedBox(height: 16),
        Row(
          children: [
            Expanded(
              child: _MetricCard(
                icon: Icons.factory_outlined,
                label: 'Xưởng của tôi',
                value: teams.length.toString(),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: _MetricCard(
                icon: Icons.notifications_active_outlined,
                label: 'Chưa đọc',
                value: unreadCount.toString(),
              ),
            ),
          ],
        ),
        const SizedBox(height: 20),
        const Text(
          'Chọn xưởng',
          style: TextStyle(fontSize: 18, fontWeight: FontWeight.w800),
        ),
        const SizedBox(height: 10),
        if (teams.isEmpty)
          const _EmptyCard(
            icon: Icons.groups_outlined,
            title: 'Chưa có xưởng',
            message:
                'Tạo hoặc tham gia nhóm xưởng trên web để quản lý ở mobile.',
          )
        else
          ...teams.map(
            (team) => Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: _TeamCard(
                team: team,
                selected: team.id == selectedTeam?.id,
                onTap: () => onTeamChanged(team),
              ),
            ),
          ),
      ],
    );
  }
}

class _OrdersTab extends StatelessWidget {
  const _OrdersTab({
    required this.loading,
    required this.selectedTeam,
    required this.orders,
    required this.mode,
    required this.onModeChanged,
    required this.onRefresh,
    required this.onAccept,
    required this.onReject,
    required this.onCancel,
    required this.onComplete,
  });

  final bool loading;
  final TeamSummary? selectedTeam;
  final List<InterOrder> orders;
  final OrderMode mode;
  final ValueChanged<OrderMode> onModeChanged;
  final Future<void> Function() onRefresh;
  final ValueChanged<InterOrder> onAccept;
  final ValueChanged<InterOrder> onReject;
  final ValueChanged<InterOrder> onCancel;
  final ValueChanged<InterOrder> onComplete;

  @override
  Widget build(BuildContext context) {
    final pendingCount = mode == OrderMode.inbound
        ? orders.where((order) => order.status == 'PENDING').length
        : 0;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text(
          'Đơn hàng',
          style: TextStyle(fontSize: 24, fontWeight: FontWeight.w900),
        ),
        const SizedBox(height: 12),
        SegmentedButton<OrderMode>(
          segments: const [
            ButtonSegment(
              value: OrderMode.inbound,
              icon: Icon(Icons.call_received),
              label: Text('Đơn nhận'),
            ),
            ButtonSegment(
              value: OrderMode.outbound,
              icon: Icon(Icons.call_made),
              label: Text('Đơn gửi'),
            ),
          ],
          selected: {mode},
          onSelectionChanged: (value) => onModeChanged(value.first),
        ),
        const SizedBox(height: 14),
        if (selectedTeam != null)
          Text(
            'Xưởng: ${selectedTeam!.name}',
            style: const TextStyle(color: Color(0xFF7A6B60)),
          ),
        const SizedBox(height: 14),
        if (pendingCount > 0) _OrderNotice(count: pendingCount),
        if (loading)
          const Padding(
            padding: EdgeInsets.all(24),
            child: Center(child: CircularProgressIndicator()),
          )
        else if (selectedTeam == null)
          const _EmptyCard(
            icon: Icons.factory_outlined,
            title: 'Chưa chọn được xưởng',
            message: 'Bạn cần có ít nhất một xưởng để xem đơn hàng.',
          )
        else if (orders.isEmpty)
          _EmptyCard(
            icon: Icons.inventory_2_outlined,
            title: 'Chưa có đơn hàng',
            message: mode == OrderMode.inbound
                ? 'Khi xưởng khác đặt gia công, đơn sẽ hiện ở đây.'
                : 'Các đơn bạn gửi cho xưởng khác sẽ hiện ở đây.',
          )
        else
          ...orders.map(
            (order) => Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: _OrderCard(
                order: order,
                mode: mode,
                onAccept: () => onAccept(order),
                onReject: () => onReject(order),
                onCancel: () => onCancel(order),
                onComplete: () => onComplete(order),
              ),
            ),
          ),
      ],
    );
  }
}

class _NotificationsTab extends StatelessWidget {
  const _NotificationsTab({
    required this.notifications,
    required this.unreadCount,
    required this.onRefresh,
    required this.onMarkAllRead,
  });

  final List<OrcaNotification> notifications;
  final int unreadCount;
  final Future<void> Function() onRefresh;
  final Future<void> Function() onMarkAllRead;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            const Expanded(
              child: Text(
                'Thông báo',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.w900),
              ),
            ),
            TextButton.icon(
              onPressed: unreadCount == 0 ? null : onMarkAllRead,
              icon: const Icon(Icons.done_all),
              label: const Text('Đã đọc'),
            ),
          ],
        ),
        const SizedBox(height: 10),
        if (notifications.isEmpty)
          const _EmptyCard(
            icon: Icons.notifications_none,
            title: 'Chưa có thông báo',
            message: 'Thông báo mới từ công việc và đơn hàng sẽ hiện ở đây.',
          )
        else
          ...notifications.map(
            (item) => Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Card(
                child: ListTile(
                  leading: CircleAvatar(
                    backgroundColor: item.isRead
                        ? const Color(0xFFF1E8DE)
                        : const Color(0xFFD99C5F),
                    child: Icon(
                      item.isRead
                          ? Icons.notifications_none
                          : Icons.notifications_active,
                      color: const Color(0xFF3B2414),
                    ),
                  ),
                  title: Text(
                    item.title,
                    style: const TextStyle(fontWeight: FontWeight.w800),
                  ),
                  subtitle: Text(item.message),
                  trailing: item.createdAt == null
                      ? null
                      : Text(
                          _formatDate(item.createdAt!),
                          style: const TextStyle(fontSize: 12),
                        ),
                ),
              ),
            ),
          ),
      ],
    );
  }
}

class _GreetingCard extends StatelessWidget {
  const _GreetingCard({required this.session});

  final AuthSession session;

  @override
  Widget build(BuildContext context) {
    final name = session.fullName?.isNotEmpty == true
        ? session.fullName!
        : session.username;

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(18),
        child: Row(
          children: [
            CircleAvatar(
              radius: 28,
              backgroundColor: const Color(0xFF3B2414),
              child: Text(
                (name.isEmpty ? 'O' : name[0]).toUpperCase(),
                style: const TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.w800,
                ),
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Xin chào, $name',
                    style: const TextStyle(
                      fontSize: 19,
                      fontWeight: FontWeight.w900,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    session.email ?? session.role ?? 'Thành viên ORCA',
                    style: const TextStyle(color: Color(0xFF7A6B60)),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _MetricCard extends StatelessWidget {
  const _MetricCard({
    required this.icon,
    required this.label,
    required this.value,
  });

  final IconData icon;
  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Icon(icon, color: const Color(0xFF6E461F)),
            const SizedBox(height: 14),
            Text(
              value,
              style: const TextStyle(fontSize: 26, fontWeight: FontWeight.w900),
            ),
            Text(label, style: const TextStyle(color: Color(0xFF7A6B60))),
          ],
        ),
      ),
    );
  }
}

class _TeamCard extends StatelessWidget {
  const _TeamCard({
    required this.team,
    required this.selected,
    required this.onTap,
  });

  final TeamSummary team;
  final bool selected;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Card(
      color: selected ? const Color(0xFFFFF4E8) : Colors.white,
      child: ListTile(
        onTap: onTap,
        leading: CircleAvatar(
          backgroundColor:
              selected ? const Color(0xFFD99C5F) : const Color(0xFFF1E8DE),
          child: const Icon(Icons.factory_outlined, color: Color(0xFF3B2414)),
        ),
        title: Text(
          team.name,
          style: const TextStyle(fontWeight: FontWeight.w800),
        ),
        subtitle: Text(
          '${team.memberCount} thành viên · Uy tín ${team.trustScore}%',
        ),
        trailing: selected ? const Icon(Icons.check_circle) : null,
      ),
    );
  }
}

class _OrderNotice extends StatelessWidget {
  const _OrderNotice({required this.count});

  final int count;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 14),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: const Color(0xFFFFF4E8),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: const Color(0xFFD99C5F)),
      ),
      child: Row(
        children: [
          const Icon(Icons.notifications_active, color: Color(0xFF6E461F)),
          const SizedBox(width: 12),
          Expanded(
            child: Text(
              'Bạn có $count đơn đặt hàng mới cần phản hồi.',
              style: const TextStyle(
                color: Color(0xFF3B2414),
                fontWeight: FontWeight.w800,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _OrderCard extends StatelessWidget {
  const _OrderCard({
    required this.order,
    required this.mode,
    required this.onAccept,
    required this.onReject,
    required this.onCancel,
    required this.onComplete,
  });

  final InterOrder order;
  final OrderMode mode;
  final VoidCallback onAccept;
  final VoidCallback onReject;
  final VoidCallback onCancel;
  final VoidCallback onComplete;

  @override
  Widget build(BuildContext context) {
    final partner = mode == OrderMode.inbound
        ? order.buyerTeamName ?? 'Bên đặt'
        : order.sellerTeamName ?? 'Xưởng nhận';

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: Text(
                    order.title,
                    style: const TextStyle(
                      fontSize: 17,
                      fontWeight: FontWeight.w900,
                    ),
                  ),
                ),
                _StatusChip(status: order.status),
              ],
            ),
            const SizedBox(height: 8),
            Text(partner, style: const TextStyle(color: Color(0xFF7A6B60))),
            if (order.description?.isNotEmpty == true) ...[
              const SizedBox(height: 8),
              Text(order.description!),
            ],
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 8,
              children: [
                _SmallInfo(
                    icon: Icons.scale, text: 'Số lượng ${order.quantity}'),
                if (order.deadline != null)
                  _SmallInfo(
                    icon: Icons.event,
                    text: 'Hạn ${_formatDate(order.deadline!)}',
                  ),
                if (mode == OrderMode.inbound)
                  _SmallInfo(
                    icon: Icons.verified_user_outlined,
                    text: 'Uy tín ${order.buyerTrustScore}%',
                  ),
              ],
            ),
            const SizedBox(height: 14),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                if (mode == OrderMode.inbound && order.status == 'PENDING') ...[
                  OutlinedButton.icon(
                    onPressed: onReject,
                    icon: const Icon(Icons.close),
                    label: const Text('Từ chối'),
                  ),
                  FilledButton.icon(
                    onPressed: onAccept,
                    icon: const Icon(Icons.check),
                    label: const Text('Chấp nhận'),
                  ),
                ],
                if (mode == OrderMode.inbound && order.status == 'ACCEPTED')
                  FilledButton.icon(
                    onPressed: onComplete,
                    icon: const Icon(Icons.done_all),
                    label: const Text('Hoàn thành'),
                  ),
                if (order.status == 'PENDING' || order.status == 'ACCEPTED')
                  TextButton.icon(
                    onPressed: onCancel,
                    icon: const Icon(Icons.block),
                    label: const Text('Hủy'),
                  ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class _StatusChip extends StatelessWidget {
  const _StatusChip({required this.status});

  final String status;

  @override
  Widget build(BuildContext context) {
    final data = switch (status) {
      'ACCEPTED' => (
          'Đã nhận',
          const Color(0xFFE7F7ED),
          const Color(0xFF16703D)
        ),
      'REJECTED' => (
          'Từ chối',
          const Color(0xFFFFE8E6),
          const Color(0xFFB42318)
        ),
      'COMPLETED' => (
          'Hoàn thành',
          const Color(0xFFEAF2FF),
          const Color(0xFF175CD3)
        ),
      'CANCELED' => (
          'Đã hủy',
          const Color(0xFFF0F0F0),
          const Color(0xFF555555)
        ),
      _ => ('Chờ xử lý', const Color(0xFFFFF4E8), const Color(0xFF9A5B12)),
    };

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
      decoration: BoxDecoration(
        color: data.$2,
        borderRadius: BorderRadius.circular(999),
      ),
      child: Text(
        data.$1,
        style: TextStyle(
          color: data.$3,
          fontWeight: FontWeight.w800,
          fontSize: 12,
        ),
      ),
    );
  }
}

class _SmallInfo extends StatelessWidget {
  const _SmallInfo({required this.icon, required this.text});

  final IconData icon;
  final String text;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 7),
      decoration: BoxDecoration(
        color: const Color(0xFFF7F1EA),
        borderRadius: BorderRadius.circular(999),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 15, color: const Color(0xFF6E461F)),
          const SizedBox(width: 5),
          Text(text, style: const TextStyle(fontSize: 12)),
        ],
      ),
    );
  }
}

class _EmptyCard extends StatelessWidget {
  const _EmptyCard({
    required this.icon,
    required this.title,
    required this.message,
  });

  final IconData icon;
  final String title;
  final String message;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(22),
        child: Column(
          children: [
            Icon(icon, size: 42, color: const Color(0xFFB08A68)),
            const SizedBox(height: 12),
            Text(
              title,
              style: const TextStyle(fontWeight: FontWeight.w900),
            ),
            const SizedBox(height: 6),
            Text(
              message,
              textAlign: TextAlign.center,
              style: const TextStyle(color: Color(0xFF7A6B60)),
            ),
          ],
        ),
      ),
    );
  }
}

class _ErrorState extends StatelessWidget {
  const _ErrorState({required this.message, required this.onRetry});

  final String message;
  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Icon(Icons.error_outline, size: 54, color: Color(0xFFB42318)),
            const SizedBox(height: 12),
            Text(
              message,
              textAlign: TextAlign.center,
              style: const TextStyle(color: Color(0xFFB42318)),
            ),
            const SizedBox(height: 16),
            FilledButton.icon(
              onPressed: onRetry,
              icon: const Icon(Icons.refresh),
              label: const Text('Thử lại'),
            ),
          ],
        ),
      ),
    );
  }
}

String _formatDate(DateTime date) {
  final day = date.day.toString().padLeft(2, '0');
  final month = date.month.toString().padLeft(2, '0');
  return '$day/$month/${date.year}';
}

TeamSummary? _findTeam(List<TeamSummary> teams, String id) {
  for (final team in teams) {
    if (team.id == id) return team;
  }
  return null;
}
