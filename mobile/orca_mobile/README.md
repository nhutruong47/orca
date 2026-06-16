# ORCA Mobile

Ứng dụng mobile Flutter cho ORCA, kết nối trực tiếp với backend Spring Boot.

## Chức năng MVP

- Đăng nhập bằng tài khoản ORCA.
- Xem tổng quan người dùng, nhóm xưởng và số thông báo chưa đọc.
- Chọn xưởng để xem đơn liên xưởng.
- Xem đơn nhận và đơn đã đi đặt.
- Hiện thông báo khi có đơn đặt hàng mới đang chờ phản hồi.
- Chấp nhận, từ chối, hoàn thành hoặc hủy đơn.
- Xem thông báo và đánh dấu đã đọc tất cả.

## Chạy local

Backend local đang dùng `http://localhost:8080`. Với Android Emulator, app mặc định gọi:

```text
http://10.0.2.2:8080
```

Nếu chạy trên máy thật, sửa `defaultBaseUrl` trong `lib/src/api/orca_api.dart` sang IP LAN của máy chạy backend, ví dụ:

```dart
const defaultBaseUrl = 'http://192.168.1.10:8080';
```

Nếu Flutter CLI hoạt động bình thường:

```bash
flutter create . --platforms android,ios
flutter pub get
flutter run
```
