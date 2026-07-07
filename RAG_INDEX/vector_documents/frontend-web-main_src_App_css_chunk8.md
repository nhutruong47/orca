# Knowledge Document: App.css (Chunk 9/43)

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
  "chunk_index": 8,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.login-btn-primary:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(139, 94, 60, 0.4);
}

.login-btn-primary:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.login-btn-primary:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.login-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid #fff;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

/* Divider */
.login-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 18px 0;
}

.login-divider::before,
.login-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}

.login-divider span {
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 500;
}

/* Google Button */
.login-btn-google {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 12px;
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: 10px;
  color: rgba(255, 255, 255, 0.8);
  font-size: 14px;
  font-weight: 500;
  font-family: var(--font);
  cursor: pointer;
  transition: all 0.2s;
}

.login-btn-google:hover {
  background: var(--bg-input);
  border-color: var(--border-focus);
  transform: translateY(-1px);
}

/* Demo Accounts */
.login-demo {
  margin-top: 20px;
  padding: 14px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 12px;
}

.login-demo-label {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.4);
  margin-bottom: 10px;
  font-weight: 500;
}

.login-demo-accounts {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}

.login-demo-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 10px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  font-family: var(--font);
}

.login-demo-btn:hover {
  background: rgba(212, 165, 116, 0.1);
  border-color: rgba(212, 165, 116, 0.2);
}

.login-demo-btn .demo-user {
  font-size: 13px;
  font-weight: 600;
  color: #fff;
}

.login-demo-btn .demo-role {
  font-size: 10px;
  color: rgba(255, 255, 255, 0.4);
  margin-left: auto;
}

/* Login Footer */
.login-footer {

```
