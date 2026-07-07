# Knowledge Document: MarketplacePage.tsx (Chunk 11/70)

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
  "chunk_index": 10,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
].value);
    const [rfqDeadline, setRfqDeadline] = useState('');
    const [rfqBudget, setRfqBudget] = useState('');
    const [rfqQuality, setRfqQuality] = useState('');
    const [rfqPackaging, setRfqPackaging] = useState('');
    const [rfqNote, setRfqNote] = useState('');
    const [submitting, setSubmitting] = useState(false);
    const [showAiMatching, setShowAiMatching] = useState(false);
    const [aiMatchingProgress, setAiMatchingProgress] = useState(0);

    // Delivery profile fields
    const [deliveryPhone, setDeliveryPhone] = useState('');
    const [deliveryPhoneAlt, setDeliveryPhoneAlt] = useState('');
    const [deliveryAddress, setDeliveryAddress] = useState('');
    const [deliveryFrom, setDeliveryFrom] = useState('');
    const [deliveryTo, setDeliveryTo] = useState('');
    const [deliveryFailureAction, setDeliveryFailureAction] = useState('RETRY_LATER');
    const [deliveryNote, setDeliveryNote] = useState('');

    const [showPublishModal, setShowPublishModal] = useState(false);
    const [publishTeamId, setPublishTeamId] = useState('');
    const [pubFactoryType, setPubFactoryType] = useState('');
    const [pubSpecialty, setPubSpecialty] = useState('');
    const [pubCapacityValue, setPubCapacityValue] = useState('');
    const [pubCapacityUnit, setPubCapacityUnit] = useState('kg/tháng');
    const [pubRegion, setPubRegion] = useState('');
    const [pubDescription, setPubDescription] = useState('');
    const [pubFactoryImageUrl, setPubFactoryImageUrl] = useState('');
    const [pubFactoryImages, setPubFactoryImages] = useState<string[]>([]);
    const [pubBusinessLicense, setPubBusinessLicense] = useState('');
    const [pubBusinessAddress, setPubBusinessAddress] = useState('');
    const [pubWebsiteUrl, setPubWebsiteUrl] = useState('');
    const [pubFacebookUrl, setPubFacebookUrl] = useState('');
    const [pubCertificates, setPubCertificates] = useState<string[]>([]);
    const [pubCertificationDocument, setPubCertificationDocument] = useState('');
    const [publishing, setPublishing] = useState(false);
    const editingPublishedTeam = myTeams.find(team => team.id === publishTeamId && team.isPublished);
    const selectedPublishTeam = myTeams.find(team => team.id === publishTeamId);
    const publishVerificationStatus = selectedPublishTeam?.verificationStatus || 'NOT_SUBMITTED';


```
