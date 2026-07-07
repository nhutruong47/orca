# Knowledge Document: Profile.css (Chunk 1/4)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Profile.css",
  "language": "css",
  "module": "components",
  "business_domain": "security",
  "tags": [
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in components.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```css
/* PREMIUM PROFILE STYLES */

.profile-header-backdrop {
    position: absolute;
    top: -20px; left: -20px; right: -20px; bottom: -20px;
    background-size: cover;
    background-position: center;
    filter: blur(20px) brightness(0.4);
    z-index: 0;
    opacity: 0.6;
}

.avatar-edit-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.6);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    opacity: 0;
    transition: all 0.3s ease;
    backdrop-filter: blur(4px);
}

.profile-avatar-large:hover .avatar-edit-overlay {
    opacity: 1;
}

.avatar-edit-btn {
    background: rgba(255,255,255,0.2);
    border: 1px solid rgba(255,255,255,0.4);
    color: #fff;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 20px;
}

.avatar-edit-btn:hover {
    background: rgba(255,255,255,0.4);
    transform: scale(1.1);
}

.avatar-uploading-spinner {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.7);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #3b82f6;
    font-size: 32px;
}

.profile-edit-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 16px;
}

.premium-input-group {
    position: relative;
    width: 100%;
}

.premium-input {
    width: 100%;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 16px 20px 16px 45px;
    border-radius: 12px;
    color: var(--shell-text-main);
    font-size: 15px;
    transition: all 0.3s ease;
    outline: none;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
}

body.theme-light .premium-input {
    background: rgba(0, 0, 0, 0.02);
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
}

.premium-input:focus,
.premium-input:valid {
    border-color: #3b82f6;
    background: rgba(59, 130, 246, 0.05);
}

.premium-label {
    position: absolute;
    left: 45px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--shell-text-soft);
    font-size: 15px;
    transition: all 0.3s ease;
    pointer-events: none;
}


```
