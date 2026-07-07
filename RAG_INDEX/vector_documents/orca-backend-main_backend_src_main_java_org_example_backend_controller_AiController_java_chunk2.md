# Knowledge Document: AiController.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/AiController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "inventory",
  "tags": [
    "inventory",
    "payment",
    "authentication",
    "security",
    "authorization"
  ],
  "logical_type": "Controller",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, authentication, security, authorization

## Source Code Chunk
```java
name();
                List<String> labels = tm.getJobLabels();
                sb.append("- ").append(name);
                if (labels != null && !labels.isEmpty()) {
                    sb.append(" (Nhãn: ").append(String.join(", ", labels)).append(")");
                } else {
                    sb.append(" (Chưa gán nhãn)");
                }
                sb.append("\n");
            }
            memberContext = sb.toString();
        }
        String history = payload.get("history");
        AiParseResult result = aiServiceClient.parseTask(text, teamId, memberContext, history);
        return ResponseEntity.ok(result);
    }
}


```
