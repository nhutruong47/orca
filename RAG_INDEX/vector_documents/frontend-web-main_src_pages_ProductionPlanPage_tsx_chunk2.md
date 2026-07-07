# Knowledge Document: ProductionPlanPage.tsx (Chunk 3/22)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionPlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 2,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
 else {
                setSelectedPlan(null);
                setDailyTargets([]);
            }
        } catch (e) { console.error(e); }
    };

    const handleGeneratePlan = async () => {
        if (!selectedOrder) return;
        setGenerating(true);
        try {
            const plan = await productionService.generatePlan(selectedOrder.id);
            setPlans(prev => [plan, ...prev]);
            setSelectedPlan(plan);
            setDailyTargets(plan.dailyTargets || []);
            alert('AI da tao ke hoach san xuat! Vui long xem va duyet.');
        } catch (e: any) {
            alert(e.response?.data?.error || 'Loi tao ke hoach');
        } finally {
            setGenerating(false);
        }
    };

    const handleApprovePlan = async () => {
        if (!selectedPlan) return;
        setApproving(true);
        try {
            const approved = await productionService.approvePlan(selectedPlan.id!, userId);
            setSelectedPlan(approved);
            setPlans(prev => prev.map(p => p.id === approved.id ? approved : p));
            alert('Da duyet ke hoach! Don hang bat dau san xuat.');
        } catch (e: any) {
            alert(e.response?.data?.error || 'Loi duyet ke hoach');
        } finally {
            setApproving(false);
        }
    };

    const loadPlanTargets = async (planId: string) => {
        try {
            const targets = await productionService.getDailyTargetsByPlan(planId);
            setDailyTargets(targets || []);
            setTargetEdits({});
        } catch (e) { console.error(e); }
    };

    const handleSaveTarget = async (target: DailyTarget) => {
        if (!target.id) return;
        const edit = targetEdits[target.id];
        if (!edit) return;
        setSavingTargetId(target.id);
        try {
            const updated = await productionService.updateDailyActual(target.id, {
                actualRoastKg: edit.actual,
                actualQcKg: edit.actual,
                actualPackagedKg: edit.actual,
                notes: target.notes
            });
            setDailyTargets(prev => prev.map(t => t.id === target.id ? updated : t));
            setTargetEdits(prev => {
                const next = { ...prev };
                delete next[target.id!];
                return next;
            });
        } catch (e: any) {

```
