# Knowledge Document: PROMPT_STANDARDIZATION.md (Chunk 1/7)

## Metadata
```json
{
  "file_path": "PROMPT_STANDARDIZATION.md",
  "language": "md",
  "module": "orca",
  "business_domain": "factory",
  "tags": [
    "factory",
    "analytics",
    "production",
    "security",
    "admin",
    "inventory",
    "employee"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, analytics, production, security, admin, inventory, employee

## Source Code Chunk
```md
# ORCA Platform - Prompt Standardization

**Date:** July 7, 2026
**Status:** READY FOR IMPLEMENTATION

---

## Overview

This document defines the unified Prompt Framework for all AI features in the ORCA platform.

---

## 1. Prompt Framework Architecture

### 1.1 Prompt Components

Every AI prompt consists of:

1. **System Prompt** - Base instructions for the AI role
2. **Developer Prompt** - Technical constraints and rules
3. **User Prompt** - Dynamic user query
4. **Context Builder** - Retrieved knowledge and conversation
5. **Safety Rules** - Content guidelines
6. **Output Formatter** - Expected response structure

### 1.2 Prompt Hierarchy

```
┌─────────────────────────────────────────────────────────┐
│                    SYSTEM PROMPT                         │
│  (Base role, identity, capabilities)                    │
├─────────────────────────────────────────────────────────┤
│                  DEVELOPER PROMPT                         │
│  (Technical rules, constraints, format)                │
├─────────────────────────────────────────────────────────┤
│                   USER PROMPT                             │
│  (Dynamic query from user)                               │
├─────────────────────────────────────────────────────────┤
│                  CONTEXT BUILDER                         │
│  (Retrieved knowledge, conversation history)            │
├─────────────────────────────────────────────────────────┤
│                   SAFETY RULES                           │
│  (Content guidelines, restrictions)                      │
├─────────────────────────────────────────────────────────┤
│                 OUTPUT FORMATTER                         │
│  (Expected response structure)                           │
└─────────────────────────────────────────────────────────┘
```

---

## 2. System Prompts

### 2.1 Base AI Assistant System Prompt

```python
SYSTEM_PROMPT_AI_ASSISTANT = """
You are ORCA AI Assistant, an expert helper for the ORCA Coffee Factory ERP platform.

IDENTITY:
- You are a helpful, knowledgeable assistant integrated into the ORCA production management system
- You help factory managers, supervisors, and workers manage daily operations
- You speak Vietnamese naturally and professionally
- You understand coffee production processes, inventory management, and team coordination

CAPABILITIES:

```
