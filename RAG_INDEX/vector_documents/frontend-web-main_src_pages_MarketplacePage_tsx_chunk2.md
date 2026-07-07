# Knowledge Document: MarketplacePage.tsx (Chunk 3/70)

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
  "chunk_index": 2,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
el: 'Mua cà phê nhân' },
    { value: 'Blend Development', label: 'Phối trộn blend' },
    { value: 'Sample Roasting', label: 'Rang mẫu / Test profile' },
    { value: 'QC Cupping', label: 'QC / Cupping' },
    { value: 'Drying', label: 'Sấy / sơ chế' },
    { value: 'Other', label: 'Khác' },
];
const RFQ_UNIT_OPTIONS = [
    { value: 'kg', label: 'kg' },
    { value: 'ton', label: 'Tấn (Ton)' },
    { value: 'bag', label: 'Bao' },
    { value: 'package', label: 'Gói' },
    { value: 'batch', label: 'Mẻ / Batch' },
];
const COFFEE_TYPE_OPTIONS = [
    { value: 'Arabica', label: 'Arabica' },
    { value: 'Robusta', label: 'Robusta' },
    { value: 'Liberica', label: 'Liberica' },
    { value: 'Excelsa', label: 'Excelsa' },
    { value: 'Blend', label: 'Blend (Phối trộn)' },
    { value: 'Arabica Specialty', label: 'Arabica Specialty' },
    { value: 'Fine Robusta', label: 'Fine Robusta' },
    { value: 'Culi / Peaberry', label: 'Culi / Peaberry' },
    { value: 'Moka', label: 'Moka' },
    { value: 'Catimor', label: 'Catimor' },
    { value: 'Bourbon', label: 'Bourbon' },
    { value: 'Typica', label: 'Typica' },
    { value: 'Caturra', label: 'Caturra' },
    { value: 'Gesha / Geisha', label: 'Gesha / Geisha' },
    { value: 'Ethiopia Heirloom', label: 'Ethiopia Heirloom' },
    { value: 'Colombia Supremo', label: 'Colombia Supremo' },
    { value: 'Brazil Santos', label: 'Brazil Santos' },
    { value: 'Vietnam Robusta', label: 'Vietnam Robusta' },
    { value: 'Green Coffee Beans', label: 'Cà phê nhân xanh' },
    { value: 'Roasted Beans', label: 'Cà phê rang nguyên hạt' },
    { value: 'Ground Coffee', label: 'Cà phê rang xay' },
    { value: 'Instant Coffee', label: 'Cà phê hòa tan' },
    { value: 'Other', label: 'Khác' },
];
const ROAST_PROFILE_OPTIONS = [
    { value: 'Light', label: 'Light Roast' },
    { value: 'Medium Light', label: 'Medium Light' },
    { value: 'Medium', label: 'Medium Roast' },
    { value: 'Medium Dark', label: 'Medium Dark' },
    { value: 'Dark', label: 'Dark Roast' },
    { value: 'Espresso Roast', label: 'Espresso Roast' },
    { value: 'Custom', label: 'Theo profile riêng' },
];
const PACKAGING_FORMAT_OPTIONS = [
    { value: '100g', label: 'Túi 100g' },
    { value: '250g', label: 'Túi 250g' },
    { value: '500g', label: 'Túi 500g' },
    { value: '1kg', label: 'Túi 1kg' },
    { value: '5kg', label: 'Bao 5kg' },

```
