# Knowledge Document: AiServiceClient.java (Chunk 4/7)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AiServiceClient.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "chat"
  ],
  "logical_type": "Service",
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, chat

## Source Code Chunk
```java
Tasks(fallbackTasks);
        }
        
        return result;
    }

    private AiParseResult parseWithGemini(String text, String memberContext, String historyContext, String inventoryContext) throws Exception {
        String memberSection = "";
        if (memberContext != null && !memberContext.isEmpty()) {
            memberSection = "\n--- DANH SÁCH THÀNH VIÊN VÀ NHÃN DÁN CÔNG VIỆC ---\n"
                    + memberContext + "\n"
                    + "PHÂN CÔNG: Dựa vào Job Labels để gán người phù hợp nhất vào trường 'assignee'.\n\n";
        }

        String historySection = "";
        if (historyContext != null && !historyContext.isEmpty()) {
            historySection = "\n--- LỊCH SỬ CHAT TRƯỚC ĐÓ ---\n"
                    + historyContext + "\n\n"
                    + "QUY TẮC CẬP NHẬT: Ưu tiên giữ cấu trúc kế hoạch cũ, chỉ thay đổi các thông tin người dùng vừa yêu cầu sửa đổi.\n";
        }

        String prompt = "HỆ THỐNG ĐIỀU PHỐI & GIAO VIỆC TỰ ĐỘNG\n"
                + "Vai trò: Bạn là nhân sự thông minh. Nhiệm vụ: Nhận yêu cầu, phân rã công việc và giao việc.\n\n"
                + "1. QUY TẮC TƯƠNG TÁC (Multi-turn):\n"
                + "- LUÔN bắt đầu phản hồi bằng lời chào: 'Chào anh/chị'.\n"
                + "- Xưng hô: Xưng là 'em', gọi User là 'anh/chị'.\n"
                + "- Nếu User thiếu thông tin TRỌNG YẾU (deadline, số lượng) hoặc yêu cầu chưa rõ ràng: Hãy khéo léo ĐẶT CÂU HỎI vào `description` để xin thêm thông tin và đặt `needsClarification` = true.\n"
                + "- LUÔN GỢI Ý CÂU HỎI (Proactive): Ngay cả khi đã có kế hoạch, hãy liệt kê 1-3 câu hỏi gợi ý để tối ưu kế hoạch vào mảng `suggestedQuestions` (ví dụ: 'Anh/chị có muốn bổ sung thông tin cho sản lượng không?', v.v.)\n"
                + "- Nếu User yêu cầu sửa đổi: Cập nhật trường tương ứng và giữ nguyên phần khác.\n"
                + "2. PHÂN RÃ CÔNG VIỆC:\n"
                + "- Trình bày BẢNG ROADMAP (markdown) trong `description` sau lời chào và câu hỏi.\n"
                + "- Từng task ghi rõ [Ca: Sáng/Chiều] ở đầu mô tả.\n\n"
                + "3. PHONG CÁCH: Lịch sự, chuyên nghiệp, hỗ trợ tận tâm.\n\n"
                + "--- CONTEXT ---\n"
                + memberSection
                + historySection
                + (inventoryContext != null ? inventoryContext : "")
                + "Định dạng JSON Phản hồi (BẮT BUỘC):\n"

```
