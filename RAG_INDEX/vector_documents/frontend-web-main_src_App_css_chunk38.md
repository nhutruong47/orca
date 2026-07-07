# Knowledge Document: App.css (Chunk 39/43)

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
  "chunk_index": 38,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
ll:active {
  color: #fffaf2 !important;
  -webkit-text-fill-color: #fffaf2 !important;
  -webkit-box-shadow: 0 0 0px 1000px #1c1d21 inset !important;
  transition: background-color 5000s ease-in-out 0s;
}

.login-split .login-link {
  color: #fffaf2 !important;
  font-weight: 800;
}

.login-split .login-link:hover {
  color: #ffffff !important;
}

.login-split .login-hero-overlay {
  background:
    linear-gradient(90deg, rgba(7, 10, 18, 0.78) 0%, rgba(7, 10, 18, 0.56) 48%, rgba(7, 10, 18, 0.28) 100%),
    linear-gradient(180deg, rgba(7, 10, 18, 0.04) 0%, rgba(7, 10, 18, 0.58) 100%);
}

@media (max-width: 1200px) {
  .login-split {
    grid-template-columns: minmax(0, 1fr);
  }

  .login-hero {
    min-height: 58vh;
  }

  .login-form-side {
    min-height: auto;
  }
}

@media (max-width: 760px) {
  .login-hero {
    display: flex;
    min-height: auto;
    padding: 30px 18px;
  }

  .login-brands-list {
    grid-template-columns: 1fr;
  }

  .login-hero-stats {
    flex-wrap: wrap;
  }

  .login-form-side {
    padding: 18px;
  }

  .login-form-container {
    max-width: none;
    padding: 22px;
  }

  .login-demo-accounts {
    grid-template-columns: 1fr;
  }

}

/* ============================================
   NOTIFICATIONS
   ============================================ */
.topbar-notification {
  position: relative;
  display: flex;
  align-items: center;
}

.notification-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-primary);
  cursor: pointer;
  position: relative;
  transition: var(--transition);
}

.notification-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: scale(1.05);
}

.notification-badge {
  position: absolute;
  top: -4px;
  right: -4px;
  background: var(--danger, #f85149);
  color: white;
  font-size: 10px;
  font-weight: 700;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid var(--bg-card);
}

.notification-dropdown {
  position: absolute;
  top: 48px;
  right: -10px;
  width: 320px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  z-index: 100;
  overflow: hidden;

```
