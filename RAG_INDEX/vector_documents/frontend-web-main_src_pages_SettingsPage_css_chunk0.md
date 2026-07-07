# Knowledge Document: SettingsPage.css (Chunk 1/5)

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
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```css
.settings-page {
    --settings-bg: #f7f3ed;
    --settings-card: #fffdf9;
    --settings-border: rgba(62, 42, 26, 0.1);
    --settings-text: #22170f;
    --settings-muted: #827165;
    --settings-accent: #3a2414;
    --settings-soft: #f7d9b8;
    max-width: 980px;
    margin: 0 auto;
    color: var(--settings-text);
}

.settings-hero {
    margin-bottom: 28px;
}

.settings-hero > span {
    display: block;
    margin-bottom: 22px;
    color: var(--settings-text);
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 18px;
    font-weight: 900;
}

.settings-hero h1 {
    margin: 0 0 8px;
    color: var(--settings-text);
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 900;
    letter-spacing: 0;
}

.settings-hero p {
    max-width: 560px;
    margin: 0;
    color: var(--settings-muted);
    line-height: 1.65;
}

.settings-account-layout {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 290px;
    gap: 22px;
    align-items: start;
}

.settings-profile-card,
.settings-security-card,
.settings-plan-card,
.settings-device-card {
    border: 1px solid var(--settings-border);
    border-radius: 8px;
    background: var(--settings-card);
    box-shadow: 0 18px 50px rgba(62, 42, 26, 0.06);
}

.settings-profile-card {
    min-height: 590px;
    padding: clamp(26px, 4vw, 38px);
}

.settings-card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-bottom: 14px;
}

.settings-pill {
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    padding: 6px 12px;
    background: var(--settings-accent);
    color: #ffe0bf;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.settings-card-top button {
    min-height: 34px;
    display: inline-flex;
    align-items: center;
    gap: 7px;
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

```
