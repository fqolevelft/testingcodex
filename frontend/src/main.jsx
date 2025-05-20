import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import App from './App'
import SuperAdminLogin from './pages/SuperAdminLogin'
import AdminLogin from './pages/AdminLogin'

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path="/superadmin" element={<SuperAdminLogin />} />
      <Route path="/admin" element={<AdminLogin />} />
      <Route path="*" element={<App />} />
    </Routes>
  </BrowserRouter>
)
