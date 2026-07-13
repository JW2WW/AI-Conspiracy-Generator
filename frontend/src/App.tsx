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
  const [modesLoading, setModesLoading] = useState(true)
  const [result, setResult] = useState<ConspiracyResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [llmProvider, setLlmProvider] = useState('mock')

  useEffect(() => {
    const abort = new AbortController()

    getGameModes()
      .then(setModes)
      .catch(console.error)
      .finally(() => {
        if (!abort.signal.aborted) setModesLoading(false)
      })

    getHealth()
      .then((h) => {
        if (!abort.signal.aborted) setLlmProvider(h.llm_provider)
      })
      .catch(console.error)

    return () => abort.abort()
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

  const handleStartOver = useCallback(() => {
    setResult(null)
    setError(null)
  }, [])

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
        {!result && (
          <div className="card mb-8">
            <EventInput
              value={event}
              onChange={setEvent}
              onSubmit={handleGenerate}
              loading={loading}
            />

            {modesLoading ? (
              <div className="mt-6 border-t border-gray-800 pt-6">
                <div className="h-4 w-24 animate-pulse rounded bg-gray-800" />
                <div className="mt-3 grid gap-3 sm:grid-cols-2">
                  {Array.from({ length: 4 }).map((_, i) => (
                    <div
                      key={i}
                      className="h-24 animate-pulse rounded-lg border border-gray-800 bg-gray-900"
                    />
                  ))}
                </div>
              </div>
            ) : (
              modes.length > 0 && (
                <div className="mt-6 border-t border-gray-800 pt-6">
                  <GameModeSelector
                    modes={modes}
                    selected={gameMode}
                    onChange={setGameMode}
                    rounds={rounds}
                    onRoundsChange={setRounds}
                  />
                </div>
              )
            )}
          </div>
        )}

        {error && (
          <div className="mb-8 rounded-lg border border-red-800 bg-red-950/50 p-4 text-red-300">
            {error}
          </div>
        )}

        {loading && <LoadingSpinner />}

        {result && !loading && (
          <>
            <ResultsDisplay result={result} />
            <div className="mt-8 text-center">
              <button
                type="button"
                onClick={handleStartOver}
                className="rounded-lg border border-gray-700 px-6 py-3 font-semibold text-gray-300 transition hover:border-conspiracy-600 hover:text-conspiracy-300"
              >
                Generate Another Conspiracy
              </button>
            </div>
          </>
        )}
      </main>

      <footer className="border-t border-gray-800 py-6 text-center text-xs text-gray-500">
        For entertainment and educational purposes only. All theories are fictional satire.
      </footer>
    </div>
  )
}