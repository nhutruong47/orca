# Knowledge Document: SettingsPage.css (Chunk 2/5)

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
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```css
ap: 7px;
    border: 0;
    border-radius: 10px;
    padding: 0 16px;
    background: var(--settings-soft);
    color: #8b5a2b;
    font-weight: 800;
    cursor: pointer;
}

.settings-card-top .material-symbols-outlined {
    font-size: 17px;
}

.settings-profile-card h2,
.settings-security-card h2,
.settings-plan-card h2,
.settings-device-card h2 {
    margin: 0;
    color: var(--settings-text);
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 24px;
    font-weight: 900;
}

.settings-info-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 34px 44px;
    margin-top: 34px;
    padding-bottom: 34px;
    border-bottom: 1px solid var(--settings-border);
}

.settings-info-grid span {
    display: block;
    margin-bottom: 8px;
    color: #c0b3a9;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.settings-info-grid strong {
    display: block;
    max-width: 210px;
    color: var(--settings-text);
    font-size: 15px;
    line-height: 1.45;
    overflow-wrap: anywhere;
}

.settings-dot-role::before {
    content: '';
    display: inline-block;
    width: 6px;
    height: 6px;
    margin-right: 7px;
    border-radius: 50%;
    background: var(--settings-accent);
    vertical-align: 2px;
}

.settings-verification {
    display: flex;
    align-items: center;
    gap: 18px;
    margin-top: 30px;
}

.settings-verification img {
    width: 72px;
    height: 72px;
    flex: 0 0 auto;
    border-radius: 4px;
    object-fit: cover;
}

.settings-verification h3 {
    margin: 0 0 6px;
    color: var(--settings-text);
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 22px;
}

.settings-verification p {
    max-width: 420px;
    margin: 0;
    color: var(--settings-muted);
    line-height: 1.5;
}

.settings-side-stack {
    display: grid;
    gap: 22px;
}

.settings-security-card,
.settings-plan-card {
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

```
