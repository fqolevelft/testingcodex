import React from 'react'
import LoginForm from '../components/LoginForm'

export default function SuperAdminLogin() {
  const submit = creds => {
    fetch('/api/superadmin/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(creds) })
      .then(r => r.json())
      .then(console.log)
  }
  return (
    <div>
      <h2>Super Admin Login</h2>
      <LoginForm onSubmit={submit} />
    </div>
  )
}
