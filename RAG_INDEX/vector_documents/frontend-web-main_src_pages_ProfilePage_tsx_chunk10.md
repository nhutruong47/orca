# Knowledge Document: ProfilePage.tsx (Chunk 11/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProfilePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "security",
  "tags": [
    "security"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 10,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
           autoComplete="username"
                                    />
                                </label>
                            )}
                            <label>
                                <span>Mật khẩu mới</span>
                                <input
                                    type="password"
                                    value={passwordForm.newPassword}
                                    onChange={event => setPasswordForm(current => ({ ...current, newPassword: event.target.value }))}
                                    autoComplete="new-password"
                                />
                            </label>
                            <label>
                                <span>Nhập lại mật khẩu mới</span>
                                <input
                                    type="password"
                                    value={passwordForm.confirmPassword}
                                    onChange={event => setPasswordForm(current => ({ ...current, confirmPassword: event.target.value }))}
                                    autoComplete="new-password"
                                />
                            </label>
                        </div>

                        <div className="profile-password-actions">
                            <button type="button" className="btn-secondary" onClick={closePasswordForm}>
                                Hủy
                            </button>
                            <button type="button" className="btn-primary" onClick={handlePasswordSubmit} disabled={passwordSaving}>
                                {passwordSaving ? 'Đang cập nhật...' : 'Xác nhận'}
                            </button>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

```
