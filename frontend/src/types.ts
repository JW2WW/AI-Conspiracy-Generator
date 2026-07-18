export type GameMode =
  'classic' | 'xfiles' | 'corporate' | 'time_traveler' | 'ancient' | 'debate' | 'escalation'

export interface GameModeInfo {
  id: GameMode
  name: string
  description: string
}

export interface DebateRound {
  round_number: number
  theory: string
  investigation: string
}

export interface ScoreBreakdown {
  creativity: number
  plausibility: number
  evidence: number
  comedy: number
  commentary: string
}

export interface ConspiracyResponse {
  id: string
  event: string
  game_mode: GameMode
  evidence: string
  theory: string
  investigation: string
  debate_rounds: DebateRound[]
  scores: ScoreBreakdown
  reality_restored: string
  created_at?: string
  metadata: Record<string, unknown>
}

export interface ConspiracyRequest {
  event: string
  game_mode: GameMode
  rounds?: number
}
