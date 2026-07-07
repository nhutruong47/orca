# Knowledge Document: README.md (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/ai-service/README.md",
  "language": "md",
  "module": "ai-service",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in ai-service.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```md
nstructions.

Mock mode is still available for local integration checks when Gemini key, quota, model, or network is unstable.

## Phase 3 Plan Acceptance Test

Before implementing Gemini for `/plan`, use this script as the acceptance target:

```powershell
F:\code\InSchool\Semester8\EXE201\Ver2\ai-service\.venv\Scripts\python.exe F:\code\InSchool\Semester8\EXE201\Ver2\test_ai_v2_plan_api.py
```

The script calls Spring Boot, not Python directly, so it also verifies that Spring can load team members and job labels before forwarding the request to the AI service.

Expected before Phase 3 implementation:

```text
Some tests can fail because /plan is still mock.
```

Expected after Phase 3 implementation:

```text
All Gemini plan acceptance tests pass.
```

## Phase 4 Revise Acceptance Test

Use this script to verify `/revise` through Spring Boot:

```powershell
F:\code\InSchool\Semester8\EXE201\Ver2\ai-service\.venv\Scripts\python.exe F:\code\InSchool\Semester8\EXE201\Ver2\test_ai_v2_revise_api.py
```

The script does not call `/extract` or `/plan`; it sends a fixed draft to `/revise` so it can test revision behavior with fewer Gemini calls.

```
