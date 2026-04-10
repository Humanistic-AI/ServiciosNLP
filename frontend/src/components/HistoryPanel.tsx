import type { HistoryItem } from '../types'
import { getResultsUrl } from '../services/api'

interface Props {
  items: HistoryItem[]
}

function ServiceBadge({ service }: { service: HistoryItem['service'] }) {
  const styles = {
    word_count: 'bg-green-100 text-green-800',
    sentence_classification: 'bg-purple-100 text-purple-800',
  }
  const labels = {
    word_count: 'Frecuencia de palabras',
    sentence_classification: 'Clasificación de oraciones',
  }
  return (
    <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${styles[service]}`}>
      {labels[service]}
    </span>
  )
}

function StatusIndicator({ status }: { status: HistoryItem['status'] }) {
  if (status === 'processing') {
    return <span className="text-xs text-amber-600">Procesando...</span>
  }
  if (status === 'failed') {
    return <span className="text-xs text-red-600">Error</span>
  }
  return <span className="text-xs text-green-600">Completado</span>
}

export default function HistoryPanel({ items }: Props) {
  if (items.length === 0) {
    return (
      <div className="bg-white border border-gray-200 rounded-xl p-5">
        <p className="text-xs font-medium text-gray-400 uppercase tracking-wide mb-4">
          Historial de análisis
        </p>
        <p className="text-sm text-gray-400 text-center py-8">
          Aún no hay análisis realizados
        </p>
      </div>
    )
  }

  return (
    <div className="bg-white border border-gray-200 rounded-xl p-5">
      <p className="text-xs font-medium text-gray-400 uppercase tracking-wide mb-4">
        Historial de análisis
      </p>
      <ul className="divide-y divide-gray-100">
        {items.map((item) => (
          <li key={item.request_id} className="py-3 first:pt-0 last:pb-0">
            <div className="flex flex-col gap-1.5">
              <ServiceBadge service={item.service} />
              <p className="text-sm text-gray-700 line-clamp-2">{item.text}</p>
              <div className="flex justify-between items-center">
                <StatusIndicator status={item.status} />
                <div className="flex gap-3">
                  {item.status === 'completed' ? (
                    <a
                      href={getResultsUrl(item.service, item.request_id)}
                      className="text-xs text-blue-600"
                      download
                    >
                      Descargar
                    </a>
                  ) : (
                    <span className="text-xs text-gray-300">Descargar</span>
                  )}
                </div>
              </div>
              <p className="text-xs text-gray-400">{item.createdAt}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}