import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

interface ChatSummary {
  id: number
  name: string | null
  chat_type: string
}

export default function DashboardPage() {
  const [chats, setChats] = useState<ChatSummary[]>([])

  useEffect(() => {
    axios.get<ChatSummary[]>('http://localhost:8000/api/v1/chats').then((response) => setChats(response.data))
  }, [])

  return (
    <div className="mx-auto flex min-h-screen max-w-6xl flex-col px-6 py-10">
      <header className="flex items-center justify-between rounded-2xl border border-slate-800 bg-slate-900/80 p-6">
        <div>
          <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">Real-Time Chat</p>
          <h1 className="text-3xl font-semibold">Welcome to the collaboration hub</h1>
        </div>
        <div className="flex gap-3">
          <Link to="/login" className="rounded-lg border border-slate-700 px-4 py-2">Login</Link>
          <Link to="/register" className="rounded-lg bg-cyan-600 px-4 py-2">Register</Link>
        </div>
      </header>

      <section className="mt-8 grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
        <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Chat rooms</h2>
          <div className="mt-4 space-y-3">
            {chats.map((chat) => (
              <div key={chat.id} className="rounded-xl border border-slate-800 bg-slate-950 p-4">
                <div className="font-medium">{chat.name ?? 'Untitled chat'}</div>
                <div className="mt-1 text-sm text-slate-400">{chat.chat_type}</div>
              </div>
            ))}
          </div>
        </div>
        <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Project Highlights</h2>
          <ul className="mt-4 space-y-3 text-sm text-slate-400">
            <li>• JWT authentication and refresh tokens</li>
            <li>• WebSocket-based real-time messaging</li>
            <li>• Redis-backed scaling strategy</li>
            <li>• Modular, production-ready architecture</li>
          </ul>
        </div>
      </section>
    </div>
  )
}
