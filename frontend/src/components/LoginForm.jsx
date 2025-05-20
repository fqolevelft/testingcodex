import React, { useState } from 'react'

export default function LoginForm({ onSubmit }) {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  return (
    <form onSubmit={e => { e.preventDefault(); onSubmit({ email, password }) }}>
      <div>
        <label>Email</label>
        <input value={email} onChange={e => setEmail(e.target.value)} />
      </div>
      <div>
        <label>Password</label>
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
      </div>
      <button type="submit">Login</button>
    </form>
  )
}
