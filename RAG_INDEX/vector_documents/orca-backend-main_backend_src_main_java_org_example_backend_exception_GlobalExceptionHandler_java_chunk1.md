# Knowledge Document: GlobalExceptionHandler.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/exception/GlobalExceptionHandler.java",
  "language": "java",
  "module": "exception",
  "business_domain": "security",
  "tags": [
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in exception.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```java
 trùng dữ liệu (UNIQUE constraint) ===
    @ExceptionHandler(DataIntegrityViolationException.class)
    public ResponseEntity<Map<String, Object>> handleDataIntegrity(DataIntegrityViolationException ex) {
        String detail = ex.getMostSpecificCause().getMessage();
        String friendlyMsg;

        if (detail.contains("Duplicate") || detail.contains("UNIQUE") || detail.contains("unique")) {
            friendlyMsg = "Dữ liệu bị trùng! Kiểm tra lại các trường có giá trị duy nhất (SKU, username, mã...)";
        } else if (detail.contains("FOREIGN KEY") || detail.contains("foreign key")) {
            friendlyMsg = "Không thể thực hiện vì có dữ liệu liên kết. Xóa dữ liệu liên quan trước.";
        } else if (detail.contains("NULL") || detail.contains("cannot be null")) {
            friendlyMsg = "Thiếu trường bắt buộc! Vui lòng điền đầy đủ thông tin.";
        } else {
            friendlyMsg = "Lỗi dữ liệu: " + detail;
        }

        return buildResponse(HttpStatus.CONFLICT, "Lỗi dữ liệu", friendlyMsg);
    }

    // === Lỗi thiếu/sai tham số ===
    @ExceptionHandler(MissingServletRequestParameterException.class)
    public ResponseEntity<Map<String, Object>> handleMissingParam(MissingServletRequestParameterException ex) {
        String msg = "Thiếu tham số bắt buộc: " + ex.getParameterName() + " (kiểu: " + ex.getParameterType() + ")";
        return buildResponse(HttpStatus.BAD_REQUEST, "Thiếu tham số", msg);
    }

    // === Lỗi kiểu dữ liệu sai (VD: truyền string cho UUID) ===
    @ExceptionHandler(MethodArgumentTypeMismatchException.class)
    public ResponseEntity<Map<String, Object>> handleTypeMismatch(MethodArgumentTypeMismatchException ex) {
        String msg = "Tham số '" + ex.getName() + "' có giá trị không hợp lệ: '" + ex.getValue()
                + "'. Kiểu yêu cầu: "
                + (ex.getRequiredType() != null ? ex.getRequiredType().getSimpleName() : "không xác định");
        return buildResponse(HttpStatus.BAD_REQUEST, "Sai kiểu dữ liệu", msg);
    }

    // === Lỗi body JSON không đọc được ===
    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<Map<String, Object>> handleBadJson(HttpMessageNotReadableException ex) {
        return buildResponse(HttpStatus.BAD_REQUEST, "Lỗi định dạng",
                "Dữ liệu gửi lên không đúng định dạng JSON. Kiểm tra lại body request.");
    }


```
