# Knowledge Document: MarketplacePage.tsx (Chunk 17/70)

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
  "chunk_index": 16,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx


    const handleDocumentFile = (event: React.ChangeEvent<HTMLInputElement>, setter: (value: string) => void) => {
        const file = event.target.files?.[0];
        if (!file) return;
        if (!['application/pdf', 'image/jpeg', 'image/png'].includes(file.type)) {
            alert('Tài liệu chỉ hỗ trợ PDF, JPG hoặc PNG.');
            event.target.value = '';
            return;
        }
        if (file.size > 10 * 1024 * 1024) {
            alert('Tài liệu tối đa 10MB.');
            event.target.value = '';
            return;
        }
        const reader = new FileReader();
        reader.onload = () => setter(String(reader.result || ''));
        reader.readAsDataURL(file);
        event.target.value = '';
    };

    const openChat = (factory: MarketplaceFactory) => {
        setChatTarget(factory);
        setChatDraft('');
        setChatMessages([{ sender: 'other', text: `Chào bạn, ${factory.name} có thể giúp gì cho bạn?` }]);
        setShowChatModal(true);
    };

    const handleSaveChatDraft = () => {
        if (!chatDraft.trim()) return;
        const newMsg = chatDraft.trim();
        setChatMessages(prev => [...prev, { sender: 'me', text: newMsg }]);
        setChatDraft('');

        setTimeout(() => {
            setChatMessages(prev => [...prev, { sender: 'other', text: 'Dạ, xưởng đã nhận được thông tin và sẽ phản hồi lại sớm ạ.' }]);
        }, 1500);
    };

    const handleOrderClick = (seller?: Team) => {
        setSelectedSeller(seller || null);
        setBuyerTeamId(myTeams[0]?.id || '');
        setRfqTitle('');
        setRfqRequestType(RFQ_SERVICE_OPTIONS[0].value);
        setRfqProductName('');
        setRfqQuantity(1);
        setRfqUnit(RFQ_UNIT_OPTIONS[0].value);
        setRfqDeadline('');
        setRfqBudget('');
        setRfqQuality('');
        setRfqPackaging('');
        setRfqNote('');
        setDeliveryPhone('');
        setDeliveryPhoneAlt('');
        setDeliveryAddress('');
        setDeliveryFrom('');
        setDeliveryTo('');
        setDeliveryFailureAction('RETRY_LATER');
        setDeliveryNote('');
        setShowOrderModal(true);
    };

    const handleSubmitOrder = async (event: React.FormEvent) => {
        event.preventDefault();
        if (!rfqTitle.trim() || !rfqProductName.trim()) return;
        if (rfqQuantity <= 0) {
            alert('Số lượng phải lớn hơn 0.');

```
