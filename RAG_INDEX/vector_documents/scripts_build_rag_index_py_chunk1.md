# Knowledge Document: build_rag_index.py (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in scripts.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, admin, attendance, inventory, authentication, payment, subscription, analytics, dashboard, workspace, chat, production, security, notification, booking, warehouse, employee, authorization

## Source Code Chunk
```py
urn

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
        if "Controller" in str(filepath): logical_type = "Controller"
        elif "Service" in str(filepath): logical_type = "Service"
        elif "Repository" in str(filepath): logical_type = "Repository"
        elif "Entity" in str(filepath) or "Model" in str(filepath): logical_type = "Entity"
        elif "DTO" in str(filepath): logical_type = "DTO"
        elif ext in ['.tsx', '.jsx']: logical_type = "Component/Page"
        
        metadata = {
            "file_path": str(relative_path).replace("\\", "/"),
            "language": ext[1:],
            "module": module,
            "business_domain": "Core" if not tags else tags[0],
            "tags": tags,
            "logical_type": logical_type,
            "chunk_index": i,
            "total_chunks": len(chunks)
        }
        
        # Markdown layout
        md_content = f"# Knowledge Document: {filepath.name} (Chunk {i+1}/{len(chunks)})\n\n"
        md_content += "## Metadata\n"
        md_content += "```json\n"
        md_content += json.dumps(metadata, indent=2) + "\n"
        md_content += "```\n\n"
        md_content += "## Semantic Context\n"
        md_content += f"- **Purpose**: Implementation chunk of {logical_type} in {module}.\n"
        md_content += f"- **Dependencies**: Refer to module imports.\n"
        md_content += f"- **Tags**: {', '.join(tags)}\n\n"
        md_content += "## Source Code Chunk\n"
        md_content += f"```{ext[1:]}\n"
        md_content += chunk_text_content
        md_content += "\n```\n"
        
        # Save to RAG_INDEX/vector_documents
        safe_name = str(relative_path).replace("\\", "_").replace("/", "_").replace(".", "_")
        out_filename = VECTOR_DOCS_DIR / f"{safe_name}_chunk{i}.md"
        
        with open(out_filename, 'w', encoding='utf-8') as out_f:
            out_f.write(md_content)

def build_index():
    print("Starting ORCA Knowledge Base Indexing...")
    count = 0
    for root, dirs, files in os.walk(REPO_ROOT):

```
