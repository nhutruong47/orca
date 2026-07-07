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
