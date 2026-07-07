# Knowledge Document: AiParseResult.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/AiParseResult.java",
  "language": "java",
  "module": "dto",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
 needsClarification) {
        this.needsClarification = needsClarification;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public List<Map<String, Object>> getTasks() {
        return tasks;
    }

    public void setTasks(List<Map<String, Object>> tasks) {
        this.tasks = tasks;
    }

    public String getPhase() {
        return phase;
    }

    public void setPhase(String phase) {
        this.phase = phase;
    }

    public String getMainGoal() {
        return mainGoal;
    }

    public void setMainGoal(String mainGoal) {
        this.mainGoal = mainGoal;
    }

    public String getContingency() {
        return contingency;
    }

    public void setContingency(String contingency) {
        this.contingency = contingency;
    }

    public List<String> getSuggestedQuestions() {
        return suggestedQuestions;
    }

    public void setSuggestedQuestions(List<String> suggestedQuestions) {
        this.suggestedQuestions = suggestedQuestions;
    }
}

```
