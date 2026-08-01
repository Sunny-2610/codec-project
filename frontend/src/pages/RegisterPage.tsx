import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

export default function RegisterPage() {
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const onSubmit = async (event: React.FormEvent) => {
    event.preventDefault()
    await axios.post('http://localhost:8000/api/v1/auth/register', { username, email, password })
    navigate('/login')
  }

  return (
    <div className="flex min-h-screen items-center justify-center px-4">
      <form onSubmit={onSubmit} className="w-full max-w-md rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-xl">
        <h1 className="text-2xl font-semibold">Create an account</h1>
        <div className="mt-6 space-y-4">
          <input value={username} onChange={(e) => setUsername(e.target.value)} className="w-full rounded-lg border border-slate-700 bg-slate-950 px-4 py-3" placeholder="Username" />
          <input value={email} onChange={(e) => setEmail(e.target.value)} className="w-full rounded-lg border border-slate-700 bg-slate-950 px-4 py-3" placeholder="Email" />
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="w-full rounded-lg border border-slate-700 bg-slate-950 px-4 py-3" placeholder="Password" />
          <button className="w-full rounded-lg bg-cyan-600 px-4 py-3 font-semibold hover:bg-cyan-500">Register</button>
        </div>
      </form>
    </div>
  )
}
