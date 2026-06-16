import 'dart:convert';
import 'dart:io';

import '../models.dart';

const defaultBaseUrl = 'http://10.0.2.2:8080';

class ApiException implements Exception {
  ApiException(this.message);

  final String message;

  @override
  String toString() => message;
}

class OrcaApi {
  OrcaApi({this.baseUrl = defaultBaseUrl});

  final String baseUrl;
  final HttpClient _client = HttpClient()
    ..connectionTimeout = const Duration(seconds: 12);

  String? _token;

  bool get isLoggedIn => _token != null;

  Future<AuthSession> login({
    required String username,
    required String password,
  }) async {
    final json = await _request<Map<String, dynamic>>(
      'POST',
      '/api/auth/login',
      body: {'username': username, 'password': password},
      authenticated: false,
    );
    final session = AuthSession.fromJson(json);
    if (session.token.isEmpty) {
      throw ApiException('Backend không trả token đăng nhập.');
    }
    _token = session.token;
    return session;
  }

  void logout() {
    _token = null;
  }

  Future<List<TeamSummary>> getMyTeams() async {
    final list = await _request<List<dynamic>>('GET', '/api/teams');
    return list
        .whereType<Map<String, dynamic>>()
        .map(TeamSummary.fromJson)
        .where((team) => team.id.isNotEmpty)
        .toList();
  }

  Future<List<InterOrder>> getInboundOrders(String teamId) async {
    final list = await _request<List<dynamic>>(
      'GET',
      '/api/inter-orders/inbound/$teamId',
    );
    return list
        .whereType<Map<String, dynamic>>()
        .map(InterOrder.fromJson)
        .toList();
  }

  Future<List<InterOrder>> getOutboundOrders(String teamId) async {
    final list = await _request<List<dynamic>>(
      'GET',
      '/api/inter-orders/outbound/$teamId',
    );
    return list
        .whereType<Map<String, dynamic>>()
        .map(InterOrder.fromJson)
        .toList();
  }

  Future<void> acceptOrder(String orderId) async {
    await _request<Object?>('POST', '/api/inter-orders/$orderId/accept');
  }

  Future<void> rejectOrder(String orderId) async {
    await _request<Object?>('POST', '/api/inter-orders/$orderId/reject');
  }

  Future<void> cancelOrder(String orderId) async {
    await _request<Object?>('POST', '/api/inter-orders/$orderId/cancel');
  }

  Future<void> completeOrder(String orderId) async {
    await _request<Object?>('POST', '/api/inter-orders/$orderId/complete');
  }

  Future<List<OrcaNotification>> getNotifications() async {
    final list = await _request<List<dynamic>>('GET', '/api/notifications');
    return list
        .whereType<Map<String, dynamic>>()
        .map(OrcaNotification.fromJson)
        .toList();
  }

  Future<int> getUnreadCount() async {
    final json = await _request<Map<String, dynamic>>(
      'GET',
      '/api/notifications/unread-count',
    );
    final value = json['count'];
    if (value is int) return value;
    return int.tryParse(value?.toString() ?? '') ?? 0;
  }

  Future<void> markAllNotificationsRead() async {
    await _request<Object?>('PATCH', '/api/notifications/read-all');
  }

  Future<T> _request<T>(
    String method,
    String path, {
    Map<String, dynamic>? body,
    bool authenticated = true,
  }) async {
    final uri = Uri.parse('$baseUrl$path');
    final request = await _client.openUrl(method, uri);
    request.headers.contentType = ContentType.json;
    request.headers.set(HttpHeaders.acceptHeader, 'application/json');
    if (authenticated && _token != null) {
      request.headers.set(HttpHeaders.authorizationHeader, 'Bearer $_token');
    }
    if (body != null) {
      request.write(jsonEncode(body));
    }

    final response = await request.close();
    final text = await response.transform(utf8.decoder).join();
    final decoded = text.isEmpty ? null : jsonDecode(text);

    if (response.statusCode < 200 || response.statusCode >= 300) {
      if (decoded is Map<String, dynamic> && decoded['error'] != null) {
        throw ApiException(decoded['error'].toString());
      }
      throw ApiException('API lỗi ${response.statusCode}: $text');
    }

    return decoded as T;
  }
}
