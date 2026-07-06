import type { DebateRound } from '../types'

interface DebateRoundsProps {
  rounds: DebateRound[]
}

export default function DebateRounds({ rounds }: DebateRoundsProps) {
  if (rounds.length <= 1) return null

  return (
    <div className="space-y-4">
      <h3 className="font-display text-lg font-bold text-white">Debate Rounds</h3>
      {rounds.map((round) => (
        <div key={round.round_number} className="card">
          <div className="mb-3 text-sm font-medium text-conspiracy-400">
            Round {round.round_number}
          </div>
          <div className="grid gap-4 md:grid-cols-2">
            <div className="agent-theory rounded-lg bg-gray-950/50 p-4">
              <div className="mb-2 text-xs font-semibold uppercase tracking-wider text-conspiracy-400">
                Theory Agent
              </div>
              <p className="whitespace-pre-wrap text-sm text-gray-300">{round.theory}</p>
            </div>
            <div className="agent-investigator rounded-lg bg-gray-950/50 p-4">
              <div className="mb-2 text-xs font-semibold uppercase tracking-wider text-emerald-400">
                Investigator Agent
              </div>
              <p className="whitespace-pre-wrap text-sm text-gray-300">{round.investigation}</p>
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}
