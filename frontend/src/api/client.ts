import type { ConspiracyRequest, ConspiracyResponse, GameModeInfo } from '../types'

const API_BASE = import.meta.env.VITE_API_URL || '/api'

async function fetchJson<T>(url: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${url}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!response.ok) {
    const error = await response.json().catch(() => null)
    const detail =
      (error && typeof error === 'object' && 'detail' in error && String(error.detail)) ||
      (response.status === 504
        ? 'Request timed out waiting for the model. Try a faster model (e.g. gemini-2.5-flash) or fewer rounds.'
        : `Request failed (HTTP ${response.status})`)
    throw new Error(detail)
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
