# Knowledge Document: App.css (Chunk 1/43)

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
  "chunk_index": 0,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
/* ===================================================
   ORCA Management System - Component Styles
   =================================================== */

/* Loading Screen - Responsive */
.loading-screen {
  min-height: 100vh;
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: clamp(12px, 3vw, 16px);
  background: var(--bg-primary);
  color: var(--text-secondary);
}

.loading-spinner {
  width: clamp(32px, 8vw, 40px);
  height: clamp(32px, 8vw, 40px);
  border: 3px solid var(--bg-tertiary);
  border-top: 3px solid var(--accent-primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes orca-pulse {
  0%, 100% {
    opacity: 0.4;
  }
  50% {
    opacity: 0.8;
  }
}

/* Auth Container - Fixed height without scrollbar issues */
.auth-container {
  min-height: 100vh;
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-primary);
  position: relative;
  overflow: hidden;
}

/* Animated background shapes */
.auth-bg-shapes {
  position: absolute;
  inset: 0;
  overflow: hidden;
  z-index: 0;
}

.shape {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.4;
}

.shape-1 {
  width: 400px;
  height: 400px;
  background: var(--accent-primary);
  top: -100px;
  right: -100px;
  animation: float1 8s ease-in-out infinite;
}

.shape-2 {
  width: 300px;
  height: 300px;
  background: var(--accent-secondary);
  bottom: -80px;
  left: -80px;
  animation: float2 10s ease-in-out infinite;
}

.shape-3 {
  width: 200px;
  height: 200px;
  background: #6f4e37;
  top: 50%;
  left: 50%;
  animation: float3 12s ease-in-out infinite;
}

@keyframes float1 {

  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }

  50% {
    transform: translate(-40px, 40px) scale(1.1);
  }
}

@keyframes float2 {

  0%,
  100% {
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

```
