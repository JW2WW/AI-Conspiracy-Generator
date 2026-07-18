interface EventInputProps {
  value: string
  onChange: (value: string) => void
  onSubmit: () => void
  loading: boolean
}

const EXAMPLES = [
  'Why did the neighborhood power go out?',
  'Why was my package delayed?',
  'Why is my internet slow?',
  'Why was traffic stopped?',
  'Why did the office coffee machine stop working?',
]

export default function EventInput({ value, onChange, onSubmit, loading }: EventInputProps) {
  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault()
      onSubmit()
    }
  }

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault()
        onSubmit()
      }}
      className="space-y-4"
    >
      <div>
        <label htmlFor="event" className="block text-sm font-medium text-gray-300">
          What happened?
        </label>
        <textarea
          id="event"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Why did the neighborhood power go out?"
          rows={3}
          className="mt-2 w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-conspiracy-500 focus:outline-none focus:ring-1 focus:ring-conspiracy-500"
        />
      </div>

      <div className="flex flex-wrap gap-2">
        {EXAMPLES.map((example) => (
          <button
            key={example}
            type="button"
            onClick={() => onChange(example)}
            className="rounded-full border border-gray-700 px-3 py-1 text-xs text-gray-400 transition hover:border-conspiracy-600 hover:text-conspiracy-300"
          >
            {example}
          </button>
        ))}
      </div>

      <button
        type="submit"
        disabled={loading || value.trim().length < 3}
        className="w-full rounded-lg bg-conspiracy-600 px-6 py-3 font-semibold text-white transition hover:bg-conspiracy-500 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? 'Generating Conspiracy...' : 'Generate Conspiracy'}
      </button>
      <p className="text-center text-xs text-gray-500">Press Ctrl+Enter to submit</p>
    </form>
  )
}
