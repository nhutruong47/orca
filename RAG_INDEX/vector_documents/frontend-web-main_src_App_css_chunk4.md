# Knowledge Document: App.css (Chunk 5/43)

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
  "chunk_index": 4,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css

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
  background: linear-gradient(135deg, #d4a574, #8b5e3c);
  color: white;
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 4px 15px rgba(212, 165, 116, 0.3);
}

.auth-form .btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(212, 165, 116, 0.4);
}

.btn-primary {
  background: var(--accent-gradient);
  color: white;
  box-shadow: 0 4px 15px rgba(212, 165, 116, 0.3);
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(212, 165, 116, 0.4);
}

.btn-primary:active:not(:disabled) {
  transform: translateY(0);
}

.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.btn-loading {
  position: relative;
}

.btn-spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

/* Auth Divider */
.auth-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 20px 0;
}

.auth-divider::before,
.auth-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}

.auth-divider span {
  font-size: 13px;
  color: var(--text-muted);
  font-weight: 500;
}

/* Google Login Button */
.btn-google {
  width: 100%;
  background: var(--bg-input);
  border: 1px solid var(--border);
  color: var(--text-primary);
  font-weight: 500;
}

.btn-google:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-focus);
  transform: translateY(-1px);
}

.google-icon {
  flex-shrink: 0;
}

/* Auth Footer */
.auth-footer {
  text-align: center;
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid var(--border);
}

.auth-footer p {
  color: var(--text-secondary);
  font-size: 14px;
}

.auth-link {
  color: var(--accent-primary);
  font-weight: 600;
  transition: var(--transition);
}

.auth-link:hover {
  color: var(--text-accent);
  text-decoration: underline;
}

/* Split Layout - Responsive */
.login-split {

```
