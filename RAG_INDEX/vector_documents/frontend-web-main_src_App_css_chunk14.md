# Knowledge Document: App.css (Chunk 15/43)

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
  "chunk_index": 14,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
gin-bottom: 20px;
}

.tabs-header {
  display: flex;
  gap: 4px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 4px;
}

.tab-btn {
  flex: 1;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  background: transparent;
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 600;
  font-family: var(--font);
  cursor: pointer;
  transition: var(--transition);
}

.tab-btn:hover {
  color: var(--text-primary);
  background: var(--bg-input);
}

.tab-btn.active {
  background: linear-gradient(135deg, rgba(212, 165, 116, 0.2) 0%, rgba(139, 94, 60, 0.2) 100%);
  color: var(--accent-primary);
  box-shadow: 0 0 12px rgba(212, 165, 116, 0.3);
  border: 1px solid rgba(212, 165, 116, 0.4);
}

/* Goals / Orders Table */
.goals-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
}

.goals-table thead {
  background: var(--bg-tertiary);
}

.goals-table th {
  padding: 14px 16px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border);
}

.goals-table td {
  padding: 14px 16px;
  font-size: 13px;
  color: var(--text-primary);
  border-bottom: 1px solid var(--border);
}

.goals-table tbody tr {
  transition: var(--transition);
}

.goals-table tbody tr:hover {
  background: var(--bg-input);
}

.goals-table tbody tr:last-child td {
  border-bottom: none;
}

/* ============================================
   DASHBOARD PAGE
   ============================================ */
.dashboard {
  display: flex;
  flex-direction: column;
  gap: 28px;
  animation: pageEnter 0.4s ease-out;
}

@keyframes pageEnter {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Welcome Banner */
.welcome-banner {
  display: flex;
  align-items: center;
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

```
