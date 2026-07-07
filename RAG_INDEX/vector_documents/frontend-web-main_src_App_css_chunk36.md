# Knowledge Document: App.css (Chunk 37/43)

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
  "chunk_index": 36,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
);
  background: rgba(12, 19, 34, 0.62);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 8px;
  box-shadow: 0 28px 90px rgba(0, 0, 0, 0.34);
  backdrop-filter: blur(20px) saturate(1.08);
}

.login-form-header {
  margin-bottom: 24px;
}

.login-logo-row {
  gap: 13px;
  margin-bottom: 24px;
}

.login-logo-icon {
  width: 64px;
  height: 54px;
  display: grid;
  place-items: center;
  color: #0c1322;
  background: transparent;
  border-radius: 0;
  box-shadow: none;
}

.login-logo-icon span {
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  color: #fff;
  border: 2px solid rgba(255, 255, 255, 0.92);
  border-radius: 50%;
  font-size: 0.78rem;
  font-weight: 950;
}

.login-logo-icon img {
  width: 62px;
  height: 50px;
  display: block;
  object-fit: contain;
  filter: drop-shadow(0 8px 14px rgba(0, 0, 0, 0.34));
}

.login-logo-text {
  display: grid;
  gap: 2px;
  color: #fff;
  line-height: 1;
}

.login-logo-text strong {
  font-size: 1.18rem;
  font-weight: 900;
  letter-spacing: 0.08em;
}

.login-logo-text small {
  color: rgba(255, 247, 236, 0.58);
  font-size: 0.82rem;
  font-weight: 750;
}

.login-form-title {
  margin: 0 0 8px;
  color: #fffaf2;
  font-size: clamp(2.35rem, 3vw, 3rem);
  line-height: 1.12;
}

.login-form-subtitle {
  margin: 0;
  color: rgba(255, 247, 236, 0.68);
  font-size: 1.08rem;
  font-weight: 600;
}

.login-form {
  display: grid;
  gap: 16px;
}

.login-field label {
  display: inline-block;
  margin-bottom: 8px;
  color: rgba(255, 247, 236, 0.88);
  font-size: 0.96rem;
  font-weight: 800;
}

.login-split .login-input-wrap input {
  width: 100%;
  min-height: 66px;
  padding-left: 54px;
  font-size: 1.08rem;
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(255, 255, 255, 0.17);
  border-radius: 8px;
}

.login-btn-primary,
.login-btn-google {
  width: 100%;
  min-height: 66px;
  border-radius: 8px;
  font-size: 1.02rem;
  font-weight: 800;
}

.login-divider,
.login-footer {
  width: 100%;
}

.login-demo {
  background: rgba(255, 255, 255, 0.035);
  border-color: rgba(255, 255, 255, 0.08);
  border-radius: 8px;
}

.login-demo-accounts {
  gap: 8px;
}

.login-demo-btn {
  min-height: 42px;
  border-radius: 7px;
}

.login-split .login-hero-title,
.login-split .login-form-title,
.login-split .login-logo-text,
.login-split .login-logo-text strong {
  color: #fffaf2 !important;
}


```
