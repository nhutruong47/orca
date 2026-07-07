# Knowledge Document: GlobalExceptionHandler.java (Chunk 1/3)

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
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in exception.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```java
package org.example.backend.exception;

import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.MissingServletRequestParameterException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.method.annotation.MethodArgumentTypeMismatchException;
import org.springframework.web.server.ResponseStatusException;

import java.time.LocalDateTime;
import java.util.LinkedHashMap;
import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResponseStatusException.class)
    public ResponseEntity<Map<String, Object>> handleResponseStatusException(ResponseStatusException ex) {
        HttpStatus status = HttpStatus.resolve(ex.getStatusCode().value());
        if (status == null) {
            status = HttpStatus.INTERNAL_SERVER_ERROR;
        }
        String message = ex.getReason() != null ? ex.getReason() : status.getReasonPhrase();
        return buildResponse(status, status.name(), message);
    }

    // === Lỗi logic nghiệp vụ (RuntimeException) ===
    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<Map<String, Object>> handleAccessDenied(AccessDeniedException ex) {
        return buildResponse(HttpStatus.FORBIDDEN, "Forbidden", ex.getMessage());
    }

    @ExceptionHandler(RuntimeException.class)
    public ResponseEntity<Map<String, Object>> handleRuntimeException(RuntimeException ex) {
        return buildResponse(HttpStatus.BAD_REQUEST, "Lỗi nghiệp vụ", ex.getMessage());
    }

    // === Lỗi trùng dữ liệu (UNIQUE constraint) ===
    @ExceptionHandler(DataIntegrityViolationException.class)
    public ResponseEntity<Map<String, Object>> handleDataIntegrity(DataIntegrityViolationException ex) {
        String detail = ex.getMostSpecificCause().getMessage();
        String friendlyMsg;

        if (detail.contains("Duplicate") || detail.contains("UNIQUE") || detail.contains("unique")) {

```
