# Knowledge Document: TESTING_CHECKLIST.md (Chunk 2/5)

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
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, production, dashboard

## Source Code Chunk
```md
1.4 Theme Flash Prevention

| Test | Expected Result | Status |
|------|----------------|--------|
| Initial page load | No flash of wrong theme | ☐ |
| Hard refresh (Ctrl+F5) | No flash | ☐ |
| Direct URL navigation | No flash | ☐ |

### 1.5 Theme Toggle

| Test | Action | Expected Result | Status |
|------|--------|----------------|--------|
| Dark → Light | Toggle button | Instant switch | ☐ |
| Light → System | Toggle button | System theme applied | ☐ |
| System → Dark | Toggle button | Dark theme applied | ☐ |
| Theme persisted | Close browser | Theme saved in localStorage | ☐ |

### 1.6 Component Testing

#### Buttons
| Test | State | Expected | Status |
|------|-------|----------|--------|
| Primary button | Default (dark) | `var(--brand)` bg, white text | ☐ |
| Primary button | Hover | Slight lift, darker shade | ☐ |
| Primary button | Active | Pressed effect | ☐ |
| Primary button | Light mode | Darker brand, white text | ☐ |
| Danger button | Dark mode | Red bg, white text | ☐ |
| Danger button | Light mode | Darker red, white text | ☐ |

#### Cards
| Test | Expected | Status |
|------|----------|--------|
| Card hover effect | Lift + shadow increase | ☐ |
| Card border | Subtle border visible | ☐ |
| Elevated card | Higher contrast | ☐ |

#### Status Badges
| Test | Expected | Status |
|------|----------|--------|
| Success badge | Green soft bg, dark green text | ☐ |
| Warning badge | Yellow soft bg, dark yellow text | ☐ |
| Danger badge | Red soft bg, dark red text | ☐ |
| Light mode badges | Adjusted for light bg | ☐ |

#### Forms
| Test | Expected | Status |
|------|----------|--------|
| Input focus | Brand color ring | ☐ |
| Input focus | Light mode ring | ☐ |
| Input disabled | Reduced opacity | ☐ |
| Select dropdown | Native dropdown | ☐ |

---

## 2. RAG System Testing

### 2.1 Knowledge Indexing

| Test | Expected Result | Status |
|------|----------------|--------|
| Index single document | Vector stored | ☐ |
| Index batch documents | All vectors stored | ☐ |
| Delete document | Vector removed | ☐ |
| Reindex source | Old vectors replaced | ☐ |

### 2.2 Retrieval

| Test | Query | Expected Result | Status |
|------|-------|----------------|--------|
| Exact match | Known product name | Relevant doc returned | ☐ |
| Semantic match | Synonym query | Relevant doc returned | ☐ |
| No match | Unknown topic | Empty results | ☐ |

```
