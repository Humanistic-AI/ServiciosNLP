import axios from 'axios'
import type { ServiceType, JobStatus } from '../types'

const client = axios.create({
  baseURL: 'http://localhost:8000',
})

export interface JobResponse {
  request_id: string
  status: JobStatus
}

export async function submitWordCount(text: string): Promise<JobResponse> {
  const response = await client.post('/word-count', { text })
  return response.data
}

export async function submitClassification(
  text: string,
  categories: string[],
  examples: string
): Promise<JobResponse> {
  const response = await client.post('/sentence-classification', {
    text,
    categories,
    examples,
  })
  return response.data
}

export async function checkStatus(
  service: ServiceType,
  requestId: string
): Promise<JobResponse> {
  const base = service === 'word_count' ? '/word-count' : '/sentence-classification'
  const response = await client.get(`${base}/status/${requestId}`)
  return response.data
}

export function getResultsUrl(
  service: ServiceType,
  requestId: string
): string {
  const base = service === 'word_count' ? '/word-count' : '/sentence-classification'
  return `http://localhost:8000${base}/results/${requestId}`
}