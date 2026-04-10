export type ServiceType = 'word_count' | 'sentence_classification'

export type JobStatus = 'processing' | 'completed' | 'failed'

export interface HistoryItem {
  request_id: string
  service: ServiceType
  text: string
  status: JobStatus
  createdAt: string
}