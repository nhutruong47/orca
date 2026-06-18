import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../api/orca_api.dart';
import '../models.dart';

class TeamDetailScreen extends StatefulWidget {
  const TeamDetailScreen({
    required this.api,
    required this.session,
    required this.teamId,
    required this.onBack,
    super.key,
  });

  final OrcaApi api;
  final AuthSession session;
  final String teamId;
  final VoidCallback onBack;

  @override
  State<TeamDetailScreen> createState() => _TeamDetailScreenState();
}

class _TeamDetailScreenState extends State<TeamDetailScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;
  TeamDetail? team;
  List<OrcaTask> tasks = [];
  List<GoalSummary> goals = [];
  bool loading = true;
  String? error;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    loadData();
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  Future<void> loadData() async {
    setState(() {
      loading = true;
      error = null;
    });
    try {
      final teamData = await widget.api.getTeamDetail(widget.teamId);
      final tasksData = await widget.api.getMyTasks();
      if (!mounted) return;
      setState(() {
        team = teamData;
        tasks = tasksData;
        loading = false;
      });
    } catch (e) {
      if (!mounted) return;
      setState(() {
        error = e.toString();
        loading = false;
      });
    }
  }

  Future<void> copyInviteCode() async {
    if (team?.inviteCode == null) return;
    await Clipboard.setData(ClipboardData(text: team!.inviteCode!));
    if (!mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Đã copy mã mời!')),
    );
  }

  bool get isOwner => team?.ownerId == widget.session.id;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: widget.onBack,
        ),
        title: Text(team?.name ?? 'Chi tiết nhóm'),
        actions: [
          if (isOwner && team?.inviteCode != null)
            IconButton(
              icon: const Icon(Icons.share),
              tooltip: 'Copy mã mời',
              onPressed: copyInviteCode,
            ),
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: loadData,
          ),
        ],
        bottom: TabBar(
          controller: _tabController,
          tabs: const [
            Tab(text: 'Tổng quan'),
            Tab(text: 'Thành viên'),
            Tab(text: 'Tasks'),
            Tab(text: 'Goals'),
          ],
        ),
      ),
      body: loading
          ? const Center(child: CircularProgressIndicator())
          : error != null
              ? Center(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(error!, style: const TextStyle(color: Colors.red)),
                      const SizedBox(height: 16),
                      ElevatedButton(
                        onPressed: loadData,
                        child: const Text('Thử lại'),
                      ),
                    ],
                  ),
                )
              : team == null
                  ? const Center(child: Text('Không tìm thấy nhóm'))
                  : TabBarView(
                      controller: _tabController,
                      children: [
                        _buildOverviewTab(),
                        _buildMembersTab(),
                        _buildTasksTab(),
                        _buildGoalsTab(),
                      ],
                    ),
    );
  }

  Widget _buildOverviewTab() {
    return RefreshIndicator(
      onRefresh: loadData,
      child: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // Header Card
          Card(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                children: [
                  CircleAvatar(
                    radius: 40,
                    backgroundColor: const Color(0xFF3B2414),
                    child: Text(
                      team!.name.isNotEmpty ? team!.name[0].toUpperCase() : '?',
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 32,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  const SizedBox(height: 16),
                  Text(
                    team!.name,
                    style: const TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  if (team!.description != null) ...[
                    const SizedBox(height: 8),
                    Text(
                      team!.description!,
                      style: const TextStyle(color: Colors.grey),
                      textAlign: TextAlign.center,
                    ),
                  ],
                  const SizedBox(height: 16),
                  if (team!.inviteCode != null && isOwner)
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 16,
                        vertical: 8,
                      ),
                      decoration: BoxDecoration(
                        color: const Color(0xFFFFF4E8),
                        borderRadius: BorderRadius.circular(8),
                        border: Border.all(color: const Color(0xFFD99C5F)),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(Icons.qr_code, color: Color(0xFF6E461F)),
                          const SizedBox(width: 8),
                          Text(
                            'Mã mời: ${team!.inviteCode}',
                            style: const TextStyle(
                              fontWeight: FontWeight.bold,
                              color: Color(0xFF3B2414),
                              letterSpacing: 2,
                            ),
                          ),
                        ],
                      ),
                    ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),

          // Stats
          Row(
            children: [
              Expanded(
                child: _StatCard(
                  icon: Icons.people,
                  label: 'Thành viên',
                  value: team!.memberCount.toString(),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: _StatCard(
                  icon: Icons.verified,
                  label: 'Uy tín',
                  value: '${team!.trustScore}%',
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Row(
            children: [
              Expanded(
                child: _StatCard(
                  icon: Icons.check_circle,
                  label: 'Đơn hoàn thành',
                  value: team!.completedOrders.toString(),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: _StatCard(
                  icon: Icons.inventory,
                  label: 'Tổng đơn',
                  value: team!.totalOrders.toString(),
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),

          // Info
          if (team!.region != null || team!.specialty != null)
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text(
                      'Thông tin xưởng',
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 12),
                    if (team!.region != null)
                      _InfoRow(
                        icon: Icons.location_on,
                        label: 'Khu vực',
                        value: team!.region!,
                      ),
                    if (team!.specialty != null)
                      _InfoRow(
                        icon: Icons.star,
                        label: 'Chuyên môn',
                        value: team!.specialty!,
                      ),
                    if (team!.capacity != null)
                      _InfoRow(
                        icon: Icons.factory,
                        label: 'Công suất',
                        value: team!.capacity!,
                      ),
                    if (team!.ownerName != null)
                      _InfoRow(
                        icon: Icons.person,
                        label: 'Chủ nhóm',
                        value: team!.ownerName!,
                      ),
                  ],
                ),
              ),
            ),
        ],
      ),
    );
  }

  Widget _buildMembersTab() {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: team!.members.length,
      itemBuilder: (ctx, index) {
        final member = team!.members[index];
        return Card(
          margin: const EdgeInsets.only(bottom: 12),
          child: ListTile(
            leading: CircleAvatar(
              backgroundColor: member.isOwner
                  ? const Color(0xFFD99C5F)
                  : const Color(0xFFF1E8DE),
              child: Text(
                member.fullName.isNotEmpty
                    ? member.fullName[0].toUpperCase()
                    : '?',
                style: TextStyle(
                  color: member.isOwner ? Colors.white : const Color(0xFF3B2414),
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            title: Row(
              children: [
                Text(
                  member.fullName.isNotEmpty ? member.fullName : member.username,
                  style: const TextStyle(fontWeight: FontWeight.bold),
                ),
                if (member.isOwner) ...[
                  const SizedBox(width: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                    decoration: BoxDecoration(
                      color: const Color(0xFFD99C5F),
                      borderRadius: BorderRadius.circular(4),
                    ),
                    child: const Text(
                      'ADMIN',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 10,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ],
            ),
            subtitle: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SizedBox(height: 4),
                Text('@${member.username}'),
                const SizedBox(height: 8),
                Row(
                  children: [
                    _MiniChip(
                      icon: Icons.task,
                      label: '${member.totalTasks} task',
                    ),
                    const SizedBox(width: 8),
                    _MiniChip(
                      icon: Icons.done,
                      label: '${member.completedTasks} hoàn thành',
                    ),
                  ],
                ),
                if (member.jobLabels.isNotEmpty) ...[
                  const SizedBox(height: 8),
                  Wrap(
                    spacing: 4,
                    runSpacing: 4,
                    children: member.jobLabels
                        .map((label) => Chip(
                              label: Text(label, style: const TextStyle(fontSize: 11)),
                              padding: EdgeInsets.zero,
                              materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
                            ))
                        .toList(),
                  ),
                ],
              ],
            ),
          ),
        );
      },
    );
  }

  Widget _buildTasksTab() {
    if (tasks.isEmpty) {
      return Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Icon(Icons.task_alt, size: 64, color: Colors.grey),
            const SizedBox(height: 16),
            const Text('Chưa có công việc nào'),
            const SizedBox(height: 8),
            const Text(
              'Tạo task mới trong nhóm để quản lý',
              style: TextStyle(color: Colors.grey),
            ),
          ],
        ),
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: tasks.length,
      itemBuilder: (ctx, index) {
        final task = tasks[index];
        return Card(
          margin: const EdgeInsets.only(bottom: 12),
          child: ListTile(
            leading: Icon(
              task.status == 'COMPLETED'
                  ? Icons.check_circle
                  : task.status == 'IN_PROGRESS'
                      ? Icons.pending
                      : Icons.radio_button_unchecked,
              color: task.status == 'COMPLETED'
                  ? Colors.green
                  : task.status == 'IN_PROGRESS'
                      ? Colors.orange
                      : Colors.grey,
            ),
            title: Text(
              task.title,
              style: TextStyle(
                fontWeight: FontWeight.bold,
                decoration: task.status == 'COMPLETED'
                    ? TextDecoration.lineThrough
                    : null,
              ),
            ),
            subtitle: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (task.description != null) ...[
                  const SizedBox(height: 4),
                  Text(
                    task.description!,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                ],
                const SizedBox(height: 8),
                Row(
                  children: [
                    if (task.memberName != null)
                      _MiniChip(
                        icon: Icons.person,
                        label: task.memberName!,
                      ),
                    const SizedBox(width: 8),
                    _StatusBadge(status: task.status),
                  ],
                ),
                if (task.deadline != null) ...[
                  const SizedBox(height: 8),
                  Text(
                    'Hạn: ${_formatDate(task.deadline!)}',
                    style: const TextStyle(
                      fontSize: 12,
                      color: Colors.grey,
                    ),
                  ),
                ],
              ],
            ),
          ),
        );
      },
    );
  }

  Widget _buildGoalsTab() {
    if (goals.isEmpty) {
      return Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Icon(Icons.flag, size: 64, color: Colors.grey),
            const SizedBox(height: 16),
            const Text('Chưa có mục tiêu nào'),
            const SizedBox(height: 8),
            const Text(
              'Goals sẽ được tạo khi chấp nhận đơn hàng',
              style: TextStyle(color: Colors.grey),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: goals.length,
      itemBuilder: (ctx, index) {
        final goal = goals[index];
        return Card(
          margin: const EdgeInsets.only(bottom: 12),
          child: Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Expanded(
                      child: Text(
                        goal.title,
                        style: const TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    _StatusBadge(status: goal.status),
                  ],
                ),
                if (goal.description != null) ...[
                  const SizedBox(height: 8),
                  Text(
                    goal.description!,
                    style: const TextStyle(color: Colors.grey),
                  ),
                ],
                const SizedBox(height: 12),
                Row(
                  children: [
                    Expanded(
                      child: LinearProgressIndicator(
                        value: goal.progress / 100,
                        backgroundColor: Colors.grey[200],
                        valueColor: AlwaysStoppedAnimation(
                          goal.progress == 100
                              ? Colors.green
                              : goal.progress >= 50
                                  ? Colors.orange
                                  : Colors.blue,
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    Text(
                      '${goal.progress}%',
                      style: const TextStyle(fontWeight: FontWeight.bold),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Text(
                  '${goal.completedTasks}/${goal.totalTasks} công việc hoàn thành',
                  style: const TextStyle(fontSize: 12, color: Colors.grey),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  String _formatDate(DateTime date) {
    return '${date.day.toString().padLeft(2, '0')}/${date.month.toString().padLeft(2, '0')}/${date.year}';
  }
}

class _StatCard extends StatelessWidget {
  const _StatCard({
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
          children: [
            Icon(icon, color: const Color(0xFF6E461F), size: 28),
            const SizedBox(height: 8),
            Text(
              value,
              style: const TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
            Text(
              label,
              style: const TextStyle(
                fontSize: 12,
                color: Colors.grey,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _InfoRow extends StatelessWidget {
  const _InfoRow({
    required this.icon,
    required this.label,
    required this.value,
  });

  final IconData icon;
  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        children: [
          Icon(icon, size: 18, color: Colors.grey),
          const SizedBox(width: 8),
          Text('$label: ', style: const TextStyle(color: Colors.grey)),
          Text(value, style: const TextStyle(fontWeight: FontWeight.w500)),
        ],
      ),
    );
  }
}

class _MiniChip extends StatelessWidget {
  const _MiniChip({required this.icon, required this.label});

  final IconData icon;
  final String label;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: const Color(0xFFF1E8DE),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 12, color: const Color(0xFF6E461F)),
          const SizedBox(width: 4),
          Text(
            label,
            style: const TextStyle(fontSize: 11, color: Color(0xFF6E461F)),
          ),
        ],
      ),
    );
  }
}

class _StatusBadge extends StatelessWidget {
  const _StatusBadge({required this.status});

  final String status;

  @override
  Widget build(BuildContext context) {
    final data = switch (status) {
      'COMPLETED' || 'ACCEPTED' => (
          'Hoàn thành',
          const Color(0xFFE7F7ED),
          const Color(0xFF16703D),
        ),
      'IN_PROGRESS' => (
          'Đang làm',
          const Color(0xFFFFF4E8),
          const Color(0xFF9A5B12),
        ),
      'PENDING' => (
          'Chờ xử lý',
          const Color(0xFFFFF4E8),
          const Color(0xFF9A5B12),
        ),
      'REJECTED' || 'CANCELED' => (
          'Từ chối',
          const Color(0xFFFFE8E6),
          const Color(0xFFB42318),
        ),
      _ => (
          status,
          const Color(0xFFF0F0F0),
          const Color(0xFF555555),
        ),
    };

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: data.$2,
        borderRadius: BorderRadius.circular(8),
      ),
      child: Text(
        data.$1,
        style: TextStyle(
          color: data.$3,
          fontSize: 11,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }
}
