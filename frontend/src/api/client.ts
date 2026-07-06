import type { ConspiracyRequest, ConspiracyResponse, GameModeInfo } from '../types'

const API_BASE = import.meta.env.VITE_API_URL || '/api'

async function fetchJson<T>(url: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${url}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Request failed' }))
    throw new Error(error.detail || `HTTP ${response.status}`)
  }
  return response.json()
}

export async function getGameModes(): Promise<GameModeInfo[]> {
  return fetchJson<GameModeInfo[]>('/modes')
}

export async function generateConspiracy(request: ConspiracyRequest): Promise<ConspiracyResponse> {
  return fetchJson<ConspiracyResponse>('/generate', {
    method: 'POST',
    body: JSON.stringify(request),
  })
}

export async function getHealth(): Promise<{ status: string; llm_provider: string }> {
  return fetchJson('/health')
}
