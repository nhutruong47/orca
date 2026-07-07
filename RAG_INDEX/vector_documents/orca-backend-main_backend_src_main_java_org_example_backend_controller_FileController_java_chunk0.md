# Knowledge Document: FileController.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/FileController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Controller",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.util.StringUtils;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/upload")
public class FileController {

    private final Path fileStorageLocation;

    public FileController() {
        this.fileStorageLocation = Paths.get("uploads").toAbsolutePath().normalize();
        try {
            Files.createDirectories(this.fileStorageLocation);
        } catch (Exception ex) {
            throw new RuntimeException("Could not create the directory where the uploaded files will be stored.", ex);
        }
    }

    @PostMapping
    public ResponseEntity<?> uploadFile(@RequestParam("file") MultipartFile file) {
        if (file.isEmpty()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Vui lòng chọn một file."));
        }

        try {
            // Normalize file name and generate unique ID to avoid overwriting
            String originalFileName = StringUtils.cleanPath(file.getOriginalFilename());
            if (originalFileName.contains("..")) {
                return ResponseEntity.badRequest().body(Map.of("error", "Tên file không hợp lệ."));
            }

            String fileExtension = "";
            int dotIndex = originalFileName.lastIndexOf(".");
            if (dotIndex > 0) {
                fileExtension = originalFileName.substring(dotIndex);
            }

            String fileName = UUID.randomUUID().toString() + fileExtension;

            // Copy file to the target location
            Path targetLocation = this.fileStorageLocation.resolve(fileName);
            Files.copy(file.getInputStream(), targetLocation, StandardCopyOption.REPLACE_EXISTING);

            // Generate full URL
            String fileDownloadUri = ServletUriComponentsBuilder.fromCurrentContextPath()
                    .path("/uploads/")
                    .path(fileName)
                    .toUriString();


```
