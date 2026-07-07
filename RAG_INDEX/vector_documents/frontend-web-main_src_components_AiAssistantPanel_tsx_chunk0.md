# Knowledge Document: AiAssistantPanel.tsx (Chunk 1/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/AiAssistantPanel.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "payment",
  "tags": [
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
import { useState, useRef, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { aiService } from '../services/groupService';
import { isPaymentRequiredError } from '../services/api';
import type { AiParseResult } from '../services/groupService';
import { estimateTokens, formatTokenCount } from '../utils/tokenUsage';

interface AiAssistantPanelProps {
    onCreateGoal?: (result: AiParseResult) => void;
    trialActive: boolean;
    trialDays: number;
    teamId: string;
}

interface ChatMessage {
    id: string;
    role: 'user' | 'assistant';
    content: string;
    result?: AiParseResult;
    timestamp: Date;
}

export default function AiAssistantPanel({ onCreateGoal, trialActive, trialDays, teamId }: AiAssistantPanelProps) {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const [loading, setLoading] = useState(false);
    const [showTokens, setShowTokens] = useState(false);
    const [isCollapsed, setIsCollapsed] = useState(false);
    const [panelHeight, setPanelHeight] = useState(460);
    const [isResizing, setIsResizing] = useState(false);
    const resizeStartY = useRef(0);
    const resizeStartH = useRef(0);
    const messagesEndRef = useRef<HTMLDivElement>(null);
    const totalTokens = messages.reduce((sum, message) => sum + estimateTokens(message.content), 0);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, loading]);

    const startResize = (e: React.MouseEvent) => {
        e.preventDefault();
        setIsResizing(true);
        resizeStartY.current = e.clientY;
        resizeStartH.current = panelHeight;
    };

    useEffect(() => {
        if (!isResizing) return;
        const onMove = (e: MouseEvent) => {
            const delta = resizeStartY.current - e.clientY;
            setPanelHeight(Math.max(280, Math.min(800, resizeStartH.current + delta)));
        };
        const onUp = () => setIsResizing(false);
        window.addEventListener('mousemove', onMove);
        window.addEventListener('mouseup', onUp);
        return () => { window.removeEventListener('mousemove', onMove); window.removeEventListener('mouseup', onUp); };
    }, [isResizing]);

    const handleSend = async () => {

```
