# Knowledge Document: test_admin_api.py (Chunk 1/1)

## Metadata
```json
{
  "file_path": "test_admin_api.py",
  "language": "py",
  "module": "orca",
  "business_domain": "admin",
  "tags": [
    "admin",
    "payment",
    "authorization"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, payment, authorization

## Source Code Chunk
```py
import urllib.request
import json

base_url = "https://orca-backend-j82z.onrender.com"

# 1. Login as admin
login_data = json.dumps({"username": "admin", "password": "Admin@123"}).encode("utf-8")
req = urllib.request.Request(f"{base_url}/api/auth/login", data=login_data, headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode())
        token = res.get("token")
        print("Login successful. Token:", token[:20], "...")
        
        endpoints = ["overview", "users", "teams", "orders", "tasks", "payments"]
        for ep in endpoints:
            req_ep = urllib.request.Request(f"{base_url}/api/admin/{ep}", headers={'Authorization': f'Bearer {token}'})
            try:
                with urllib.request.urlopen(req_ep) as res_ep:
                    print(f"[{ep}] SUCCESS: {res_ep.status}")
            except Exception as e:
                print(f"[{ep}] FAILED:", e)
                if hasattr(e, 'read'):
                    with open(f"error_{ep}.txt", "w", encoding="utf-8") as f:
                        f.write(e.read().decode())
                    print(f"Saved error response to error_{ep}.txt")
                
except Exception as e:
    print("Login failed:", e)
    if hasattr(e, 'read'):
        print("Response:", e.read().decode())

```
