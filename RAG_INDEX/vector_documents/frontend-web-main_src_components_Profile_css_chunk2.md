# Knowledge Document: Profile.css (Chunk 3/4)

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
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in components.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```css
ion: color 0.2s;
}
.close-btn:hover {
    color: #ef4444;
}

.webcam-body {
    background: #000;
    position: relative;
    aspect-ratio: 4/3;
    display: flex;
    justify-content: center;
    align-items: center;
}

.webcam-video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transform: scaleX(-1); /* Mirror effect */
}

.webcam-footer {
    padding: 20px;
    display: flex;
    justify-content: center;
}

.capture-btn {
    padding: 12px 30px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}

.profile-feedback {
    position: sticky;
    top: 12px;
    z-index: 20;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 13px 16px;
    border: 1px solid;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
}

.profile-feedback.success {
    color: #86efac;
    background: rgba(22, 101, 52, 0.2);
    border-color: rgba(74, 222, 128, 0.35);
}

.profile-feedback.error {
    color: #fca5a5;
    background: rgba(127, 29, 29, 0.2);
    border-color: rgba(248, 113, 113, 0.35);
}

.profile-feedback button,
.profile-password-close {
    margin-left: auto;
    border: 0;
    background: transparent;
    color: inherit;
    cursor: pointer;
    font-size: 20px;
}

.profile-security-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}

.profile-security-actions button {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    min-height: 42px;
    padding: 10px 16px;
}

.profile-password-panel {
    padding: 20px;
    border: 1px solid var(--shell-border);
    border-radius: 12px;
    background: var(--shell-surface-soft);
}

.profile-password-heading {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 16px;
    margin-bottom: 18px;
}

.profile-password-heading h3 {
    margin: 0 0 5px;
    color: var(--shell-title);
    font-size: 17px;
}

.profile-password-heading p {
    margin: 0;
    color: var(--shell-text-soft);
    font-size: 13px;
}

.profile-password-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
}

.profile-password-grid label {
    display: flex;
    flex-direction: column;
    gap: 7px;
    color: var(--shell-text-soft);
    font-size: 12px;

```
