# Knowledge Document: prompt_builder.py (Chunk 5/5)

## Metadata
```json
{
  "file_path": "ai-service/app/rag/prompt_builder.py",
  "language": "py",
  "module": "rag",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production

## Source Code Chunk
```py
d structured fields into a draft Goal and draft Tasks.
Do not classify intent. Do not ask questions. Do not save data. Do not explain.

Intent: {intent}

Extracted fields:
{fields_json}

Team members available for suggested assignment:
{members_json}

Output format: JSON with goalTitle, outputTarget, deadline, priority, and tasks array.
Return {task_count}.

Keep the draft in Vietnamese.
"""
    
    def build_revision_prompt(
        self,
        instruction: str,
        current_draft: Dict[str, Any],
        team_members: List[Dict[str, Any]]
    ) -> str:
        """
        Build prompt for plan revision.
        
        Args:
            instruction: User revision instruction
            current_draft: Current plan draft to revise
            team_members: Available team members
            
        Returns:
            Revision prompt
        """
        import json
        
        draft_json = json.dumps(current_draft, ensure_ascii=False, indent=2)
        members_json = json.dumps(team_members, ensure_ascii=False, indent=2)
        
        return f"""You are ORCA AI v2 revise module for a Vietnamese workshop/task management app.

Your only job is to revise an existing draft Goal/Tasks according to the user's revision instruction.
Do not classify intent. Do not create a new plan from scratch. Do not save data. Do not explain.

User revision instruction:
{instruction}

Current draft:
{draft_json}

Team members available for suggested assignment:
{members_json}

Only change what was requested. Preserve other fields.
Keep the draft in Vietnamese.
"""

```
