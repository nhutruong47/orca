# Knowledge Document: TESTING_CHECKLIST.md (Chunk 3/5)

## Metadata
```json
{
  "file_path": "TESTING_CHECKLIST.md",
  "language": "md",
  "module": "orca",
  "business_domain": "admin",
  "tags": [
    "admin",
    "inventory",
    "production",
    "dashboard"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, production, dashboard

## Source Code Chunk
```md
s | All vectors stored | ☐ |
| Delete document | Vector removed | ☐ |
| Reindex source | Old vectors replaced | ☐ |

### 2.2 Retrieval

| Test | Query | Expected Result | Status |
|------|-------|----------------|--------|
| Exact match | Known product name | Relevant doc returned | ☐ |
| Semantic match | Synonym query | Relevant doc returned | ☐ |
| No match | Unknown topic | Empty results | ☐ |
| Source filter | Filter by inventory | Only inventory docs | ☐ |

### 2.3 Response Format

| Test | Field | Expected | Status |
|------|-------|----------|--------|
| Answer field | Response | Non-empty string | ☐ |
| Reasoning summary | Analysis | Non-empty string | ☐ |
| Confidence score | 0-1 | Valid number | ☐ |
| Confidence level | high/medium/low | Valid enum | ☐ |
| Sources | Citations | Array with relevance | ☐ |
| Suggestions | Actions | Array with type | ☐ |

### 2.4 Hallucination Prevention

| Test | Input | Expected Result | Status |
|------|-------|----------------|--------|
| Unknown query | Random nonsense | Low confidence | ☐ |
| Out of domain | Politics, sports | "Cannot find" response | ☐ |
| Partial match | Vague query | Partial answer | ☐ |

### 2.5 Prompt Injection Prevention

| Test | Input | Expected Result | Status |
|------|-------|----------------|--------|
| Injection attempt | "Ignore instructions..." | Filtered/rejected | ☐ |
| Code injection | "```system" | Filtered | ☐ |
| Role play | "You are now..." | Filtered | ☐ |

---

## 3. Page-by-Page Testing

### 3.1 Core Pages

| Page | Dark Mode | Light Mode | Charts | Theme Toggle |
|------|----------|-----------|--------|-------------|
| Dashboard | ☐ | ☐ | ☐ | ☐ |
| Group Detail | ☐ | ☐ | ☐ | ☐ |
| Inventory | ☐ | ☐ | ☐ | ☐ |
| Production Orders | ☐ | ☐ | ☐ | ☐ |
| Settings | ☐ | ☐ | ☐ | ☐ |
| Admin | ☐ | ☐ | ☐ | ☐ |
| Profile | ☐ | ☐ | ☐ | ☐ |

### 3.2 AI Features

| Feature | Dark Mode | Light Mode | Citations | Confidence |
|---------|-----------|-----------|-----------|------------|
| AI Assistant Panel | ☐ | ☐ | ☐ | ☐ |
| AI Plan Generation | ☐ | ☐ | ☐ | ☐ |
| AI Task Suggestions | ☐ | ☐ | ☐ | ☐ |

### 3.3 Responsive Testing

| Breakpoint | Width | Sidebar | Content | Status |
|------------|-------|---------|---------|--------|
| Mobile | < 480px | Hidden | Full width | ☐ |
| Tablet | < 768px | Hidden | Adjusted | ☐ |
| Desktop | < 1024px | Collapsed | Normal | ☐ |

```
