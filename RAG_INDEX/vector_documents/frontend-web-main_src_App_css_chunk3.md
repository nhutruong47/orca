# Knowledge Document: App.css (Chunk 4/43)

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
  "chunk_index": 3,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
0);
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
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  color: var(--text-primary);
  font-size: clamp(13px, 2.5vw, 15px);
  font-family: var(--font);
  transition: var(--transition);
  outline: none;
}

.form-input::placeholder {
  color: var(--text-muted);
}

.form-input:focus {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(212, 165, 116, 0.1);
}

.order-team-select {
  color-scheme: dark;
  min-width: 72px;
  background: linear-gradient(180deg, rgba(43, 32, 24, 0.98), rgba(28, 21, 16, 0.98)) !important;
  border-color: rgba(201, 140, 78, 0.48) !important;
  color: #f6dcc0 !important;
  box-shadow: inset 0 0 0 1px rgba(255, 214, 164, 0.05), 0 10px 26px rgba(0, 0, 0, 0.22);
}

.order-team-select:hover,
.order-team-select:focus {
  border-color: rgba(224, 166, 99, 0.76) !important;
  box-shadow: 0 0 0 3px rgba(201, 140, 78, 0.16), 0 10px 26px rgba(0, 0, 0, 0.28) !important;
}

.order-team-select option {
  background: #211813;
  color: #f6dcc0;
}

.order-team-select option:checked {
  background: #a8743f;
  color: #fff5e8;
}

.form-error {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: var(--radius-sm);
  color: #fca5a5;
  font-size: 14px;
  animation: shake 0.4s ease-in-out;
}

@keyframes shake {

  0%,
  100% {
    transform: translateX(0);
  }

  25% {
    transform: translateX(-5px);
  }

  75% {
    transform: translateX(5px);
  }
}

/* Buttons - Responsive */
.btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(6px, 1.5vw, 8px);
  padding: clamp(10px, 2vw, 14px) clamp(16px, 3vw, 24px);
  border: none;
  border-radius: var(--radius-md);
  font-size: clamp(13px, 2.5vw, 15px);
  font-weight: 600;
  font-family: var(--font);
  cursor: pointer;
  transition: var(--transition);
  outline: none;
}

.auth-form .btn-primary {

```
