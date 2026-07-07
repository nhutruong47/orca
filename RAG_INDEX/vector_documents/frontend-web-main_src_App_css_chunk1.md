# Knowledge Document: App.css (Chunk 2/43)

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
  "chunk_index": 1,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
 transform: translate(0, 0) scale(1);
  }

  50% {
    transform: translate(30px, -30px) scale(1.15);
  }
}

@keyframes float3 {

  0%,
  100% {
    transform: translate(-50%, -50%) scale(1);
  }

  50% {
    transform: translate(-45%, -55%) scale(1.2);
  }
}

/* Auth Card - Responsive */
.auth-card {
  position: relative;
  z-index: 1;
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  padding: clamp(24px, 5vw, 48px) clamp(20px, 4vw, 40px);
  width: clamp(300px, 90vw, 440px);
  max-width: 90vw;
  box-shadow: var(--shadow-lg), var(--shadow-glow);
  animation: cardEnter 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes cardEnter {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.97);
  }

  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.auth-logo {
  text-align: center;
  margin-bottom: 32px;
}

.auth-logo-icon {
  width: clamp(92px, 22vw, 128px);
  height: clamp(58px, 14vw, 80px);
  display: block;
  object-fit: contain;
  margin: 0 auto 8px;
  animation: logoFloat 3s ease-in-out infinite;
  filter: drop-shadow(0 10px 18px rgba(0, 0, 0, 0.32));
}

@keyframes logoFloat {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-6px);
  }
}

.auth-logo-text {
  font-size: 28px;
  font-weight: 800;
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: 3px;
}

.auth-subtitle {
  color: var(--text-secondary);
  font-size: 14px;
  margin-top: 4px;
}

/* Form Styles */
.auth-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-label {
  font-size: 13px;
  font-weight: 500;
  color: #8b949e;
  letter-spacing: 0.3px;
}

.input-container {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
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

```
