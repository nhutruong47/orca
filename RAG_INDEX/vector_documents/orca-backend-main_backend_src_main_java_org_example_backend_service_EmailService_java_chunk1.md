# Knowledge Document: EmailService.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/EmailService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory"
  ],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory

## Source Code Chunk
```java
 chưa có tài khoản, bạn sẽ được hướng dẫn tạo tài khoản.)\n\n" +
                            "Trân trọng,\nĐội ngũ ORCA");
            mailSender.send(message);
            System.out.println("[EMAIL] ✅ Đã gửi thành công tới " + toEmail);
            return true;
        } catch (Exception e) {
            System.err.println("[EMAIL ERROR] ❌ Không thể gửi tới " + toEmail + ": " + e.getMessage());
            throw new RuntimeException("Gửi email thất bại: " + e.getMessage());
        }
    }
}

```
