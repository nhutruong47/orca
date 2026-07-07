# Knowledge Document: Profile.css (Chunk 2/4)

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
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in components.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```css
 0, 0.1);
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

.premium-input:focus ~ .premium-label,
.premium-input:valid ~ .premium-label {
    top: -10px;
    left: 15px;
    font-size: 12px;
    background: var(--shell-bg-dark);
    padding: 0 5px;
    color: #3b82f6;
    border-radius: 4px;
}

body.theme-light .premium-input:focus ~ .premium-label,
body.theme-light .premium-input:valid ~ .premium-label {
    background: #ffffff;
}

.premium-input-icon {
    position: absolute;
    left: 15px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--shell-text-soft);
    font-size: 20px;
    transition: all 0.3s ease;
}

.premium-input:focus ~ .premium-input-icon {
    color: #3b82f6;
}

/* WEBCAM MODAL */
.webcam-modal-backdrop {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.8);
    backdrop-filter: blur(8px);
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
    animation: fadeIn 0.3s ease;
}

.webcam-modal {
    width: 90%;
    max-width: 500px;
    border-radius: 20px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.webcam-header {
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

body.theme-light .webcam-header {
    border-bottom: 1px solid rgba(0,0,0,0.1);
}

.webcam-header h3 {
    margin: 0;
    font-size: 18px;
    font-weight: 600;
}

.close-btn {
    background: transparent;
    border: none;
    color: var(--shell-text-soft);
    font-size: 24px;
    cursor: pointer;
    transition: color 0.2s;
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

```
