import { useCallback, useEffect, useState } from 'react'
import { generateConspiracy, getGameModes, getHealth } from './api/client'
import EventInput from './components/EventInput'
import GameModeSelector from './components/GameModeSelector'
import LoadingSpinner from './components/LoadingSpinner'
import ResultsDisplay from './components/ResultsDisplay'
import type { ConspiracyResponse, GameMode, GameModeInfo } from './types'

export default function App() {
  const [event, setEvent] = useState('')
  const [gameMode, setGameMode] = useState<GameMode>('classic')
  const [rounds, setRounds] = useState(3)
  const [modes, setModes] = useState<GameModeInfo[]>([])
  const [result, setResult] = useState<ConspiracyResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [llmProvider, setLlmProvider] = useState('mock')

  useEffect(() => {
    getGameModes().then(setModes).catch(console.error)
    getHealth().then((h) => setLlmProvider(h.llm_provider)).catch(console.error)
  }, [])

  const handleGenerate = useCallback(async () => {
    if (event.trim().length < 3) return
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await generateConspiracy({
        event: event.trim(),
        game_mode: gameMode,
        rounds,
      })
      setResult(response)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Generation failed')
    } finally {
      setLoading(false)
    }
  }, [event, gameMode, rounds])

  return (
    <div className="min-h-screen">
      <header className="border-b border-gray-800 bg-gray-900/50 backdrop-blur">
        <div className="mx-auto flex max-w-4xl items-center justify-between px-4 py-6">
          <div>
            <h1 className="font-display text-3xl font-bold text-white">
              AI Conspiracy Generator
            </h1>
            <p className="mt-1 text-sm text-gray-400">
              Where AI agents create absurd theories — then debunk them
            </p>
          </div>
          <div className="rounded-full border border-gray-700 px-3 py-1 text-xs text-gray-400">
            LLM: {llmProvider}
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-4xl px-4 py-8">
        <div className="card mb-8">
          <EventInput
            value={event}
            onChange={setEvent}
            onSubmit={handleGenerate}
            loading={loading}
          />

          {modes.length > 0 && (
            <div className="mt-6 border-t border-gray-800 pt-6">
              <GameModeSelector
                modes={modes}
                selected={gameMode}
                onChange={setGameMode}
                rounds={rounds}
                onRoundsChange={setRounds}
              />
            </div>
          )}
        </div>

        {error && (
          <div className="mb-8 rounded-lg border border-red-800 bg-red-950/50 p-4 text-red-300">
            {error}
          </div>
        )}

        {loading && <LoadingSpinner />}

        {result && !loading && <ResultsDisplay result={result} />}
      </main>

      <footer className="border-t border-gray-800 py-6 text-center text-xs text-gray-500">
        For entertainment and educational purposes only. All theories are fictional satire.
      </footer>
    </div>
  )
}
