# Knowledge Document: SettingsPage.css (Chunk 5/5)

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
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```css
round: linear-gradient(135deg, #f0c27f, #e5b376);
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
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.theme-toggle-btn.dark .toggle-knob {
    left: 4px;
}

.theme-toggle-btn.light .toggle-knob {
    left: 30px;
}

body.theme-dark .settings-page {
    --settings-bg: #151617;
    --settings-card: #1f2223;
    --settings-border: rgba(255, 255, 255, 0.08);
    --settings-text: #f4eee8;
    --settings-muted: #aaa098;
    --settings-accent: #ffd7b7;
    --settings-soft: rgba(255, 184, 123, 0.16);
}

body.theme-dark .settings-card-top button,
body.theme-dark .settings-security-row > .material-symbols-outlined:first-child,
body.theme-dark .settings-device-list article {
    background: rgba(255, 255, 255, 0.05);
}

body.theme-dark .settings-plan-card {
    background: #3a2414;
}

@media (max-width: 980px) {
    .settings-account-layout,
    .settings-device-list {
        grid-template-columns: 1fr;
    }

    .settings-profile-card {
        min-height: 0;
    }
}

@media (max-width: 640px) {
    .settings-page {
        max-width: 100%;
    }

    .settings-card-top,
    .settings-theme-card,
    .settings-verification {
        align-items: flex-start;
        flex-direction: column;
    }

    .settings-info-grid {
        grid-template-columns: 1fr;
        gap: 24px;
    }

    .settings-profile-card,
    .settings-security-card,
    .settings-plan-card,
    .settings-device-card {
        padding: 22px;
    }
}

```
