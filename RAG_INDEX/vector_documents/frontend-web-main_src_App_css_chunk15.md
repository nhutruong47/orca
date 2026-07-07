# Knowledge Document: App.css (Chunk 16/43)

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
  "chunk_index": 15,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
: center;
  justify-content: space-between;
  padding: 32px 36px;
  background: var(--accent-gradient);
  border-radius: var(--radius-lg);
  box-shadow: 0 8px 25px rgba(212, 165, 116, 0.2);
  position: relative;
  overflow: hidden;
}

.welcome-banner::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -20%;
  width: 300px;
  height: 300px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 50%;
}

.welcome-content {
  z-index: 1;
}

.welcome-greeting {
  font-size: 14px;
  opacity: 0.85;
  margin-bottom: 4px;
}

.welcome-name {
  font-size: 28px;
  font-weight: 800;
  color: white;
  margin-bottom: 4px;
}

.welcome-role {
  font-size: 14px;
  opacity: 0.8;
}

.welcome-illustration {
  font-size: 72px;
  z-index: 1;
  animation: logoFloat 3s ease-in-out infinite;
}

/* Stats Grid - Responsive */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(clamp(160px, 20vw, 220px), 1fr));
  gap: clamp(12px, 2vw, 16px);
}

.stat-card {
  display: flex;
  align-items: center;
  gap: clamp(12px, 2vw, 16px);
  padding: clamp(16px, 3vw, 24px);
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  transition: var(--transition);
  cursor: default;
}

.stat-card:hover {
  background: var(--bg-card-hover);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.stat-icon {
  font-size: clamp(20px, 4vw, 28px);
  width: clamp(40px, 8vw, 52px);
  height: clamp(40px, 8vw, 52px);
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(212, 165, 116, 0.1);
  border-radius: var(--radius-md);
  flex-shrink: 0;
}

.stat-info {
  display: flex;
  flex-direction: column;
}

.stat-label {
  font-size: clamp(9px, 2vw, 12px);
  color: var(--text-muted);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stat-value {
  font-size: clamp(13px, 3vw, 16px);
  font-weight: 600;
  color: var(--text-primary);
  margin-top: 2px;
}

/* Sections */
.section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* Section Title - Responsive */
.section-title {
  font-size: clamp(14px, 4vw, 18px);
  font-weight: 700;
  color: var(--text-primary);
}

/* Actions Grid */
.actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(clamp(150px, 20vw, 200px), 1fr));
  gap: clamp(12px, 2vw, 16px);
}

.action-card {

```
