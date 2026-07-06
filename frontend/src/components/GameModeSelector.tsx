import type { GameMode, GameModeInfo } from '../types'

interface GameModeSelectorProps {
  modes: GameModeInfo[]
  selected: GameMode
  onChange: (mode: GameMode) => void
  rounds: number
  onRoundsChange: (rounds: number) => void
}

export default function GameModeSelector({
  modes,
  selected,
  onChange,
  rounds,
  onRoundsChange,
}: GameModeSelectorProps) {
  const showRounds = selected === 'debate' || selected === 'escalation'

  return (
    <div className="space-y-4">
      <label className="block text-sm font-medium text-gray-300">Game Mode</label>
      <div className="grid gap-3 sm:grid-cols-2">
        {modes.map((mode) => (
          <button
            key={mode.id}
            type="button"
            onClick={() => onChange(mode.id)}
            className={`rounded-lg border p-4 text-left transition-all ${
              selected === mode.id
                ? 'border-conspiracy-500 bg-conspiracy-950/50 ring-1 ring-conspiracy-500'
                : 'border-gray-800 bg-gray-900 hover:border-gray-700'
            }`}
          >
            <div className="font-medium text-white">{mode.name}</div>
            <div className="mt-1 text-sm text-gray-400">{mode.description}</div>
          </button>
        ))}
      </div>

      {showRounds && (
        <div>
          <label htmlFor="rounds" className="block text-sm font-medium text-gray-300">
            Debate Rounds ({rounds})
          </label>
          <input
            id="rounds"
            type="range"
            min={1}
            max={5}
            value={rounds}
            onChange={(e) => onRoundsChange(Number(e.target.value))}
            className="mt-2 w-full accent-conspiracy-500"
          />
        </div>
      )}
    </div>
  )
}
