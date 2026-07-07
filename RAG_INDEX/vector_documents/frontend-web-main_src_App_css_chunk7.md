# Knowledge Document: App.css (Chunk 8/43)

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
  "chunk_index": 7,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
w, 40px);
  background: var(--bg-secondary);
  border-left: 1px solid var(--border);
  overflow-y: auto;
  max-height: 100vh;
}

.login-form-container {
  width: 100%;
  max-width: 400px;
  animation: fadeInRight 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeInRight {
  from {
    opacity: 0;
    transform: translateX(20px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.login-form-header {
  margin-bottom: 28px;
}

.login-logo-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}

.login-input-wrap {
  position: relative;
  display: flex;
  align-items: center;
}

.login-input-icon {
  position: absolute;
  left: 14px;
  color: var(--text-muted);
  pointer-events: none;
}

.login-split .login-input-wrap input {
  width: 100%;
  padding: 13px 16px 13px 44px;
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: 10px;
  color: var(--text-primary);
  font-size: 15px;
  font-family: var(--font);
  transition: all 0.2s;
  outline: none;
}

.login-split .login-input-wrap input::placeholder {
  color: var(--text-muted);
}

.login-split .login-input-wrap input:focus {
  border-color: #d4a574;
  background: var(--bg-input);
  box-shadow: 0 0 0 3px rgba(212, 165, 116, 0.1);
  color: var(--text-primary);
}

.login-error {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.25);
  border-radius: 8px;
  color: #fca5a5;
  font-size: 13px;
  animation: shake 0.4s ease-in-out;
}

.login-error svg {
  flex-shrink: 0;
  color: #ef4444;
}

.login-btn-primary {
  width: 100%;
  padding: 13px;
  background: linear-gradient(135deg, #d4a574, #8b5e3c);
  border: none;
  border-radius: 10px;
  color: #fff;
  /* Buttons usually have light text regardless of theme */
  font-size: 15px;
  font-weight: 600;
  font-family: var(--font);
  cursor: pointer;
  transition: all 0.3s;
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

```
