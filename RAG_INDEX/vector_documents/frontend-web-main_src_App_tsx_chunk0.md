# Knowledge Document: App.tsx (Chunk 1/2)

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
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, payment, dashboard

## Source Code Chunk
```tsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { ThemeProvider } from './context/ThemeContext';
import ProtectedRoute from './components/ProtectedRoute';
import Layout from './components/Layout';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import DashboardPage from './pages/DashboardPage';
import ProfilePage from './pages/ProfilePage';
import OAuth2Callback from './pages/OAuth2Callback';
import GroupsPage from './pages/GroupsPage';
import GroupDetailPage from './pages/GroupDetailPage';
import CreateTaskPage from './pages/CreateTaskPage';
import InviteAcceptPage from './pages/InviteAcceptPage';
import MarketplacePage from './pages/MarketplacePage';
import OrderManagementPage from './pages/OrderManagementPage';
import SettingsPage from './pages/SettingsPage';
import AdminPage from './pages/AdminPage';
import HomePage from './pages/HomePage';
import UpgradePlanPage from './pages/UpgradePlanPage';
import PaymentResultPage from './pages/PaymentResultPage';
import VnpayMockCheckoutPage from './pages/VnpayMockCheckoutPage';
import './App.css';

function App() {
    return (
        <BrowserRouter>
            <ThemeProvider>
                <AuthProvider>
                    <Routes>
                        <Route path="/login" element={<LoginPage />} />
                        <Route path="/register" element={<RegisterPage />} />
                        <Route path="/oauth2/callback" element={<OAuth2Callback />} />
                        <Route path="/invite" element={<InviteAcceptPage />} />
                        <Route path="/invite/:code" element={<InviteAcceptPage />} />

                        <Route element={<ProtectedRoute><Layout /></ProtectedRoute>}>
                            <Route path="/dashboard" element={<DashboardPage />} />
                            <Route path="/profile" element={<ProfilePage />} />
                            <Route path="/groups" element={<GroupsPage />} />
                            <Route path="/groups/:id" element={<GroupDetailPage />} />
                            <Route path="/groups/:id/create-task" element={<CreateTaskPage />} />
                            <Route path="/orders" element={<OrderManagementPage />} />

```
