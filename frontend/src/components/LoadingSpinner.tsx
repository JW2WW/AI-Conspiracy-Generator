interface LoadingSpinnerProps {
  message?: string
}

export default function LoadingSpinner({ message = 'Agents are conspiring...' }: LoadingSpinnerProps) {
  return (
    <div className="flex flex-col items-center justify-center gap-4 py-16">
      <div className="relative h-16 w-16">
        <div className="absolute inset-0 animate-spin rounded-full border-4 border-conspiracy-900 border-t-conspiracy-500" />
        <div className="absolute inset-2 animate-pulse rounded-full bg-conspiracy-900/50" />
      </div>
      <p className="animate-pulse text-conspiracy-300">{message}</p>
    </div>
  )
}
