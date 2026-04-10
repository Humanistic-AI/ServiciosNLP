import { useState } from 'react'
import type { ServiceType, HistoryItem } from '../types'
import { submitWordCount, submitClassification, checkStatus } from '../services/api'

interface Props {
  onSubmit: (item: HistoryItem) => void
}

export default function TextPanel({ onSubmit }: Props) {
  const [service, setService] = useState<ServiceType>('word_count')
  const [text, setText] = useState('')
  const [categories, setCategories] = useState<string[]>([])
  const [categoryInput, setCategoryInput] = useState('')
  const [examples, setExamples] = useState('')

  function handleCategoryKeyDown(e: React.KeyboardEvent<HTMLInputElement>) {
    if (e.key === 'Enter' && categoryInput.trim() !== '') {
      e.preventDefault()
      setCategories(prev => [...prev, categoryInput.trim()])
      setCategoryInput('')
    }
  }

  function removeCategory(index: number) {
    setCategories(prev => prev.filter((_, i) => i !== index))
  }

  function pollStatus(requestId: string, submittedService: ServiceType, submittedText: string, createdAt: string) {
    const interval = setInterval(async () => {
      const updated = await checkStatus(submittedService, requestId)
      if (updated.status === 'completed' || updated.status === 'failed') {
        clearInterval(interval)
        onSubmit({
          request_id: requestId,
          service: submittedService,
          text: submittedText,
          status: updated.status,
          createdAt,
        })
      }
    }, 3000)
  }

  async function handleSubmit() {
    if (text.trim() === '') return

    const createdAt = new Date().toLocaleString('es-MX')
    const submittedText = text
    const submittedService = service

    const job =
      submittedService === 'word_count'
        ? await submitWordCount(submittedText)
        : await submitClassification(submittedText, categories, examples)

    onSubmit({
      request_id: job.request_id,
      service: submittedService,
      text: submittedText,
      status: 'processing',
      createdAt,
    })

    setText('')
    setCategories([])
    setCategoryInput('')
    setExamples('')

    pollStatus(job.request_id, submittedService, submittedText, createdAt)
  }

  return (
    <div className="bg-white border border-gray-200 rounded-xl p-5 flex flex-col gap-4">
      <p className="text-xs font-medium text-gray-400 uppercase tracking-wide">
        Panel de trabajo
      </p>

      <div className="flex gap-2">
        <button
          onClick={() => setService('word_count')}
          className={`text-sm px-3 py-1.5 rounded-lg border transition-colors ${
            service === 'word_count'
              ? 'bg-green-50 border-green-300 text-green-800'
              : 'border-gray-200 text-gray-500 hover:border-gray-300'
          }`}
        >
          Frecuencia de palabras
        </button>
        <button
          onClick={() => setService('sentence_classification')}
          className={`text-sm px-3 py-1.5 rounded-lg border transition-colors ${
            service === 'sentence_classification'
              ? 'bg-purple-50 border-purple-300 text-purple-800'
              : 'border-gray-200 text-gray-500 hover:border-gray-300'
          }`}
        >
          Clasificación de oraciones
        </button>
      </div>

      <textarea
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="Pega tu texto aquí..."
        rows={6}
        className="w-full border border-gray-200 rounded-lg p-3 text-sm text-gray-700 resize-none focus:outline-none focus:ring-1 focus:ring-gray-300"
      />

      {service === 'sentence_classification' && (
        <div className="flex flex-col gap-3">
          <div>
            <label className="text-xs text-gray-500 mb-1 block">
              Categorías — presiona Enter para agregar
            </label>
            <div className="flex flex-wrap gap-1.5 border border-gray-200 rounded-lg p-2 min-h-[42px]">
              {categories.map((cat, i) => (
                <span
                  key={i}
                  className="flex items-center gap-1 bg-purple-100 text-purple-800 text-xs px-2 py-0.5 rounded-full"
                >
                  {cat}
                  <button
                    onClick={() => removeCategory(i)}
                    className="text-purple-500 hover:text-purple-800"
                  >
                    ✕
                  </button>
                </span>
              ))}
              <input
                value={categoryInput}
                onChange={e => setCategoryInput(e.target.value)}
                onKeyDown={handleCategoryKeyDown}
                placeholder={categories.length === 0 ? 'ej. positivo, negativo...' : ''}
                className="text-sm text-gray-700 flex-1 min-w-[120px] focus:outline-none"
              />
            </div>
          </div>

          <div>
            <label className="text-xs text-gray-500 mb-1 block">
              Ejemplos
            </label>
            <textarea
              value={examples}
              onChange={e => setExamples(e.target.value)}
              placeholder="Escribe ejemplos para guiar la clasificación..."
              rows={3}
              className="w-full border border-gray-200 rounded-lg p-3 text-sm text-gray-700 resize-none focus:outline-none focus:ring-1 focus:ring-gray-300"
            />
          </div>
        </div>
      )}

      <button
        onClick={handleSubmit}
        disabled={text.trim() === ''}
        className="self-start bg-gray-900 text-white text-sm px-4 py-2 rounded-lg hover:bg-gray-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
      >
        Analizar
      </button>
    </div>
  )
}