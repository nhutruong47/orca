# Knowledge Document: GlobalExceptionHandler.java (Chunk 3/3)

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
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in exception.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```java
 kiểu dữ liệu", msg);
    }

    // === Lỗi body JSON không đọc được ===
    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<Map<String, Object>> handleBadJson(HttpMessageNotReadableException ex) {
        return buildResponse(HttpStatus.BAD_REQUEST, "Lỗi định dạng",
                "Dữ liệu gửi lên không đúng định dạng JSON. Kiểm tra lại body request.");
    }

    // === Lỗi validation (@Valid) ===
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, Object>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, Object> body = new LinkedHashMap<>();
        body.put("timestamp", LocalDateTime.now().toString());
        body.put("status", 400);
        body.put("error", "Lỗi validation");

        Map<String, String> fieldErrors = new LinkedHashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(fe -> fieldErrors.put(fe.getField(), fe.getDefaultMessage()));
        body.put("fields", fieldErrors);
        body.put("message", "Có " + fieldErrors.size() + " trường không hợp lệ");

        return ResponseEntity.badRequest().body(body);
    }

    // === Lỗi chung ===
    @ExceptionHandler(Exception.class)
    public ResponseEntity<Map<String, Object>> handleGeneral(Exception ex) {
        return buildResponse(HttpStatus.INTERNAL_SERVER_ERROR, "Lỗi hệ thống",
                ex.getClass().getSimpleName() + ": " + ex.getMessage());
    }

    private ResponseEntity<Map<String, Object>> buildResponse(HttpStatus status, String error, String message) {
        Map<String, Object> body = new LinkedHashMap<>();
        body.put("timestamp", LocalDateTime.now().toString());
        body.put("status", status.value());
        body.put("error", error);
        body.put("message", message);
        return ResponseEntity.status(status).body(body);
    }
}

```
