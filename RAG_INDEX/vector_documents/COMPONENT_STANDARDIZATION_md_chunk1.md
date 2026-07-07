# Knowledge Document: COMPONENT_STANDARDIZATION.md (Chunk 2/4)

## Metadata
```json
{
  "file_path": "COMPONENT_STANDARDIZATION.md",
  "language": "md",
  "module": "orca",
  "business_domain": "production",
  "tags": [
    "production",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: production, chat

## Source Code Chunk
```md
/div>
```

---

## 3. Form Elements

### 3.1 Input Fields

```tsx
// Standard input
<input className="input" type="text" placeholder="Enter text..." />

// With icon
<div className="input-icon-wrap">
  <ion-icon name="search"></ion-icon>
  <input className="input" placeholder="Search..." />
</div>

// Form group with label
<div className="form-group">
  <label className="form-label">Email</label>
  <input className="form-input" type="email" />
</div>
```

### 3.2 Select

```tsx
<select className="input">
  <option value="1">Option 1</option>
  <option value="2">Option 2</option>
</select>
```

### 3.3 Textarea

```tsx
<textarea className="input" rows={4} placeholder="Description..." />
```

---

## 4. Data Display

### 4.1 Tables

```tsx
<table className="data-table">
  <thead>
    <tr>
      <th>Column 1</th>
      <th>Column 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data 1</td>
      <td>Data 2</td>
    </tr>
  </tbody>
</table>
```

### 4.2 KPI Cards

```tsx
<div className="kpi-card" style={{ '--kpi-accent': 'var(--brand)' }}>
  <div className="kpi-card-head">
    <div className="kpi-icon-container">
      <ion-icon name="chart"></ion-icon>
    </div>
    <span className="kpi-trend up">+12%</span>
  </div>
  <div className="kpi-label">Revenue</div>
  <div className="kpi-value">1,234,567</div>
</div>
```

### 4.3 Progress Bars

```tsx
<div className="progress-track">
  <div className="progress-fill" style={{ width: '75%' }} />
</div>

// With status color
<div className="progress-fill success" style={{ width: '100%' }} />
```

---

## 5. Navigation

### 5.1 Tabs

```tsx
<div className="tabs-container">
  <button className="tab-btn active">Tab 1</button>
  <button className="tab-btn">Tab 2</button>
  <button className="tab-btn">Tab 3</button>
</div>
```

### 5.2 Page Header

```tsx
<div className="page-header">
  <div className="page-header-content">
    <h1 className="page-title">
      <ion-icon name="cube"></ion-icon>
      Page Title
    </h1>
    <p className="page-subtitle">Page description text</p>
  </div>
  <div className="page-header-actions">
    <button className="btn btn-primary">Action</button>
  </div>
</div>
```

---

## 6. Feedback

### 6.1 Empty State

```tsx
<div className="empty-state">
  <ion-icon name="folder-open"></ion-icon>
  <h3 className="empty-state-title">No data</h3>
  <p>Description of empty state</p>

```
