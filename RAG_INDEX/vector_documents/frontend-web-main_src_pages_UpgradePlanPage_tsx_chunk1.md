# Knowledge Document: UpgradePlanPage.tsx (Chunk 2/3)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/UpgradePlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```tsx
     'Thương hiệu riêng cho doanh nghiệp'
        ],
        theme: 'dark',
    },
];

export default function UpgradePlanPage() {

    const handleSelectPlan = async (plan: Plan) => {
        if (plan.id === 'starter') {
            return;
        }
        localStorage.setItem('orca-ai-plan-pending', plan.id);
        localStorage.setItem('orca-payment-method', 'PAYOS');
        
        try {
            const res = await paymentService.createPayosPayment(plan.id);
            window.location.href = res.checkoutUrl;
        } catch (err) {
            console.error(err);
            alert('Có lỗi xảy ra khi tạo link thanh toán PayOS. Vui lòng thử lại.');
        }
    };

    return (
        <div className="pricing-page">
            <section className="pricing-header">
                <h1>Giải pháp AI cho sản xuất</h1>
                <p>Chọn gói phù hợp để tối ưu quy trình và nâng cao năng suất nhà máy của bạn.</p>
            </section>



            <section className="pricing-grid">
                {plans.map((plan) => {
                    return (
                        <article
                            key={plan.id}
                            className={`pricing-card theme-${plan.theme} ${plan.featured ? 'featured' : ''}`}
                        >
                            {plan.featured && <span className="pricing-ribbon">★ Phổ biến nhất</span>}
                            
                            <h2>{plan.name}</h2>
                            
                            <div className="pricing-price">
                                <strong>{plan.price}</strong>
                                <span>{plan.priceNote}</span>
                            </div>

                            <div className="pricing-subtitle">
                                <strong>{plan.subtitle}</strong>
                                <span>{plan.target}</span>
                            </div>

                            <button
                                type="button"
                                className="pricing-action"
                                onClick={() => handleSelectPlan(plan)}
                            >
                                {plan.buttonText}
                            </button>

                            <ul className="pricing-features">
                                {plan.features.map((feature) => (

```
