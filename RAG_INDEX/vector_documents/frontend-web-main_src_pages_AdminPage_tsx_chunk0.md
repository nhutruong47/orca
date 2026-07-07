# Knowledge Document: AdminPage.tsx (Chunk 1/16)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/AdminPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "report",
    "dashboard",
    "admin",
    "workspace",
    "production",
    "factory",
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
import { useEffect, useMemo, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import {
  Activity,
  AlertTriangle,
  Building2,
  CreditCard,
  DollarSign,
  Download,
  FileText,
  Lock,
  MoreHorizontal,
  Plus,
  RotateCcw,
  Search,
  ServerCrash,
  ShieldCheck,
  Users
} from 'lucide-react';
import {
  Area,
  AreaChart,
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis
} from 'recharts';

import { useAuth } from '../context/AuthContext';
import { adminService } from '../services/adminService';
import type { AdminOverview, AdminPayment, AdminTeam, AdminUser } from '../types/types';
import './AdminPage.css';

type AdminSection =
  | 'overview'
  | 'workspace_requests'
  | 'companies'
  | 'users'
  | 'subscriptions'
  | 'payments'
  | 'reports'
  | 'logs';

const money = (value: number) =>
  new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND', maximumFractionDigits: 0 }).format(value);

const number = (value: number) => new Intl.NumberFormat('vi-VN').format(value);

const parseDateInput = (value: string, endOfDay = false) => {
  const date = new Date(`${value}T${endOfDay ? '23:59:59' : '00:00:00'}`);
  return Number.isNaN(date.getTime()) ? new Date() : date;
};


const sidebarModules: Array<{ id: AdminSection; label: string; icon: React.ElementType }> = [
  { id: 'overview', label: 'Tổng quan & Phân tích', icon: Activity },
  { id: 'workspace_requests', label: 'Yêu cầu mở xưởng', icon: ShieldCheck },
  { id: 'companies', label: 'Quản lý doanh nghiệp', icon: Building2 },
  { id: 'users', label: 'Quản lý người dùng', icon: Users },
  { id: 'subscriptions', label: 'Gói dịch vụ', icon: CreditCard },
  { id: 'payments', label: 'Thanh toán & doanh thu', icon: DollarSign },
  { id: 'reports', label: 'Báo cáo thống kê', icon: FileText },
  { id: 'logs', label: 'Nhật ký hệ thống', icon: ServerCrash },
];

type KpiTone = 'blue' | 'green' | 'amber' | 'violet' | 'rose';

type KpiItem = {
  label: string;
  value: string;
  detail: string;
  icon: React.ElementType;
  tone: KpiTone;
  trend?: 'up' | 'down';
};

const emptyOverview: AdminOverview = {
  totalUsers: 0,
  adminUsers: 0,
  memberUsers: 0,
  newUsersThisMonth: 0,
  newUsersPreviousMonth: 0,
  totalTeams: 0,
  publishedTeams: 0,
  newTeamsThisMonth: 0,
  newTeamsPreviousMonth: 0,
  totalGoals: 0,
  activeGoals: 0,

```
