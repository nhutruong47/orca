# Knowledge Document: App.css (Chunk 17/43)

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
  "chunk_index": 16,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
ns */
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
  padding: clamp(14px, 3vw, 24px);
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  cursor: pointer;
  transition: var(--transition);
}

.action-card:hover {
  background: var(--bg-card-hover);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: rgba(212, 165, 116, 0.3);
}

.action-icon {
  font-size: clamp(24px, 5vw, 32px);
  margin-bottom: 12px;
}

.action-card h3 {
  font-size: clamp(12px, 2.5vw, 15px);
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 4px;
}

.action-card p {
  font-size: clamp(11px, 2vw, 13px);
  color: var(--text-muted);
}

/* Profile Page - Responsive */
.profile-page {
  display: flex;
  flex-direction: column;
  gap: clamp(20px, 3vw, 28px);
  max-width: 100%;
  animation: pageEnter 0.4s ease-out;
}

.profile-header {
  text-align: center;
  padding: clamp(24px, 5vw, 40px) 0;
}

.profile-avatar-large {
  width: clamp(64px, 12vw, 96px);
  height: clamp(64px, 12vw, 96px);
  border-radius: 50%;
  background: var(--accent-gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: clamp(24px, 6vw, 40px);
  font-weight: 800;
  margin: 0 auto clamp(12px, 2vw, 16px);
  box-shadow: 0 8px 25px rgba(212, 165, 116, 0.3);
}

.profile-name {
  font-size: clamp(18px, 4vw, 24px);
  font-weight: 700;
  margin-bottom: 8px;
}

.profile-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.profile-fields {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.profile-field {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 18px 20px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  transition: var(--transition);
}

.profile-field:hover {
  background: var(--bg-card-hover);
}

.field-icon {
  font-size: 22px;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;

```
