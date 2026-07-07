# Knowledge Document: VideoCallController.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/VideoCallController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Controller",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.VideoCallSignalDTO;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Controller;

@Controller
public class VideoCallController {

    private final SimpMessagingTemplate messagingTemplate;

    public VideoCallController(SimpMessagingTemplate messagingTemplate) {
        this.messagingTemplate = messagingTemplate;
    }

    @MessageMapping("/call.signal")
    public void relaySignal(VideoCallSignalDTO signal) {
        if (signal == null
                || isBlank(signal.getTeamId())
                || isBlank(signal.getSenderId())
                || isBlank(signal.getRecipientId())
                || isBlank(signal.getType())
                || isBlank(signal.getCallId())) {
            return;
        }

        messagingTemplate.convertAndSend(
                "/topic/call/team/" + signal.getTeamId() + "/user/" + signal.getRecipientId(),
                signal
        );
    }

    private boolean isBlank(String value) {
        return value == null || value.isBlank();
    }
}

```
