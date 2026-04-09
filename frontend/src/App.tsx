import { useState } from 'react'
import type { HistoryItem } from './types'
import HistoryPanel from './components/HistoryPanel'
import TextPanel from './components/TextPanel'

export default function App() {
  const [history, setHistory] = useState<HistoryItem[]>([])

  function handleSubmit(item: HistoryItem) {
    setHistory(prev => {
      const exists = prev.find(i => i.request_id === item.request_id)
      if (exists) {
        return prev.map(i => i.request_id === item.request_id ? item : i)
      }
      return [item, ...prev]
    })
  }

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
          <TextPanel onSubmit={handleSubmit} />
          <HistoryPanel items={history} />
        </div>
      </div>
    </div>
  )
}