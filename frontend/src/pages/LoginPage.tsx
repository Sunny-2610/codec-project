import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

export default function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const onSubmit = async (event: React.FormEvent) => {
    event.preventDefault()
    const response = await axios.post('http://localhost:8000/api/v1/auth/login', { email, password })
    localStorage.setItem('access_token', response.data.access_token)
    navigate('/')
  }

  return (
    <div className="flex min-h-screen items-center justify-center px-4">
      <form onSubmit={onSubmit} className="w-full max-w-md rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-xl">
        <h1 className="text-2xl font-semibold">Welcome back</h1>
        <p className="mt-2 text-sm text-slate-400">Sign in to your workspace</p>
        <div className="mt-6 space-y-4">
          <input value={email} onChange={(e) => setEmail(e.target.value)} className="w-full rounded-lg border border-slate-700 bg-slate-950 px-4 py-3" placeholder="Email" />
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="w-full rounded-lg border border-slate-700 bg-slate-950 px-4 py-3" placeholder="Password" />
          <button className="w-full rounded-lg bg-cyan-600 px-4 py-3 font-semibold hover:bg-cyan-500">Login</button>
        </div>
      </form>
    </div>
  )
}
