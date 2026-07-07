# Knowledge Document: RAG_AUDIT.md (Chunk 4/10)

## Metadata
```json
{
  "file_path": "RAG_AUDIT.md",
  "language": "md",
  "module": "orca",
  "business_domain": "report",
  "tags": [
    "report",
    "payment",
    "factory",
    "production",
    "admin",
    "inventory",
    "security",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 3,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, production, admin, inventory, security, chat

## Source Code Chunk
```md
: string;               // Relevant text chunk
        relevanceScore: number;        // 0-1 similarity score
    }[];
    
    // Confidence and quality
    confidence: {
        score: number;                // 0-1 overall confidence
        level: 'high' | 'medium' | 'low';
        reasons: string[];             // Why confidence is this level
    };
    
    // Actions
    suggestedActions: {
        label: string;                 // Human-readable action
        type: 'create' | 'update' | 'navigate' | 'confirm';
        payload?: any;                // Action data
    }[];
    
    // Metadata
    metadata: {
        model: string;
        tokensUsed: number;
        processingTimeMs: number;
        timestamp: string;
    };
}
```

### 4.3 Hallucination Prevention

**Current:** No mechanism to prevent hallucination
**Required:** Explicit "I don't know" responses

```typescript
// Required response when knowledge not found:
{
    answer: "I cannot find verified information in the ORCA knowledge base.",
    reasoningSummary: "No documents matched the query with sufficient relevance.",
    referencedKnowledge: [],
    confidence: { score: 0, level: 'low', reasons: ["No matching knowledge found"] },
    suggestedActions: [
        { label: "Contact support", type: "navigate", payload: { path: "/support" } }
    ]
}
```

---

## 5. Inconsistencies Found

### 5.1 API Client Inconsistencies

```typescript
// aiService (V1) - groupService.ts line 225-228
export const aiService = {
    parseText: (text, teamId, history?) => ...  // Has history param but not used
};

// aiWorkflowService (V2) - groupService.ts line 256-263
export const aiWorkflowService = {
    extract: (teamId, text) => ...           // No history
    plan: (teamId, intent, fields) => ...    // No context
    revise: (teamId, instruction, draft) => ... // Only plan context
};
```

### 5.2 Response Schema Inconsistencies

| Service | Has Title | Has Tasks | Has Confidence | Has Sources |
|---------|-----------|-----------|---------------|------------|
| V1 parseText | ✅ | ✅ | ❌ | ⚠️ source field only |
| V2 extract | ❌ | ❌ | ✅ | ❌ |
| V2 plan | ❌ | ✅ | ❌ | ❌ |
| V2 revise | ❌ | ✅ | ❌ | ❌ |

### 5.3 Error Handling Inconsistencies

```typescript
// AiAssistantPanel.tsx line 90-101
catch (e: any) {
    if (isPaymentRequiredError(e)) {

```
