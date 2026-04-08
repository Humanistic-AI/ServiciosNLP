import { useState } from 'react'
import type { HistoryItem } from './types'
import HistoryPanel from './components/HistoryPanel'

export default function App() {
  const [history, setHistory] = useState<HistoryItem[]>([])

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-5xl mx-auto">
        <div className="mb-6">
          <h1 className="text-2xl font-medium text-gray-900">ServiciosNLP</h1>
          <p className="text-sm text-gray-500">
            Herramientas de procesamiento de lenguaje natural para investigadores
          </p>
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-[1fr_360px] gap-4">
          <div className="bg-white border border-gray-200 rounded-xl p-5">
            <p className="text-sm text-gray-400">Panel de trabajo — próximamente</p>
          </div>
          <HistoryPanel items={history} />
        </div>
      </div>
    </div>
  )
}