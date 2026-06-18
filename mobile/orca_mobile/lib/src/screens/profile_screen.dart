import 'package:flutter/material.dart';

import '../models.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({
    required this.session,
    required this.onBack,
    required this.onLogout,
    super.key,
  });

  final AuthSession session;
  final VoidCallback onBack;
  final VoidCallback onLogout;

  @override
  Widget build(BuildContext context) {
    final name = session.fullName?.isNotEmpty == true
        ? session.fullName!
        : session.username;

    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: onBack,
        ),
        title: const Text('Hồ sơ cá nhân'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(20),
        children: [
          // Avatar Card
          Card(
            child: Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                children: [
                  CircleAvatar(
                    radius: 50,
                    backgroundColor: const Color(0xFF3B2414),
                    child: Text(
                      name.isNotEmpty ? name[0].toUpperCase() : 'O',
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 40,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  const SizedBox(height: 16),
                  Text(
                    name,
                    style: const TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    '@${session.username}',
                    style: const TextStyle(
                      color: Colors.grey,
                      fontSize: 16,
                    ),
                  ),
                  const SizedBox(height: 12),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 16,
                      vertical: 8,
                    ),
                    decoration: BoxDecoration(
                      color: const Color(0xFFF1E8DE),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        const Icon(
                          Icons.person,
                          size: 18,
                          color: Color(0xFF6E461F),
                        ),
                        const SizedBox(width: 8),
                        Text(
                          session.role ?? 'Thành viên',
                          style: const TextStyle(
                            fontWeight: FontWeight.bold,
                            color: Color(0xFF6E461F),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 20),

          // Info Section
          Card(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Padding(
                  padding: EdgeInsets.all(16),
                  child: Text(
                    'Thông tin tài khoản',
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                const Divider(height: 1),
                _ProfileRow(
                  icon: Icons.badge,
                  label: 'User ID',
                  value: session.id,
                ),
                _ProfileRow(
                  icon: Icons.person_outline,
                  label: 'Tên đăng nhập',
                  value: session.username,
                ),
                _ProfileRow(
                  icon: Icons.badge_outlined,
                  label: 'Họ tên',
                  value: session.fullName ?? 'Chưa cập nhật',
                ),
                _ProfileRow(
                  icon: Icons.mail_outline,
                  label: 'Email',
                  value: session.email ?? 'Chưa cập nhật',
                ),
                _ProfileRow(
                  icon: Icons.workspace_premium_outlined,
                  label: 'Vai trò',
                  value: session.role ?? 'Thành viên',
                ),
              ],
            ),
          ),
          const SizedBox(height: 20),

          // Security Section
          Card(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Padding(
                  padding: EdgeInsets.all(16),
                  child: Text(
                    'Bảo mật',
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                const Divider(height: 1),
                ListTile(
                  leading: const CircleAvatar(
                    backgroundColor: Color(0xFFE7F7ED),
                    child: Icon(
                      Icons.check_circle,
                      color: Colors.green,
                    ),
                  ),
                  title: const Text('Mật khẩu'),
                  subtitle: const Text('Được mã hóa BCrypt'),
                  trailing: const Icon(Icons.lock, color: Colors.grey),
                ),
                ListTile(
                  leading: const CircleAvatar(
                    backgroundColor: Color(0xFFE7F7ED),
                    child: Icon(
                      Icons.check_circle,
                      color: Colors.green,
                    ),
                  ),
                  title: const Text('Xác thực'),
                  subtitle: const Text('JWT Token đang hoạt động'),
                  trailing: const Icon(Icons.verified_user, color: Colors.grey),
                ),
              ],
            ),
          ),
          const SizedBox(height: 32),

          // Logout Button
          OutlinedButton.icon(
            onPressed: () {
              showDialog(
                context: context,
                builder: (ctx) => AlertDialog(
                  title: const Text('Đăng xuất'),
                  content: const Text('Bạn có chắc muốn đăng xuất?'),
                  actions: [
                    TextButton(
                      onPressed: () => Navigator.pop(ctx),
                      child: const Text('Hủy'),
                    ),
                    FilledButton(
                      onPressed: () {
                        Navigator.pop(ctx);
                        onLogout();
                      },
                      style: FilledButton.styleFrom(
                        backgroundColor: Colors.red,
                      ),
                      child: const Text('Đăng xuất'),
                    ),
                  ],
                ),
              );
            },
            icon: const Icon(Icons.logout, color: Colors.red),
            label: const Text(
              'Đăng xuất',
              style: TextStyle(color: Colors.red),
            ),
            style: OutlinedButton.styleFrom(
              padding: const EdgeInsets.symmetric(vertical: 16),
              side: const BorderSide(color: Colors.red),
            ),
          ),
        ],
      ),
    );
  }
}

class _ProfileRow extends StatelessWidget {
  const _ProfileRow({
    required this.icon,
    required this.label,
    required this.value,
  });

  final IconData icon;
  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: Icon(icon, color: const Color(0xFF6E461F)),
      title: Text(label),
      subtitle: Text(
        value,
        style: const TextStyle(
          fontWeight: FontWeight.w500,
          color: Colors.black87,
        ),
      ),
    );
  }
}
