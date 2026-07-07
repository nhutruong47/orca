# Knowledge Document: adminService.ts (Chunk 2/2)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/services/adminService.ts",
  "language": "ts",
  "module": "services",
  "business_domain": "admin",
  "tags": [
    "admin",
    "payment"
  ],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, payment

## Source Code Chunk
```ts
d}/reset-password`).then(r => r.data),
    
    updateTeam: (id: string, details: Partial<AdminTeam>) =>
        api.put<AdminTeam>(`/api/admin/teams/${id}`, details).then(r => r.data),
    deleteTeam: (id: string) =>
        api.delete(`/api/admin/teams/${id}`).then(r => r.data),
    
    getPlans: () =>
        api.get<any[]>('/api/admin/plans').then(r => r.data),
    createPlan: (plan: any) =>
        api.post<any>('/api/admin/plans', plan).then(r => r.data),
    updatePlan: (id: string, plan: any) =>
        api.put<any>(`/api/admin/plans/${id}`, plan).then(r => r.data),
    deletePlan: (id: string) =>
        api.delete(`/api/admin/plans/${id}`).then(r => r.data),
        
    getAiConfigs: () =>
        api.get<Record<string, string>>('/api/admin/ai-configs').then(r => r.data),
    updateAiConfigs: (configs: Record<string, string>) =>
        api.put('/api/admin/ai-configs', configs).then(r => r.data),
};

```
