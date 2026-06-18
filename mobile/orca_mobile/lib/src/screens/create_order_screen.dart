import 'package:flutter/material.dart';

import '../api/orca_api.dart';
import '../models.dart';

class CreateOrderScreen extends StatefulWidget {
  const CreateOrderScreen({
    required this.api,
    required this.session,
    required this.sellerTeam,
    required this.onBack,
    required this.onOrderCreated,
    super.key,
  });

  final OrcaApi api;
  final AuthSession session;
  final MarketplaceTeam sellerTeam;
  final VoidCallback onBack;
  final VoidCallback onOrderCreated;

  @override
  State<CreateOrderScreen> createState() => _CreateOrderScreenState();
}

class _CreateOrderScreenState extends State<CreateOrderScreen> {
  final _formKey = GlobalKey<FormState>();
  final titleController = TextEditingController();
  final descriptionController = TextEditingController();
  final quantityController = TextEditingController();
  final phoneController = TextEditingController();
  final addressController = TextEditingController();

  DateTime deadline = DateTime.now().add(const Duration(days: 7));
  bool saving = false;

  @override
  void dispose() {
    titleController.dispose();
    descriptionController.dispose();
    quantityController.dispose();
    phoneController.dispose();
    addressController.dispose();
    super.dispose();
  }

  Future<void> _selectDeadline() async {
    final picked = await showDatePicker(
      context: context,
      initialDate: deadline,
      firstDate: DateTime.now(),
      lastDate: DateTime.now().add(const Duration(days: 365)),
    );
    if (picked != null) {
      setState(() => deadline = picked);
    }
  }

  Future<void> submitOrder() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => saving = true);
    try {
      await widget.api.createOrder(
        sellerTeamId: widget.sellerTeam.id,
        title: titleController.text.trim(),
        description: descriptionController.text.trim(),
        quantity: int.parse(quantityController.text.trim()),
        deadline: deadline,
        contactPhone: phoneController.text.trim().isEmpty
            ? null
            : phoneController.text.trim(),
        deliveryAddress: addressController.text.trim().isEmpty
            ? null
            : addressController.text.trim(),
      );

      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Đã gửi yêu cầu đặt hàng thành công!'),
          backgroundColor: Colors.green,
        ),
      );
      widget.onOrderCreated();
    } catch (e) {
      if (!mounted) return;
      setState(() => saving = false);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Lỗi: $e'),
          backgroundColor: Colors.red,
        ),
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
        title: const Text('Đặt gia công'),
      ),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: const EdgeInsets.all(20),
          children: [
            // Seller Info Card
            Card(
              color: const Color(0xFFFFF4E8),
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Row(
                  children: [
                    CircleAvatar(
                      backgroundColor: const Color(0xFF3B2414),
                      child: Text(
                        widget.sellerTeam.name.isNotEmpty
                            ? widget.sellerTeam.name[0].toUpperCase()
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
                          const Text(
                            'Đặt hàng tại',
                            style: TextStyle(
                              fontSize: 12,
                              color: Colors.grey,
                            ),
                          ),
                          Text(
                            widget.sellerTeam.name,
                            style: const TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 16,
                            ),
                          ),
                        ],
                      ),
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 8,
                        vertical: 4,
                      ),
                      decoration: BoxDecoration(
                        color: Colors.green.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(Icons.verified,
                              size: 14, color: Colors.green),
                          const SizedBox(width: 4),
                          Text(
                            'Uy tín ${widget.sellerTeam.trustScore}%',
                            style: const TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.bold,
                              color: Colors.green,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 24),

            // Title
            TextFormField(
              controller: titleController,
              decoration: const InputDecoration(
                labelText: 'Tiêu đề đơn hàng *',
                hintText: 'VD: Rang 50kg cà phê Arabica',
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.title),
              ),
              validator: (value) {
                if (value == null || value.trim().isEmpty) {
                  return 'Vui lòng nhập tiêu đề';
                }
                return null;
              },
            ),
            const SizedBox(height: 16),

            // Description
            TextFormField(
              controller: descriptionController,
              decoration: const InputDecoration(
                labelText: 'Mô tả chi tiết',
                hintText: 'Mô tả yêu cầu gia công, thông số kỹ thuật...',
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.description),
              ),
              maxLines: 4,
            ),
            const SizedBox(height: 16),

            // Quantity
            TextFormField(
              controller: quantityController,
              decoration: const InputDecoration(
                labelText: 'Số lượng (kg) *',
                hintText: 'VD: 100',
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.scale),
              ),
              keyboardType: TextInputType.number,
              validator: (value) {
                if (value == null || value.trim().isEmpty) {
                  return 'Vui lòng nhập số lượng';
                }
                final qty = int.tryParse(value.trim());
                if (qty == null || qty <= 0) {
                  return 'Số lượng phải lớn hơn 0';
                }
                return null;
              },
            ),
            const SizedBox(height: 16),

            // Deadline
            InkWell(
              onTap: _selectDeadline,
              child: InputDecorator(
                decoration: const InputDecoration(
                  labelText: 'Hạn giao hàng *',
                  border: OutlineInputBorder(),
                  prefixIcon: Icon(Icons.event),
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      '${deadline.day.toString().padLeft(2, '0')}/${deadline.month.toString().padLeft(2, '0')}/${deadline.year}',
                      style: const TextStyle(fontSize: 16),
                    ),
                    const Icon(Icons.calendar_today, size: 20),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 24),

            // Delivery Info
            const Text(
              'Thông tin giao hàng',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 12),

            // Phone
            TextFormField(
              controller: phoneController,
              decoration: const InputDecoration(
                labelText: 'Số điện thoại liên hệ',
                hintText: 'VD: 0912345678',
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.phone),
              ),
              keyboardType: TextInputType.phone,
            ),
            const SizedBox(height: 16),

            // Address
            TextFormField(
              controller: addressController,
              decoration: const InputDecoration(
                labelText: 'Địa chỉ giao hàng',
                hintText: 'VD: 123 Nguyễn Trãi, Q1, TP.HCM',
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.location_on),
              ),
              maxLines: 2,
            ),
            const SizedBox(height: 32),

            // Submit Button
            FilledButton.icon(
              onPressed: saving ? null : submitOrder,
              icon: saving
                  ? const SizedBox(
                      height: 20,
                      width: 20,
                      child: CircularProgressIndicator(
                        strokeWidth: 2,
                        color: Colors.white,
                      ),
                    )
                  : const Icon(Icons.send),
              label: Text(saving ? 'Đang gửi...' : 'Gửi yêu cầu'),
              style: FilledButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 16),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
