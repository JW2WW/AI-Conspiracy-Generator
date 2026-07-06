import type { ConspiracyResponse } from '../types'
import DebateRounds from './DebateRounds'
import ScoreCard from './ScoreCard'

interface ResultsDisplayProps {
  result: ConspiracyResponse
}

export default function ResultsDisplay({ result }: ResultsDisplayProps) {
  return (
    <div className="space-y-6">
      <div className="card">
        <div className="text-sm text-gray-400">Investigating</div>
        <h2 className="mt-1 font-display text-2xl font-bold text-white">{result.event}</h2>
      </div>

      <div className="card agent-theory">
        <h3 className="mb-3 font-display text-lg font-bold text-conspiracy-400">Evidence Agent</h3>
        <p className="whitespace-pre-wrap text-gray-300">{result.evidence}</p>
      </div>

      {result.debate_rounds.length <= 1 && (
        <>
          <div className="card agent-theory">
            <h3 className="mb-3 font-display text-lg font-bold text-conspiracy-400">Theory Agent</h3>
            <p className="whitespace-pre-wrap text-gray-300">{result.theory}</p>
          </div>

          <div className="card agent-investigator">
            <h3 className="mb-3 font-display text-lg font-bold text-emerald-400">Investigator Agent</h3>
            <p className="whitespace-pre-wrap text-gray-300">{result.investigation}</p>
          </div>
        </>
      )}

      <DebateRounds rounds={result.debate_rounds} />

      <ScoreCard scores={result.scores} />

      <div className="card agent-reality">
        <h3 className="mb-3 font-display text-lg font-bold text-blue-400">Reality Restored™</h3>
        <p className="whitespace-pre-wrap text-gray-300">{result.reality_restored}</p>
      </div>
    </div>
  )
}
