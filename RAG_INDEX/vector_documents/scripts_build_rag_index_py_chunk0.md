# Knowledge Document: build_rag_index.py (Chunk 1/3)

## Metadata
```json
{
  "file_path": "scripts/build_rag_index.py",
  "language": "py",
  "module": "scripts",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "admin",
    "attendance",
    "inventory",
    "authentication",
    "payment",
    "subscription",
    "analytics",
    "dashboard",
    "workspace",
    "chat",
    "production",
    "security",
    "notification",
    "booking",
    "warehouse",
    "employee",
    "authorization"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in scripts.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, admin, attendance, inventory, authentication, payment, subscription, analytics, dashboard, workspace, chat, production, security, notification, booking, warehouse, employee, authorization

## Source Code Chunk
```py
import os
import re
import json
import ast
import uuid
from pathlib import Path

# Config
REPO_ROOT = Path("D:/tichhop/orcaV2/orca")
RAG_INDEX_DIR = REPO_ROOT / "RAG_INDEX"
VECTOR_DOCS_DIR = RAG_INDEX_DIR / "vector_documents"

# File types to scan
EXTENSIONS = {'.java', '.tsx', '.ts', '.js', '.jsx', '.py', '.sql', '.html', '.css', '.yml', '.yaml', '.json', '.properties', '.xml', '.md'}

# Business Tags dictionary for mapping folder/filenames to semantic tags
TAG_KEYWORDS = ['inventory', 'attendance', 'booking', 'payment', 'security', 'authentication', 'authorization', 'admin', 'production', 'warehouse', 'employee', 'factory', 'workspace', 'chat', 'notification', 'subscription', 'report', 'dashboard', 'analytics']

def extract_tags(content, filepath):
    content_lower = content.lower()
    path_lower = str(filepath).lower()
    tags = set()
    for keyword in TAG_KEYWORDS:
        if keyword in content_lower or keyword in path_lower:
            tags.add(keyword)
    return list(tags)

def chunk_text(text, max_tokens=600, overlap=100):
    # Very rough character-based chunking assuming ~4 chars per token
    chunk_size_chars = max_tokens * 4
    overlap_chars = overlap * 4
    
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size_chars, len(text))
        
        # Try to break at a newline if possible
        if end < len(text):
            newline_pos = text.rfind('\n', start, end)
            if newline_pos != -1 and newline_pos > start + (chunk_size_chars // 2):
                end = newline_pos + 1
                
        chunks.append(text[start:end])
        start = end - overlap_chars
        if start < 0:
            break
        if end == len(text):
            break
    return chunks

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {filepath}: {e}")
        return

    ext = filepath.suffix.lower()
    relative_path = filepath.relative_to(REPO_ROOT)
    module = filepath.parent.name
    tags = extract_tags(content, relative_path)
    
    # Generate chunks
    chunks = chunk_text(content)
    
    for i, chunk_text_content in enumerate(chunks):
        doc_id = str(uuid.uuid4())
        
        # Determine logical type
        logical_type = "Generic"

```
