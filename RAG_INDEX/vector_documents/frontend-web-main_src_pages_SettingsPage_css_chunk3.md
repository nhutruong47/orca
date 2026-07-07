# Knowledge Document: SettingsPage.css (Chunk 4/5)

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
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```css
een;
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

.settings-plan-meter progress::-webkit-progress-value {
    background: #f3c795;
}

.settings-plan-card button {
    width: 100%;
    min-height: 44px;
    border: 0;
    border-radius: 4px;
    background: #fffaf3;
    color: #3a2414;
    font-weight: 900;
    cursor: pointer;
}

.settings-device-card {
    margin-top: 26px;
    padding: 32px 38px;
}

.settings-device-card h2 {
    margin-top: 14px;
}

.settings-device-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
    margin-top: 24px;
}

.settings-device-list article {
    display: flex;
    align-items: center;
    gap: 12px;
    border: 1px solid var(--settings-border);
    border-radius: 8px;
    padding: 14px;
    background: #fbf7f1;
}

.settings-device-list .material-symbols-outlined {
    color: var(--settings-accent);
}

.settings-device-list strong,
.settings-device-list small {
    display: block;
}

.settings-device-list small,
.settings-theme-card p {
    margin-top: 4px;
    color: var(--settings-muted);
}

.settings-theme-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
}

/* Toggle Button */
.theme-toggle-btn {
    width: 56px;
    height: 30px;
    flex: 0 0 auto;
    border: none;
    border-radius: 15px;
    cursor: pointer;
    position: relative;
    transition: background 0.3s;
    display: flex;
    align-items: center;
    padding: 0 4px;
}

.theme-toggle-btn.dark {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
}

.theme-toggle-btn.light {
    background: linear-gradient(135deg, #f0c27f, #e5b376);
}

.toggle-icon {
    position: absolute;
    font-size: 0.7rem;
    z-index: 1;
}

.theme-toggle-btn.dark .toggle-icon {
    right: 8px;
}

.theme-toggle-btn.light .toggle-icon {
    left: 8px;
}

.toggle-knob {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: #fff;
    position: absolute;
    transition: left 0.3s ease;

```
