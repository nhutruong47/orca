# Knowledge Document: prompt_builder.py (Chunk 4/5)

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
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production

## Source Code Chunk
```py
".join(parts) if len(parts) > 1 else ""
    
    def build_extraction_prompt(
        self,
        query: str,
        team_members: Optional[List[Dict[str, Any]]] = None
    ) -> str:
        """
        Build prompt for intent extraction.
        
        Args:
            query: User query to extract from
            team_members: Available team members for assignment suggestions
            
        Returns:
            Extraction prompt
        """
        members_context = ""
        if team_members:
            members_json = "\n".join([
                f"- {m.get('fullName', m.get('username', 'Unknown'))}: {', '.join(m.get('jobLabels', [])) or 'No specializations'}"
                for m in team_members
            ])
            members_context = f"""
AVAILABLE TEAM MEMBERS:
{members_json}
"""
        
        return f"""You are ORCA AI v2 extract module for a Vietnamese workshop/task management app.

Your only job is to classify the user request and extract structured fields.
Do not create tasks. Do not save data. Do not explain.

{members_context}

Now extract this user request:
{query}
"""
    
    def build_planning_prompt(
        self,
        intent: str,
        fields: Dict[str, Any],
        team_members: List[Dict[str, Any]]
    ) -> str:
        """
        Build prompt for task planning.
        
        Args:
            intent: Classified intent (PRODUCTION_PLAN, OPERATION_TASK)
            fields: Extracted fields
            team_members: Available team members
            
        Returns:
            Planning prompt
        """
        import json
        
        fields_json = json.dumps(fields, ensure_ascii=False, indent=2)
        members_json = json.dumps(team_members, ensure_ascii=False, indent=2)
        
        task_count = "3 to 6 tasks" if intent == "PRODUCTION_PLAN" else "2 to 4 tasks"
        
        return f"""You are ORCA AI v2 plan module for a Vietnamese workshop/task management app.

Your only job is to convert extracted structured fields into a draft Goal and draft Tasks.
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
    

```
