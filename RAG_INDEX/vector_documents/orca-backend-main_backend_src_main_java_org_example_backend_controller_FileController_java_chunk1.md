# Knowledge Document: FileController.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/FileController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
th targetLocation = this.fileStorageLocation.resolve(fileName);
            Files.copy(file.getInputStream(), targetLocation, StandardCopyOption.REPLACE_EXISTING);

            // Generate full URL
            String fileDownloadUri = ServletUriComponentsBuilder.fromCurrentContextPath()
                    .path("/uploads/")
                    .path(fileName)
                    .toUriString();

            return ResponseEntity.ok(Map.of(
                    "fileName", fileName,
                    "url", fileDownloadUri,
                    "type", file.getContentType(),
                    "size", file.getSize()
            ));
        } catch (IOException ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(Map.of("error", "Không thể lưu file. Vui lòng thử lại."));
        }
    }
}

```
