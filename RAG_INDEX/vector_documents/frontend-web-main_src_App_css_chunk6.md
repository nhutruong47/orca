# Knowledge Document: App.css (Chunk 7/43)

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
  "chunk_index": 6,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css

  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.6;
  max-width: 480px;
  margin-bottom: 24px;
}

/* Coffee Brands Carousel */
.login-brands {
  margin-bottom: 24px;
}

.login-brands-label {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 12px;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.login-brands-list {
  display: flex;
  gap: 10px;
  overflow: hidden;
  flex-wrap: wrap;
}

.login-brand-card {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 16px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  opacity: 0.5;
  transform: scale(0.95);
  min-width: 200px;
}

.login-brand-card.active {
  background: rgba(139, 94, 60, 0.15);
  border-color: rgba(212, 165, 116, 0.3);
  opacity: 1;
  transform: scale(1);
  box-shadow: 0 4px 20px rgba(139, 94, 60, 0.15);
}

.login-brand-emoji {
  font-size: 24px;
  flex-shrink: 0;
}

.login-brand-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-primary);
}

.login-brand-desc {
  font-size: 11px;
  color: var(--text-muted);
}

.login-brands-dots {
  display: flex;
  gap: 6px;
  margin-top: 12px;
}

.login-brands-dots .dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--border);
  cursor: pointer;
  transition: all 0.3s;
}

.login-brands-dots .dot.active {
  background: #d4a574;
  width: 18px;
  border-radius: 3px;
}

/* Hero Stats */
.login-hero-stats {
  display: flex;
  gap: 32px;
}

.login-hero-stat {
  display: flex;
  flex-direction: column;
}

.login-hero-stat .stat-value {
  font-size: 22px;
  font-weight: 800;
  color: #d4a574;
}

.login-hero-stat .stat-label {
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* --- FORM SIDE --- */
.login-form-side {
  flex: 0.8;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(20px, 3vw, 40px);
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


```
