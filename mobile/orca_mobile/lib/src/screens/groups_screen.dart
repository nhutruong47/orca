import 'package:flutter/material.dart';

import '../api/orca_api.dart';
import '../models.dart';

class GroupsScreen extends StatefulWidget {
  const GroupsScreen({
    required this.api,
    required this.session,
    required this.onBack,
    required this.onTeamSelected,
    super.key,
  });

  final OrcaApi api;
  final AuthSession session;
  final VoidCallback onBack;
  final ValueChanged<TeamSummary> onTeamSelected;

  @override
  State<GroupsScreen> createState() => _GroupsScreenState();
}

class _GroupsScreenState extends State<GroupsScreen> {
  List<TeamSummary> teams = [];
  bool loading = true;
  String? error;
  bool showCreateDialog = false;
  bool showJoinDialog = false;
  final nameController = TextEditingController();
  final descController = TextEditingController();
  final joinCodeController = TextEditingController();
  bool saving = false;

  @override
  void initState() {
    super.initState();
    loadTeams();
  }

  @override
  void dispose() {
    nameController.dispose();
    descController.dispose();
    joinCodeController.dispose();
    super.dispose();
  }

  Future<void> loadTeams() async {
    setState(() {
      loading = true;
      error = null;
    });
    try {
      final data = await widget.api.getMyTeams();
      if (!mounted) return;
      setState(() {
        teams = data;
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

  Future<void> createTeam() async {
    final name = nameController.text.trim();
    if (name.isEmpty) return;

    setState(() => saving = true);
    try {
      final team = await widget.api.createTeam(
        name: name,
        description: descController.text.trim(),
      );
      if (!mounted) return;
      setState(() {
        teams = [team, ...teams];
        saving = false;
        showCreateDialog = false;
        nameController.clear();
        descController.clear();
      });
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Đã tạo nhóm mới!')),
      );
    } catch (e) {
      if (!mounted) return;
      setState(() => saving = false);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Lỗi: $e')),
      );
    }
  }

  Future<void> joinTeam() async {
    final code = joinCodeController.text.trim().toUpperCase();
    if (code.isEmpty) return;

    setState(() => saving = true);
    try {
      final team = await widget.api.joinTeamByCode(code);
      if (!mounted) return;
      setState(() {
        teams = [team, ...teams.where((t) => t.id != team.id)];
        saving = false;
        showJoinDialog = false;
        joinCodeController.clear();
      });
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Đã tham gia "${team.name}"!')),
      );
    } catch (e) {
      if (!mounted) return;
      setState(() => saving = false);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Lỗi: $e')),
      );
    }
  }

  Future<void> deleteTeam(TeamSummary team) async {
    final confirm = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Xóa nhóm?'),
        content: Text('Bạn có chắc muốn xóa nhóm "${team.name}"?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx, false),
            child: const Text('Hủy'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(ctx, true),
            child: const Text('Xóa', style: TextStyle(color: Colors.red)),
          ),
        ],
      ),
    );

    if (confirm != true) return;

    try {
      await widget.api.deleteTeam(team.id);
      if (!mounted) return;
      setState(() => teams = teams.where((t) => t.id != team.id).toList());
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Đã xóa nhóm!')),
      );
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Lỗi: $e')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: widget.onBack,
        ),
        title: const Text('Nhóm xưởng'),
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: loadTeams,
          ),
        ],
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
                        onPressed: loadTeams,
                        child: const Text('Thử lại'),
                      ),
                    ],
                  ),
                )
              : teams.isEmpty
                  ? Center(
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(Icons.groups_outlined, size: 64, color: Colors.grey),
                          const SizedBox(height: 16),
                          const Text(
                            'Chưa có nhóm xưởng',
                            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                          ),
                          const SizedBox(height: 8),
                          const Text('Tạo nhóm mới hoặc nhập mã để tham gia'),
                        ],
                      ),
                    )
                  : RefreshIndicator(
                      onRefresh: loadTeams,
                      child: ListView.builder(
                        padding: const EdgeInsets.all(16),
                        itemCount: teams.length,
                        itemBuilder: (ctx, index) {
                          final team = teams[index];
                          return Card(
                            margin: const EdgeInsets.only(bottom: 12),
                            child: ListTile(
                              contentPadding: const EdgeInsets.all(16),
                              leading: CircleAvatar(
                                backgroundColor: const Color(0xFF3B2414),
                                child: Text(
                                  team.name.isNotEmpty ? team.name[0].toUpperCase() : '?',
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ),
                              title: Text(
                                team.name,
                                style: const TextStyle(fontWeight: FontWeight.bold),
                              ),
                              subtitle: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  const SizedBox(height: 4),
                                  Text(
                                    team.description ?? 'Chưa có mô tả',
                                    maxLines: 2,
                                    overflow: TextOverflow.ellipsis,
                                  ),
                                  const SizedBox(height: 8),
                                  Row(
                                    children: [
                                      _Chip(
                                        icon: Icons.people,
                                        label: '${team.memberCount} thành viên',
                                      ),
                                      const SizedBox(width: 8),
                                      _Chip(
                                        icon: Icons.verified,
                                        label: 'Uy tín ${team.trustScore}%',
                                      ),
                                    ],
                                  ),
                                ],
                              ),
                              trailing: PopupMenuButton(
                                itemBuilder: (ctx) => [
                                  const PopupMenuItem(
                                    value: 'open',
                                    child: Row(
                                      children: [
                                        Icon(Icons.open_in_new),
                                        SizedBox(width: 8),
                                        Text('Mở nhóm'),
                                      ],
                                    ),
                                  ),
                                  if (team.ownerId == widget.session.id)
                                    const PopupMenuItem(
                                      value: 'delete',
                                      child: Row(
                                        children: [
                                          Icon(Icons.delete, color: Colors.red),
                                          SizedBox(width: 8),
                                          Text('Xóa nhóm', style: TextStyle(color: Colors.red)),
                                        ],
                                      ),
                                    ),
                                ],
                                onSelected: (value) {
                                  if (value == 'open') {
                                    widget.onTeamSelected(team);
                                  } else if (value == 'delete') {
                                    deleteTeam(team);
                                  }
                                },
                              ),
                              onTap: () => widget.onTeamSelected(team),
                            ),
                          );
                        },
                      ),
                    ),
      floatingActionButton: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          FloatingActionButton.small(
            heroTag: 'join',
            onPressed: () => setState(() => showJoinDialog = true),
            child: const Icon(Icons.group_add),
          ),
          const SizedBox(height: 12),
          FloatingActionButton.extended(
            heroTag: 'create',
            onPressed: () => setState(() => showCreateDialog = true),
            icon: const Icon(Icons.add),
            label: const Text('Tạo nhóm'),
          ),
        ],
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
      bottomSheet: showCreateDialog
          ? _buildCreateDialog()
          : showJoinDialog
              ? _buildJoinDialog()
              : null,
    );
  }

  Widget _buildCreateDialog() {
    return Container(
      padding: EdgeInsets.only(
        left: 24,
        right: 24,
        top: 24,
        bottom: MediaQuery.of(context).viewInsets.bottom + 24,
      ),
      decoration: const BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              const Expanded(
                child: Text(
                  'Tạo nhóm mới',
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                ),
              ),
              IconButton(
                icon: const Icon(Icons.close),
                onPressed: () => setState(() => showCreateDialog = false),
              ),
            ],
          ),
          const SizedBox(height: 20),
          TextField(
            controller: nameController,
            decoration: const InputDecoration(
              labelText: 'Tên nhóm *',
              border: OutlineInputBorder(),
            ),
            autofocus: true,
          ),
          const SizedBox(height: 16),
          TextField(
            controller: descController,
            decoration: const InputDecoration(
              labelText: 'Mô tả',
              border: OutlineInputBorder(),
            ),
            maxLines: 3,
          ),
          const SizedBox(height: 20),
          FilledButton(
            onPressed: saving ? null : createTeam,
            style: FilledButton.styleFrom(
              padding: const EdgeInsets.symmetric(vertical: 16),
            ),
            child: saving
                ? const SizedBox(
                    height: 20,
                    width: 20,
                    child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white),
                  )
                : const Text('Tạo nhóm'),
          ),
        ],
      ),
    );
  }

  Widget _buildJoinDialog() {
    return Container(
      padding: EdgeInsets.only(
        left: 24,
        right: 24,
        top: 24,
        bottom: MediaQuery.of(context).viewInsets.bottom + 24,
      ),
      decoration: const BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              const Expanded(
                child: Text(
                  'Tham gia nhóm',
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                ),
              ),
              IconButton(
                icon: const Icon(Icons.close),
                onPressed: () => setState(() => showJoinDialog = false),
              ),
            ],
          ),
          const SizedBox(height: 20),
          TextField(
            controller: joinCodeController,
            decoration: const InputDecoration(
              labelText: 'Mã mời (6 ký tự)',
              border: OutlineInputBorder(),
            ),
            textCapitalization: TextCapitalization.characters,
            maxLength: 6,
            autofocus: true,
          ),
          const SizedBox(height: 20),
          FilledButton(
            onPressed: saving ? null : joinTeam,
            style: FilledButton.styleFrom(
              padding: const EdgeInsets.symmetric(vertical: 16),
            ),
            child: saving
                ? const SizedBox(
                    height: 20,
                    width: 20,
                    child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white),
                  )
                : const Text('Tham gia'),
          ),
        ],
      ),
    );
  }
}

class _Chip extends StatelessWidget {
  const _Chip({required this.icon, required this.label});

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
          Icon(icon, size: 14, color: const Color(0xFF6E461F)),
          const SizedBox(width: 4),
          Text(
            label,
            style: const TextStyle(fontSize: 12, color: Color(0xFF6E461F)),
          ),
        ],
      ),
    );
  }
}
