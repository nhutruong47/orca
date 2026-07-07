# Knowledge Document: App.tsx (Chunk 2/2)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/App.tsx",
  "language": "tsx",
  "module": "src",
  "business_domain": "admin",
  "tags": [
    "admin",
    "payment",
    "dashboard"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, payment, dashboard

## Source Code Chunk
```tsx
oute path="/profile" element={<ProfilePage />} />
                            <Route path="/groups" element={<GroupsPage />} />
                            <Route path="/groups/:id" element={<GroupDetailPage />} />
                            <Route path="/groups/:id/create-task" element={<CreateTaskPage />} />
                            <Route path="/orders" element={<OrderManagementPage />} />
                            <Route path="/admin" element={<AdminPage />} />
                            <Route path="/settings" element={<SettingsPage />} />
                            <Route path="/upgrade" element={<UpgradePlanPage />} />
                            <Route path="/nang-cap-goi" element={<UpgradePlanPage />} />
                            <Route path="/payment-result" element={<PaymentResultPage />} />
                            <Route path="/vnpay-mock-checkout" element={<VnpayMockCheckoutPage />} />
                        </Route>

                        <Route path="/marketplace" element={<ProtectedRoute><MarketplacePage /></ProtectedRoute>} />
                        <Route path="/dat-hang" element={<ProtectedRoute><MarketplacePage /></ProtectedRoute>} />
                        <Route path="/thi-truong-dat-hang" element={<ProtectedRoute><MarketplacePage /></ProtectedRoute>} />
                        <Route path="/" element={<HomePage />} />
                        <Route path="/ban-sac" element={<HomePage />} />
                        <Route path="/san-pham" element={<Navigate to="/ban-sac#products" replace />} />
                        <Route path="/cong-nghe" element={<Navigate to="/ban-sac#process" replace />} />
                        <Route path="/lien-he" element={<Navigate to="/ban-sac#footer" replace />} />
                        <Route path="*" element={<Navigate to="/" replace />} />
                    </Routes>
                </AuthProvider>
            </ThemeProvider>
        </BrowserRouter>
    );
}

export default App;

```
