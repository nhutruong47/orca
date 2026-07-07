# Knowledge Document: UpgradePlanPage.tsx (Chunk 3/3)

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
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```tsx
         type="button"
                                className="pricing-action"
                                onClick={() => handleSelectPlan(plan)}
                            >
                                {plan.buttonText}
                            </button>

                            <ul className="pricing-features">
                                {plan.features.map((feature) => (
                                    <li key={feature}>
                                        <CheckCircle2 className="check-icon" size={18} />
                                        <span>{feature}</span>
                                    </li>
                                ))}
                            </ul>
                        </article>
                    );
                })}
            </section>
        </div>
    );
}

```
