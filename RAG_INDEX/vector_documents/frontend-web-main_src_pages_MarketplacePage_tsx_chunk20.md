# Knowledge Document: MarketplacePage.tsx (Chunk 21/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 20,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
    const [teamsAll, teamsMine] = await Promise.all([teamService.getAllTeams(), teamService.getMyTeams()]);
            setAllTeams(teamsAll.filter(t => t.isPublished));
            setMyTeams(teamsMine.filter(t => t.ownerId === user?.id));
        } catch {
            alert('Không thể gỡ xưởng.');
        }
    };

    const deliveryResultLabel = (status?: string) => {
        switch (status) {
            case 'ON_TIME': return 'Giao đúng hẹn';
            case 'LATE': return 'Giao trễ';
            case 'NOT_DELIVERED': return 'Chưa nhận hàng';
            default: return 'Chưa rõ';
        }
    };

    const canManageReview = (review: Review) => {
        if (!user) return false;
        const ownsByUser = review.buyerUserId === user.id;
        const ownsByTeam = myTeams.some(team => team.id === review.buyerTeamId && team.ownerId === user.id);
        return ownsByUser || ownsByTeam;
    };

    const startEditReview = (review: Review) => {
        setEditingReviewId(review.id);
        setEditReviewRating(review.rating);
        setEditReviewStatus((review.deliveryResult as "ON_TIME" | "LATE" | "NOT_DELIVERED") || 'ON_TIME');
        setEditReviewComment(review.comment || '');
    };

    const cancelEditReview = () => {
        setEditingReviewId(null);
        setEditReviewRating(5);
        setEditReviewStatus('ON_TIME');
        setEditReviewComment('');
    };

    const handleUpdateReview = async (factoryId: string, reviewId: string) => {
        try {
            await reviewService.update(reviewId, {
                rating: editReviewRating,
                deliveryResult: editReviewStatus,
                comment: editReviewComment,
            });
            cancelEditReview();
            await loadFactoryReviews(factoryId);
        } catch (err: any) {
            alert(err?.response?.data?.error || 'Không thể cập nhật đánh giá.');
        }
    };

    const handleDeleteReview = async (factoryId: string, reviewId: string) => {
        if (!confirm('Xóa đánh giá này? Điểm sao của xưởng sẽ được cập nhật lại.')) return;
        try {
            await reviewService.remove(reviewId);
            await loadFactoryReviews(factoryId);
        } catch (err: any) {
            alert(err?.response?.data?.error || 'Không thể xóa đánh giá.');
        }
    };

    const renderMetric = (label: string, value?: string | number | React.ReactNode) => (

```
