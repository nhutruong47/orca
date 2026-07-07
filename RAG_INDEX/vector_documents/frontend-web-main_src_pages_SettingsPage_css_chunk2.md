# Knowledge Document: SettingsPage.css (Chunk 3/5)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/SettingsPage.css",
  "language": "css",
  "module": "pages",
  "business_domain": "security",
  "tags": [
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```css
 padding: 28px;
}

.settings-side-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
}

.settings-side-head h2 {
    font-size: 21px;
}

.settings-side-head > span {
    color: var(--settings-accent);
    font-size: 19px;
}

.settings-security-row {
    width: 100%;
    display: grid;
    grid-template-columns: 34px minmax(0, 1fr) 18px;
    align-items: center;
    gap: 10px;
    border: 0;
    padding: 10px 0;
    background: transparent;
    color: var(--settings-text);
    text-align: left;
    cursor: pointer;
}

.settings-security-row > .material-symbols-outlined:first-child {
    width: 34px;
    height: 34px;
    display: grid;
    place-items: center;
    border-radius: 8px;
    background: #f3eee7;
    color: var(--settings-muted);
    font-size: 18px;
}

.settings-security-row strong,
.settings-security-row small {
    display: block;
}

.settings-security-row strong {
    font-size: 13px;
    font-weight: 900;
}

.settings-security-row small {
    margin-top: 3px;
    color: var(--settings-muted);
    font-size: 11px;
}

.settings-security-row:nth-of-type(2) small {
    color: #2fb565;
    font-weight: 900;
}

.settings-outline-btn {
    width: 100%;
    min-height: 42px;
    margin-top: 16px;
    border: 1px solid var(--settings-border);
    border-radius: 4px;
    background: transparent;
    color: var(--settings-text);
    font-weight: 900;
    cursor: pointer;
}

.settings-plan-card {
    background: #3a2414;
    color: #fff2e6;
}

.settings-plan-card > span {
    display: block;
    margin-bottom: 10px;
    color: rgba(255, 226, 198, 0.62);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 900;
    text-transform: uppercase;
}

.settings-plan-card h2 {
    color: #fff2e6;
    font-size: 24px;
    line-height: 1.1;
}

.settings-plan-meter {
    margin: 24px 0;
}

.settings-plan-meter div {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 8px;
    color: rgba(255, 242, 230, 0.8);
    font-size: 12px;
    font-weight: 800;
}

.settings-plan-meter progress {
    width: 100%;
    height: 5px;
    overflow: hidden;
    border: 0;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.2);
}

.settings-plan-meter progress::-webkit-progress-bar {
    background: rgba(255, 255, 255, 0.2);
}


```
