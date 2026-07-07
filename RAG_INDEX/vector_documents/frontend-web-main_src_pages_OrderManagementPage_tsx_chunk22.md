# Knowledge Document: OrderManagementPage.tsx (Chunk 23/23)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/OrderManagementPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 22,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
)' }}>Nếu không giao được:</span>
                                                                <strong style={{ marginLeft: 6 }}>{deliveryFailureLabel(order.deliveryFailureAction)}</strong>
                                                            </div>
                                                        )}
                                                        {order.deliveryNote && (
                                                            <div style={{ gridColumn: 'span 2' }}>
                                                                <span style={{ color: 'var(--text-secondary)' }}>Ghi chú giao hàng:</span>
                                                                <span style={{ marginLeft: 6 }}>{order.deliveryNote}</span>
                                                            </div>
                                                        )}
                                                    </div>
                                                )}
                                            </div>
                                        </td>
                                    </tr>
                                )}
                                </>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}

        </div>
    );
}

```
