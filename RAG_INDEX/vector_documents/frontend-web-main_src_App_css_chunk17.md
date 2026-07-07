# Knowledge Document: App.css (Chunk 18/43)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/App.css",
  "language": "css",
  "module": "src",
  "business_domain": "dashboard",
  "tags": [
    "dashboard",
    "admin",
    "inventory",
    "security",
    "notification"
  ],
  "logical_type": "Generic",
  "chunk_index": 17,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
splay: flex;
  align-items: center;
  gap: 16px;
  padding: 18px 20px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  transition: var(--transition);
}

.profile-field:hover {
  background: var(--bg-card-hover);
}

.field-icon {
  font-size: 22px;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(212, 165, 116, 0.1);
  border-radius: var(--radius-sm);
  flex-shrink: 0;
}

.field-content {
  display: flex;
  flex-direction: column;
}

.field-label {
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.field-value {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
  margin-top: 2px;
}

/* Security Section */
.security-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.security-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 20px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
}

.security-icon {
  font-size: 20px;
}

.security-label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
}

.security-value {
  display: block;
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 2px;
}

/* ============================================
   RESPONSIVE - COMPREHENSIVE BREAKPOINTS
   ============================================ */

/* Ultra Wide (1920px+) */
@media (min-width: 1920px) {
  .layout-content {
    padding: 40px 48px;
  }

  .page-header {
    margin-bottom: 36px;
  }

  .page-title {
    font-size: 32px;
  }

  .section-title {
    font-size: 20px;
  }
}

/* Desktop Large (1440px - 1919px) */
@media (max-width: 1919px) and (min-width: 1440px) {
  .layout-content {
    padding: 32px 40px;
  }

  .page-title {
    font-size: 30px;
  }

  .section-title {
    font-size: 18px;
  }
}

/* Desktop Medium (1024px - 1439px) */
@media (max-width: 1439px) and (min-width: 1024px) {
  .layout-content {
    padding: 28px 32px;
  }

  .page-title {
    font-size: 26px;
  }

  .section-title {
    font-size: 16px;
  }

  .stats-grid {
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 14px;
  }

  .actions-grid {
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 12px;
  }
}


```
