import 'package:flutter/material.dart';

import '../api/orca_api.dart';
import '../models.dart';

class MarketplaceScreen extends StatefulWidget {
  const MarketplaceScreen({
    required this.api,
    required this.session,
    required this.myTeams,
    required this.onBack,
    required this.onCreateOrder,
    super.key,
  });

  final OrcaApi api;
  final AuthSession session;
  final List<TeamSummary> myTeams;
  final VoidCallback onBack;
  final void Function(MarketplaceTeam seller) onCreateOrder;

  @override
  State<MarketplaceScreen> createState() => _MarketplaceScreenState();
}

class _MarketplaceScreenState extends State<MarketplaceScreen> {
  List<MarketplaceTeam> teams = [];
  List<MarketplaceTeam> filteredTeams = [];
  bool loading = true;
  String? error;
  String searchQuery = '';
  String? selectedSpecialty;

  final specialties = [
    'Tất cả',
    'Rang cà phê',
    'Gia công OEM',
    'Đóng gói',
    'Xay cà phê',
    'QC kiểm định',
    'Xuất khẩu',
  ];

  @override
  void initState() {
    super.initState();
    loadTeams();
  }

  Future<void> loadTeams() async {
    setState(() {
      loading = true;
      error = null;
    });
    try {
      final data = await widget.api.getAllTeams();
      if (!mounted) return;
      setState(() {
        teams = data;
        filteredTeams = data;
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

  void filterTeams() {
    setState(() {
      filteredTeams = teams.where((team) {
        final matchesSearch = searchQuery.isEmpty ||
            team.name.toLowerCase().contains(searchQuery.toLowerCase()) ||
            (team.description?.toLowerCase().contains(searchQuery.toLowerCase()) ?? false);
        final matchesSpecialty = selectedSpecialty == null ||
            selectedSpecialty == 'Tất cả' ||
            team.specialty == selectedSpecialty;
        return matchesSearch && matchesSpecialty;
      }).toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: widget.onBack,
        ),
        title: const Text('Marketplace'),
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: loadTeams,
          ),
        ],
      ),
      body: Column(
        children: [
          // Search & Filter
          Container(
            padding: const EdgeInsets.all(16),
            color: Colors.white,
            child: Column(
              children: [
                TextField(
                  decoration: InputDecoration(
                    hintText: 'Tìm kiếm xưởng...',
                    prefixIcon: const Icon(Icons.search),
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(12),
                    ),
                    filled: true,
                    fillColor: Colors.grey[100],
                  ),
                  onChanged: (value) {
                    searchQuery = value;
                    filterTeams();
                  },
                ),
                const SizedBox(height: 12),
                SizedBox(
                  height: 36,
                  child: ListView.separated(
                    scrollDirection: Axis.horizontal,
                    itemCount: specialties.length,
                    separatorBuilder: (_, __) => const SizedBox(width: 8),
                    itemBuilder: (ctx, index) {
                      final specialty = specialties[index];
                      final isSelected = selectedSpecialty == specialty ||
                          (selectedSpecialty == null && specialty == 'Tất cả');
                      return FilterChip(
                        label: Text(specialty),
                        selected: isSelected,
                        onSelected: (selected) {
                          setState(() {
                            selectedSpecialty =
                                selected && specialty != 'Tất cả' ? specialty : null;
                            filterTeams();
                          });
                        },
                        backgroundColor: Colors.grey[200],
                        selectedColor: const Color(0xFFD99C5F),
                        labelStyle: TextStyle(
                          color: isSelected ? Colors.white : Colors.black,
                        ),
                      );
                    },
                  ),
                ),
              ],
            ),
          ),

          // Results
          Expanded(
            child: loading
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
                    : filteredTeams.isEmpty
                        ? Center(
                            child: Column(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                const Icon(Icons.search_off, size: 64, color: Colors.grey),
                                const SizedBox(height: 16),
                                const Text('Không tìm thấy xưởng nào'),
                                const SizedBox(height: 8),
                                const Text(
                                  'Thử tìm kiếm với từ khóa khác',
                                  style: TextStyle(color: Colors.grey),
                                ),
                              ],
                            ),
                          )
                        : RefreshIndicator(
                            onRefresh: loadTeams,
                            child: ListView.builder(
                              padding: const EdgeInsets.all(16),
                              itemCount: filteredTeams.length,
                              itemBuilder: (ctx, index) {
                                final team = filteredTeams[index];
                                return Card(
                                  margin: const EdgeInsets.only(bottom: 16),
                                  child: InkWell(
                                    onTap: () => _showTeamDetail(team),
                                    borderRadius: BorderRadius.circular(12),
                                    child: Padding(
                                      padding: const EdgeInsets.all(16),
                                      child: Column(
                                        crossAxisAlignment: CrossAxisAlignment.start,
                                        children: [
                                          Row(
                                            children: [
                                              CircleAvatar(
                                                backgroundColor: const Color(0xFF3B2414),
                                                child: Text(
                                                  team.name.isNotEmpty
                                                      ? team.name[0].toUpperCase()
                                                      : '?',
                                                  style: const TextStyle(
                                                    color: Colors.white,
                                                    fontWeight: FontWeight.bold,
                                                  ),
                                                ),
                                              ),
                                              const SizedBox(width: 12),
                                              Expanded(
                                                child: Column(
                                                  crossAxisAlignment: CrossAxisAlignment.start,
                                                  children: [
                                                    Text(
                                                      team.name,
                                                      style: const TextStyle(
                                                        fontSize: 16,
                                                        fontWeight: FontWeight.bold,
                                                      ),
                                                    ),
                                                    if (team.ownerName != null)
                                                      Text(
                                                        'by ${team.ownerName}',
                                                        style: const TextStyle(
                                                          color: Colors.grey,
                                                          fontSize: 12,
                                                        ),
                                                      ),
                                                  ],
                                                ),
                                              ),
                                              _TrustBadge(score: team.trustScore),
                                            ],
                                          ),
                                          if (team.description != null) ...[
                                            const SizedBox(height: 12),
                                            Text(
                                              team.description!,
                                              maxLines: 2,
                                              overflow: TextOverflow.ellipsis,
                                            ),
                                          ],
                                          const SizedBox(height: 12),
                                          Wrap(
                                            spacing: 8,
                                            runSpacing: 8,
                                            children: [
                                              if (team.region != null)
                                                _Tag(
                                                  icon: Icons.location_on,
                                                  text: team.region!,
                                                ),
                                              if (team.specialty != null)
                                                _Tag(
                                                  icon: Icons.star,
                                                  text: team.specialty!,
                                                ),
                                              _Tag(
                                                icon: Icons.people,
                                                text: '${team.memberCount} thành viên',
                                              ),
                                              if (team.capacity != null)
                                                _Tag(
                                                  icon: Icons.factory,
                                                  text: team.capacity!,
                                                ),
                                            ],
                                          ),
                                          const SizedBox(height: 16),
                                          SizedBox(
                                            width: double.infinity,
                                            child: FilledButton.icon(
                                              onPressed: () => widget.onCreateOrder(team),
                                              icon: const Icon(Icons.shopping_cart),
                                              label: const Text('Đặt gia công'),
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                                  ),
                                );
                              },
                            ),
                          ),
          ),
        ],
      ),
    );
  }

  void _showTeamDetail(MarketplaceTeam team) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      builder: (ctx) => DraggableScrollableSheet(
        initialChildSize: 0.6,
        maxChildSize: 0.9,
        minChildSize: 0.4,
        expand: false,
        builder: (_, controller) => SingleChildScrollView(
          controller: controller,
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Center(
                child: Container(
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: Colors.grey[300],
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
              ),
              const SizedBox(height: 24),
              Row(
                children: [
                  CircleAvatar(
                    radius: 32,
                    backgroundColor: const Color(0xFF3B2414),
                    child: Text(
                      team.name.isNotEmpty ? team.name[0].toUpperCase() : '?',
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 24,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          team.name,
                          style: const TextStyle(
                            fontSize: 20,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        if (team.ownerName != null)
                          Text(
                            'by ${team.ownerName}',
                            style: const TextStyle(color: Colors.grey),
                          ),
                      ],
                    ),
                  ),
                  _TrustBadge(score: team.trustScore),
                ],
              ),
              const SizedBox(height: 24),
              if (team.description != null) ...[
                const Text(
                  'Mô tả',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 8),
                Text(team.description!),
                const SizedBox(height: 24),
              ],
              const Text(
                'Thông tin',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 12),
              _DetailRow(
                icon: Icons.location_on,
                label: 'Khu vực',
                value: team.region ?? 'Chưa cập nhật',
              ),
              _DetailRow(
                icon: Icons.star,
                label: 'Chuyên môn',
                value: team.specialty ?? 'Chưa cập nhật',
              ),
              _DetailRow(
                icon: Icons.factory,
                label: 'Công suất',
                value: team.capacity ?? 'Chưa cập nhật',
              ),
              _DetailRow(
                icon: Icons.people,
                label: 'Thành viên',
                value: '${team.memberCount} người',
              ),
              _DetailRow(
                icon: Icons.verified,
                label: 'Trạng thái',
                value: team.isPublished ? 'Đang hoạt động' : 'Chưa đăng',
              ),
              const SizedBox(height: 32),
              SizedBox(
                width: double.infinity,
                child: FilledButton.icon(
                  onPressed: () {
                    Navigator.pop(ctx);
                    widget.onCreateOrder(team);
                  },
                  icon: const Icon(Icons.shopping_cart),
                  label: const Text('Đặt gia công'),
                  style: FilledButton.styleFrom(
                    padding: const EdgeInsets.symmetric(vertical: 16),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _TrustBadge extends StatelessWidget {
  const _TrustBadge({required this.score});

  final int score;

  @override
  Widget build(BuildContext context) {
    final color = score >= 80
        ? Colors.green
        : score >= 50
            ? Colors.orange
            : Colors.red;

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
      decoration: BoxDecoration(
        color: color.withOpacity(0.1),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: color),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.verified, size: 16, color: color),
          const SizedBox(width: 4),
          Text(
            '$score%',
            style: TextStyle(
              color: color,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }
}

class _Tag extends StatelessWidget {
  const _Tag({required this.icon, required this.text});

  final IconData icon;
  final String text;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
      decoration: BoxDecoration(
        color: const Color(0xFFF1E8DE),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 14, color: const Color(0xFF6E461F)),
          const SizedBox(width: 4),
          Text(
            text,
            style: const TextStyle(
              fontSize: 12,
              color: Color(0xFF6E461F),
            ),
          ),
        ],
      ),
    );
  }
}

class _DetailRow extends StatelessWidget {
  const _DetailRow({
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
      padding: const EdgeInsets.only(bottom: 12),
      child: Row(
        children: [
          Icon(icon, size: 20, color: Colors.grey),
          const SizedBox(width: 12),
          SizedBox(
            width: 100,
            child: Text(
              label,
              style: const TextStyle(color: Colors.grey),
            ),
          ),
          Expanded(
            child: Text(
              value,
              style: const TextStyle(fontWeight: FontWeight.w500),
            ),
          ),
        ],
      ),
    );
  }
}
