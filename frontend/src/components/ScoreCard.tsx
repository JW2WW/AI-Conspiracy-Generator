import type { ScoreBreakdown } from '../types'

interface ScoreCardProps {
  scores: ScoreBreakdown
}

function ScoreBar({ label, value, color }: { label: string; value: number; color: string }) {
  return (
    <div>
      <div className="mb-1 flex justify-between text-sm">
        <span className="text-gray-300">{label}</span>
        <span className="font-mono text-white">{value}/10</span>
      </div>
      <div className="h-2 overflow-hidden rounded-full bg-gray-800">
        <div
          className={`h-full rounded-full transition-all duration-700 ${color}`}
          style={{ width: `${value * 10}%` }}
        />
      </div>
    </div>
  )
}

export default function ScoreCard({ scores }: ScoreCardProps) {
  return (
    <div className="card agent-judge">
      <h3 className="mb-4 font-display text-lg font-bold text-amber-400">Judge Agent Scores</h3>
      <div className="space-y-3">
        <ScoreBar label="Creativity" value={scores.creativity} color="bg-amber-500" />
        <ScoreBar label="Plausibility" value={scores.plausibility} color="bg-red-500" />
        <ScoreBar label="Evidence" value={scores.evidence} color="bg-blue-500" />
        <ScoreBar label="Comedy" value={scores.comedy} color="bg-conspiracy-500" />
      </div>
      {scores.commentary && (
        <p className="mt-4 text-sm italic text-gray-400">{scores.commentary}</p>
      )}
    </div>
  )
}
