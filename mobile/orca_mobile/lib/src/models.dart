class AuthSession {
  const AuthSession({
    required this.token,
    required this.id,
    required this.username,
    this.fullName,
    this.email,
    this.role,
  });

  final String token;
  final String id;
  final String username;
  final String? fullName;
  final String? email;
  final String? role;

  factory AuthSession.fromJson(Map<String, dynamic> json) {
    return AuthSession(
      token: json['token']?.toString() ?? '',
      id: json['id']?.toString() ?? '',
      username: json['username']?.toString() ?? '',
      fullName: json['fullName']?.toString(),
      email: json['email']?.toString(),
      role: json['role']?.toString(),
    );
  }
}

class TeamSummary {
  const TeamSummary({
    required this.id,
    required this.name,
    required this.memberCount,
    required this.trustScore,
    this.ownerName,
    this.region,
    this.specialty,
    this.verificationStatus,
    this.isPublished = false,
    this.description,
    this.capacity,
    this.members = const [],
  });

  final String id;
  final String name;
  final int memberCount;
  final int trustScore;
  final String? ownerName;
  final String? region;
  final String? specialty;
  final String? verificationStatus;
  final bool isPublished;
  final String? description;
  final String? capacity;
  final List<TeamMember> members;

  factory TeamSummary.fromJson(Map<String, dynamic> json) {
    return TeamSummary(
      id: json['id']?.toString() ?? '',
      name: json['name']?.toString() ?? 'Xưởng chưa đặt tên',
      memberCount: _asInt(json['memberCount']),
      trustScore: _asInt(json['trustScore']),
      ownerName: json['ownerName']?.toString(),
      region: json['region']?.toString(),
      specialty: json['specialty']?.toString(),
      verificationStatus: json['verificationStatus']?.toString(),
      isPublished: json['isPublished'] == true,
      description: json['description']?.toString(),
      capacity: json['capacity']?.toString(),
      members: (json['members'] is List ? json['members'] as List : const [])
          .whereType<Map<String, dynamic>>()
          .map(TeamMember.fromJson)
          .toList(),
    );
  }
}

class TeamMember {
  const TeamMember({
    required this.userId,
    required this.username,
    required this.fullName,
    required this.groupRole,
    this.totalTasks = 0,
    this.completedTasks = 0,
    this.completionRate = 0,
    this.jobLabels = const [],
  });

  final String userId;
  final String username;
  final String fullName;
  final String groupRole;
  final int totalTasks;
  final int completedTasks;
  final int completionRate;
  final List<String> jobLabels;

  factory TeamMember.fromJson(Map<String, dynamic> json) {
    return TeamMember(
      userId: json['userId']?.toString() ?? '',
      username: json['username']?.toString() ?? '',
      fullName: json['fullName']?.toString() ?? '',
      groupRole: json['groupRole']?.toString() ?? 'MEMBER',
      totalTasks: _asInt(json['totalTasks']),
      completedTasks: _asInt(json['completedTasks']),
      completionRate: _asInt(json['completionRate']),
      jobLabels: (json['jobLabels'] is List ? json['jobLabels'] as List : const [])
          .map((label) => label.toString())
          .toList(),
    );
  }
}

class GoalSummary {
  const GoalSummary({
    required this.id,
    required this.title,
    required this.status,
    required this.totalTasks,
    required this.completedTasks,
    this.deadline,
    this.teamName,
  });

  final String id;
  final String title;
  final String status;
  final int totalTasks;
  final int completedTasks;
  final DateTime? deadline;
  final String? teamName;

  int get progress {
    if (totalTasks <= 0) return 0;
    return ((completedTasks / totalTasks) * 100).round().clamp(0, 100);
  }

  factory GoalSummary.fromJson(Map<String, dynamic> json) {
    return GoalSummary(
      id: json['id']?.toString() ?? '',
      title: json['title']?.toString() ?? 'Mục tiêu chưa đặt tên',
      status: json['status']?.toString() ?? 'PENDING',
      totalTasks: _asInt(json['totalTasks']),
      completedTasks: _asInt(json['completedTasks']),
      deadline: _parseDate(json['deadline']),
      teamName: json['teamName']?.toString(),
    );
  }
}

class OrcaTask {
  const OrcaTask({
    required this.id,
    required this.title,
    required this.status,
    required this.acceptanceStatus,
    required this.completionPercentage,
    required this.priority,
    this.description,
    this.goalTitle,
    this.memberName,
    this.productionStage,
    this.deadline,
    this.workload = 0,
    this.actualWorkload = 0,
  });

  final String id;
  final String title;
  final String status;
  final String acceptanceStatus;
  final int completionPercentage;
  final int priority;
  final String? description;
  final String? goalTitle;
  final String? memberName;
  final String? productionStage;
  final DateTime? deadline;
  final double workload;
  final double actualWorkload;

  factory OrcaTask.fromJson(Map<String, dynamic> json) {
    return OrcaTask(
      id: json['id']?.toString() ?? '',
      title: json['title']?.toString() ?? 'Công việc chưa đặt tên',
      description: json['description']?.toString(),
      status: json['status']?.toString() ?? 'PENDING',
      acceptanceStatus: json['acceptanceStatus']?.toString() ?? 'WAITING',
      completionPercentage: _asInt(json['completionPercentage']),
      priority: _asInt(json['priority']),
      goalTitle: json['goalTitle']?.toString(),
      memberName: json['memberName']?.toString(),
      productionStage: json['productionStage']?.toString(),
      deadline: _parseDate(json['deadline']),
      workload: _asDouble(json['workload']),
      actualWorkload: _asDouble(json['actualWorkload']),
    );
  }
}

class InterOrder {
  const InterOrder({
    required this.id,
    required this.title,
    required this.status,
    required this.quantity,
    this.description,
    this.buyerTeamName,
    this.sellerTeamName,
    this.deadline,
    this.buyerTrustScore = 100,
    this.cancelledBy,
  });

  final String id;
  final String title;
  final String status;
  final int quantity;
  final String? description;
  final String? buyerTeamName;
  final String? sellerTeamName;
  final DateTime? deadline;
  final int buyerTrustScore;
  final String? cancelledBy;

  factory InterOrder.fromJson(Map<String, dynamic> json) {
    return InterOrder(
      id: json['id']?.toString() ?? '',
      title: json['title']?.toString() ?? 'Đơn chưa đặt tên',
      description: json['description']?.toString(),
      status: json['status']?.toString() ?? 'PENDING',
      quantity: _asInt(json['quantity']),
      buyerTeamName: json['buyerTeamName']?.toString(),
      sellerTeamName: json['sellerTeamName']?.toString(),
      deadline: _parseDate(json['deadline']),
      buyerTrustScore: _asInt(json['buyerTrustScore'], fallback: 100),
      cancelledBy: json['cancelledBy']?.toString(),
    );
  }
}

class InventoryItem {
  const InventoryItem({
    required this.id,
    required this.name,
    required this.quantity,
    required this.unit,
    required this.status,
    this.lowStockThreshold = 0,
  });

  final String id;
  final String name;
  final double quantity;
  final String unit;
  final String status;
  final double lowStockThreshold;

  factory InventoryItem.fromJson(Map<String, dynamic> json) {
    return InventoryItem(
      id: json['id']?.toString() ?? '',
      name: json['name']?.toString() ?? 'Mặt hàng',
      quantity: _asDouble(json['quantity']),
      unit: json['unit']?.toString() ?? '',
      status: json['status']?.toString() ?? 'IN_STOCK',
      lowStockThreshold: _asDouble(json['lowStockThreshold']),
    );
  }
}

class OrcaNotification {
  const OrcaNotification({
    required this.id,
    required this.title,
    required this.message,
    required this.isRead,
    this.type,
    this.createdAt,
  });

  final String id;
  final String title;
  final String message;
  final bool isRead;
  final String? type;
  final DateTime? createdAt;

  factory OrcaNotification.fromJson(Map<String, dynamic> json) {
    return OrcaNotification(
      id: json['id']?.toString() ?? '',
      title: json['title']?.toString() ?? 'Thông báo',
      message: json['message']?.toString() ?? '',
      type: json['type']?.toString(),
      isRead: json['read'] == true || json['isRead'] == true,
      createdAt: _parseDate(json['createdAt']),
    );
  }
}

int _asInt(dynamic value, {int fallback = 0}) {
  if (value is int) return value;
  if (value is num) return value.toInt();
  return int.tryParse(value?.toString() ?? '') ?? fallback;
}

double _asDouble(dynamic value, {double fallback = 0}) {
  if (value is double) return value;
  if (value is num) return value.toDouble();
  return double.tryParse(value?.toString() ?? '') ?? fallback;
}

DateTime? _parseDate(dynamic value) {
  final text = value?.toString();
  if (text == null || text.isEmpty) return null;
  return DateTime.tryParse(text);
}
