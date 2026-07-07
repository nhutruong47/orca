# Knowledge Document: App.css (Chunk 3/43)

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
  "chunk_index": 2,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
lute;
  left: 14px;
  font-size: 16px;
  z-index: 1;
  pointer-events: none;
}

.auth-form .form-input {
  width: 100%;
  padding: 14px 14px 14px 44px;
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: 12px;
  color: var(--text-primary);
  font-size: 15px;
  font-family: var(--font);
  transition: all 0.3s;
  outline: none;
}

.auth-form .form-input::placeholder {
  color: var(--text-muted);
}

.auth-form .form-input:focus {
  background: var(--bg-input);
  border-color: var(--border-focus);
  box-shadow: 0 0 0 4px rgba(212, 165, 116, 0.1);
}

.auth-form .input-container:focus-within .input-icon {
  color: #d4a574;
}

.password-input {
  padding-right: 50px !important;
}

.password-toggle-btn {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 34px;
  height: 34px;
  border: 1px solid transparent;
  border-radius: 8px;
  background: transparent;
  color: rgba(255, 238, 214, 0.78);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 18px;
  transition: background 0.18s ease, border-color 0.18s ease, color 0.18s ease;
}

.password-toggle-btn:hover,
.password-toggle-btn:focus-visible {
  background: rgba(212, 165, 116, 0.14);
  border-color: rgba(212, 165, 116, 0.28);
  color: #f5c58b;
  outline: none;
}

.remember-row {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  width: fit-content;
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  user-select: none;
}

.remember-row input {
  appearance: none;
  width: 18px;
  height: 18px;
  margin: 0;
  border-radius: 5px;
  border: 1px solid rgba(212, 165, 116, 0.5);
  background: rgba(255, 255, 255, 0.04);
  display: grid;
  place-items: center;
  cursor: pointer;
}

.remember-row input::after {
  content: "";
  width: 8px;
  height: 5px;
  border-left: 2px solid #20140c;
  border-bottom: 2px solid #20140c;
  transform: rotate(-45deg) scale(0);
  transition: transform 0.14s ease;
}

.remember-row input:checked {
  background: linear-gradient(135deg, #d8a66f, #a87540);
  border-color: #d8a66f;
}

.remember-row input:checked::after {
  transform: rotate(-45deg) scale(1);
}

.form-input {
  width: 100%;
  padding: clamp(11px, 2vw, 14px) clamp(11px, 2vw, 14px) clamp(11px, 2vw, 14px) clamp(38px, 8vw, 44px);
  background: var(--bg-input);

```
