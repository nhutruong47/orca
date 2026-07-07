# Knowledge Document: build_rag_index.py (Chunk 3/3)

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
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in scripts.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, admin, attendance, inventory, authentication, payment, subscription, analytics, dashboard, workspace, chat, production, security, notification, booking, warehouse, employee, authorization

## Source Code Chunk
```py
afe_name = str(relative_path).replace("\\", "_").replace("/", "_").replace(".", "_")
        out_filename = VECTOR_DOCS_DIR / f"{safe_name}_chunk{i}.md"
        
        with open(out_filename, 'w', encoding='utf-8') as out_f:
            out_f.write(md_content)

def build_index():
    print("Starting ORCA Knowledge Base Indexing...")
    count = 0
    for root, dirs, files in os.walk(REPO_ROOT):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'target', 'build', '__pycache__', 'RAG_INDEX', 'dist', 'uploads', 'logs', '.vite']]
        
        for file in files:
            filepath = Path(root) / file
            if filepath.suffix.lower() in EXTENSIONS:
                process_file(filepath)
                count += 1
                if count % 100 == 0:
                    print(f"Processed {count} files...")
    print(f"Indexing complete! Processed {count} files.")

if __name__ == '__main__':
    build_index()

```
