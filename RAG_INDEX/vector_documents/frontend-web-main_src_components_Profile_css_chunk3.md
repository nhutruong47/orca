# Knowledge Document: Profile.css (Chunk 4/4)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Profile.css",
  "language": "css",
  "module": "components",
  "business_domain": "security",
  "tags": [
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in components.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```css
title);
    font-size: 17px;
}

.profile-password-heading p {
    margin: 0;
    color: var(--shell-text-soft);
    font-size: 13px;
}

.profile-password-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
}

.profile-password-grid label {
    display: flex;
    flex-direction: column;
    gap: 7px;
    color: var(--shell-text-soft);
    font-size: 12px;
    font-weight: 700;
}

.profile-password-grid input {
    width: 100%;
    min-height: 44px;
    padding: 10px 12px;
    border: 1px solid var(--shell-border);
    border-radius: 8px;
    outline: none;
    background: var(--shell-surface);
    color: var(--shell-text);
}

.profile-password-grid input:focus {
    border-color: var(--shell-accent);
    box-shadow: 0 0 0 3px var(--shell-accent-soft);
}

.profile-password-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 18px;
}

.profile-password-actions button {
    min-width: 110px;
    min-height: 42px;
    padding: 10px 16px;
    border-radius: 8px;
    border: 1px solid var(--shell-border);
    font-weight: 700;
    cursor: pointer;
}

@media (max-width: 720px) {
    .profile-edit-grid,
    .profile-password-grid {
        grid-template-columns: 1fr;
    }

    .profile-security-actions,
    .profile-password-actions {
        flex-direction: column;
    }

    .profile-security-actions button,
    .profile-password-actions button {
        width: 100%;
    }
}

```
