# AI Conspiracy Generator

An AI-powered comedy platform where one AI agent creates increasingly ridiculous conspiracy theories while another AI agent investigates, fact-checks, and debunks them.

> **The goal is not to promote misinformation.**
>
> The goal is to demonstrate how easily narratives can be constructed around incomplete information while using humor, critical thinking, and adversarial AI reasoning to separate fact from fiction.

---

# Overview

AI Conspiracy Generator is a multi-agent AI system that turns ordinary events into absurd conspiracy theories and then systematically dismantles them.

Users provide a simple event:

> Why did the neighborhood power go out?

One AI agent creates increasingly elaborate theories.

Another AI agent investigates the evidence.

A third agent may score the theories for creativity, plausibility, and comedy.

The result is a humorous demonstration of how narratives, assumptions, and speculation can quickly diverge from reality.

---

# Screenshots

> *Screenshots coming soon — contributions welcome!*

---

# Why This Project Exists

Humans are naturally wired to seek patterns and explanations.

Given limited information, it is surprisingly easy to construct convincing stories that appear logical but have little connection to reality.

AI Conspiracy Generator uses humor to illustrate:

- Confirmation bias
- Narrative construction
- Critical thinking
- Evidence evaluation
- Fact checking
- Adversarial reasoning

The platform is designed as entertainment first and educational second.

---

# Core Concept

Input:

```text
Why did the neighborhood power go out?
```

---

## Theory Agent

Creates a conspiracy theory.

```text
The outage coincided with a full moon,
three missing cats, and a delivery truck
from an unknown company.

This strongly suggests an underground
squirrel organization is testing
electromagnetic acorn technology.
```

---

## Investigator Agent

Examines the evidence.

```text
Utility company records show
a contractor accidentally struck
a transformer with a backhoe
at 2:17 PM.

No evidence of electromagnetic
acorns was discovered.
```

---

## Judge Agent

Scores the theory.

```text
Creativity: 10/10

Plausibility: 0/10

Evidence: 0/10

Comedy: 10/10
```

---

# Key Features

## Multi-Agent AI System

Multiple AI agents with competing objectives.

### Theory Agent

Responsible for:

- Creating theories
- Connecting unrelated events
- Escalating absurdity
- Defending its claims

---

### Investigator Agent

Responsible for:

- Fact checking
- Evidence review
- Logical analysis
- Debunking claims

---

### Judge Agent

Responsible for scoring:

- Creativity
- Plausibility
- Evidence quality
- Entertainment value

---

### Evidence Agent (Optional)

Responsible for:

- Gathering facts
- Finding contradictions
- Building timelines
- Supporting investigations

---

# Game Modes

## Classic Conspiracy Mode

Create increasingly elaborate conspiracy theories.

---

## X-Files Mode

Every event must involve:

- Aliens
- Government coverups
- Secret facilities
- Paranormal activity

---

## Corporate Conspiracy Mode

Every event is blamed on a fictional mega-corporation.

Example:

```text
The outage was caused by
Global Acorn Dynamics Corporation
to test next-generation squirrel
communication infrastructure.
```

---

## Time Traveler Mode

All events are explained through timeline manipulation.

---

## Ancient Civilization Mode

Everything traces back to:

- Lost civilizations
- Ancient technology
- Mysterious artifacts

---

## AI Debate Mode

Theory Agent and Investigator Agent engage in multiple rounds.

Example:

### Round 1

```text
Squirrels caused the outage.
```

### Round 2

```text
The squirrels are organized.
```

### Round 3

```text
The squirrels report to an
interdimensional acorn council.
```

### Investigator

```text
The outage was caused by
equipment damage.
```

---

## Escalation Mode

Each round must become more absurd than the previous one.

The system rewards creativity while the Investigator attempts to restore reality.

---

# Reality Restored™

After the debate concludes, the platform reveals the most likely real explanation.

Example:

```text
Actual Cause

A contractor accidentally struck
a power transformer while digging.

Case Closed.
```

---

# Example Scenarios

## Power Outage

```text
Why did the power go out?
```

---

## Missing Package

```text
Why was my package delayed?
```

---

## Slow Internet

```text
Why is my internet slow?
```

---

## Traffic Jam

```text
Why was traffic stopped?
```

---

## Broken Coffee Machine

```text
Why did the office coffee machine stop working?
```

---

# Educational Goals

Although designed as comedy, the platform demonstrates:

- Confirmation bias
- Logical fallacies
- Correlation vs causation
- Evidence evaluation
- Critical thinking
- Fact verification

The project encourages users to question assumptions and examine evidence.

---

# Architecture

```text
User Input

      │
      ▼
Theory Agent
      │
      ▼
Evidence Agent
      │
      ▼
Investigator Agent
      │
      ▼
Judge Agent
      │
      ▼
Reality Restored Engine
      │
      ▼
Final Results
```

---

# Technology Stack

## Backend

- Python 3.12+
- FastAPI
- PostgreSQL 16
- Redis 7

---

## AI

- OpenAI GPT Models
- Anthropic Claude
- Local LLM Support (mock provider)

---

## Agent Framework

- Multi-Agent Orchestration
- Prompt Chaining
- Reasoning Pipelines

---

## Frontend

- React 18
- TypeScript
- TailwindCSS
- Vite

---

## Deployment

- Docker
- Docker Compose
- Linux

---

# Setup

## Prerequisites

- **Docker & Docker Compose** (recommended) — for running the full stack with one command
- **Node.js 20+** — for local frontend development
- **Python 3.12+** — for local backend development
- **PostgreSQL 16** and **Redis 7** — required when running the backend outside Docker

---

## Quick Start (Docker Compose)

The fastest way to run the entire platform:

```bash
# Clone the repository
git clone https://github.com/JW2WW/AI-Conspiracy-Generator.git
cd AI-Conspiracy-Generator

# Copy environment config (mock mode works without API keys)
cp .env.example .env

# Build and start all services
docker compose up --build
```

Once running:

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| API | http://localhost:8000 |
| API Docs (Swagger) | http://localhost:8000/docs |

Enter an event (e.g. *"Why did the neighborhood power go out?"*), pick a game mode, and click **Generate Conspiracy**.

To stop:

```bash
docker compose down
```

---

## Configuration

Copy `.env.example` to `.env` and adjust as needed:

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_PROVIDER` | `mock` | LLM backend: `mock`, `openai`, or `anthropic` |
| `OPENAI_API_KEY` | — | Required when `LLM_PROVIDER=openai` |
| `ANTHROPIC_API_KEY` | — | Required when `LLM_PROVIDER=anthropic` |
| `DATABASE_URL` | `postgresql+asyncpg://conspiracy:conspiracy@localhost:5432/conspiracy` | PostgreSQL connection string |
| `REDIS_URL` | `redis://localhost:6379/0` | Redis connection string |
| `POSTGRES_USER` | `conspiracy` | PostgreSQL user (Docker only) |
| `POSTGRES_PASSWORD` | `conspiracy` | PostgreSQL password (Docker only) |
| `POSTGRES_DB` | `conspiracy` | PostgreSQL database name (Docker only) |

**Mock mode** works out of the box with no API keys — it uses template-based responses for demo and development. Set `LLM_PROVIDER=openai` or `anthropic` and provide the corresponding API key for live LLM-generated theories.

---

## Local Development

### Backend

```bash
cd backend

# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Start PostgreSQL and Redis (or use Docker for just these services)
docker compose up postgres redis -d

# Run the API server
export DATABASE_URL=postgresql+asyncpg://conspiracy:conspiracy@localhost:5432/conspiracy
export REDIS_URL=redis://localhost:6379/0
export LLM_PROVIDER=mock
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API available at http://localhost:8000 — interactive docs at http://localhost:8000/docs.

### Frontend

```bash
cd frontend

npm install
npm run dev
```

Dev server runs at http://localhost:5173 and proxies `/api` requests to the backend on port 8000.

### Production build (frontend only)

```bash
cd frontend
npm run build
npm run preview
```

---

# Testing

## Backend tests

```bash
cd backend
pip install -r requirements.txt
pytest tests/ -v
```

Tests use:
- `pytest` and `pytest-asyncio` for async test support
- `fakeredis` to mock Redis without a running server
- The `MockProvider` which works without any API keys

### Writing tests

Tests are located in `backend/tests/` and follow these conventions:

- `test_llm.py` — tests for LLM providers and score parsing
- `test_agents.py` — tests for individual agent classes
- `test_orchestrator.py` — tests for the full orchestration pipeline
- `conftest.py` — shared fixtures (Redis mocking)

## Frontend linting

```bash
cd frontend
npm run lint       # ESLint
npm run format     # Prettier
```

---

# Linting & Formatting

## Backend (Python)

This project uses [ruff](https://docs.astral.sh/ruff/) for both linting and formatting:

```bash
cd backend
ruff check .       # Lint
ruff format .      # Format
```

Configuration is in `backend/pyproject.toml`.

## Frontend (TypeScript/React)

This project uses ESLint + Prettier:

```bash
cd frontend
npm run lint       # ESLint
npm run format     # Prettier
```

## Pre-commit hooks

Install pre-commit to automatically lint/format on every commit:

```bash
pip install pre-commit
pre-commit install
```

Configuration is in `.pre-commit-config.yaml`.

## CI

Every push and pull request to `main` is checked via GitHub Actions (see `.github/workflows/ci.yml`):

- Backend lint (`ruff check`)
- Backend tests (`pytest`)
- Frontend lint (`eslint`)
- Frontend formatting (`prettier --check`)
- Frontend build (`tsc && vite build`)
- Docker build (`docker compose build`)

---

# API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/health` | Health check and active LLM provider |
| `GET` | `/api/modes` | List available game modes |
| `POST` | `/api/generate` | Run the full agent pipeline |
| `GET` | `/api/sessions/{id}` | Retrieve a past generation session |

### Example request

```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "event": "Why did the neighborhood power go out?",
    "game_mode": "classic",
    "rounds": 1
  }'
```

### Game modes

| Mode | Value | Description |
|------|-------|-------------|
| Classic Conspiracy | `classic` | Elaborate theories with escalating absurdity |
| X-Files | `xfiles` | Aliens, coverups, paranormal activity |
| Corporate Conspiracy | `corporate` | Blame a fictional mega-corporation |
| Time Traveler | `time_traveler` | Timeline manipulation and paradoxes |
| Ancient Civilization | `ancient` | Lost civilizations and ancient technology |
| AI Debate | `debate` | Multi-round theory vs. investigation debate |
| Escalation | `escalation` | Each round more absurd than the last |

For `debate` and `escalation` modes, set `rounds` (1–5) to control how many debate rounds run.

---

# Project Structure

```text
AI-Conspiracy-Generator/
├── backend/
│   ├── app/
│   │   ├── agents/          # Theory, Investigator, Judge, Evidence agents
│   │   ├── api/             # FastAPI routes
│   │   ├── models/          # Pydantic schemas and database models
│   │   ├── services/        # LLM providers, orchestration, sanitizer
│   │   ├── config.py        # Settings from environment
│   │   └── main.py          # FastAPI application entry point
│   ├── tests/               # Pytest test suite
│   ├── pyproject.toml       # Ruff & pytest config
│   ├── requirements.txt
│   ├── .dockerignore
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/      # React UI components
│   │   ├── api/             # API client
│   │   ├── types.ts         # TypeScript interfaces
│   │   └── App.tsx          # Main application
│   ├── package.json
│   ├── .eslintrc.cjs
│   ├── .prettierrc
│   ├── .dockerignore
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI
├── .pre-commit-config.yaml  # Pre-commit hook configuration
├── .dockerignore
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# Troubleshooting

## Docker port conflicts

If ports 5432, 6379, 8000, or 5173 are already in use:

```bash
# Stop conflicting services
docker compose down

# Or change the host port mapping in docker-compose.yml, e.g.:
#   ports:
#     - "8001:8000"   # maps host 8001 to container 8000
```

## Redis connection errors

Ensure Redis is running. If running the backend locally:

```bash
docker compose up redis -d
export REDIS_URL=redis://localhost:6379/0
```

## Backend won't start — database error

Make sure PostgreSQL is running and the `conspiracy` database exists:

```bash
docker compose up postgres -d
```

## Tests fail with "cannot connect to Redis"

Tests use `fakeredis` (an in-memory Redis simulator), so no running Redis is needed. If you see this error, ensure `fakeredis` is installed:

```bash
cd backend
pip install -r requirements.txt
```

## Frontend shows blank page / API errors

The frontend dev server proxies `/api` requests to `http://localhost:8000`. Make sure the backend is running on port 8000. For production Docker, check `docker compose logs backend` for errors.

---

# Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Make your changes
4. Run tests: `cd backend && pytest tests/ -v`
5. Run linting: `cd backend && ruff check .` and `cd frontend && npm run lint`
6. Commit with a descriptive message
7. Push and open a Pull Request

Please ensure:

- Tests pass for both backend and frontend
- New features include tests where practical
- Code follows the existing style (ruff for Python, eslint/prettier for TypeScript)
- Pull requests have a clear description of the change and motivation

---

# Future Enhancements

## Multiplayer Theory Battles

Allow users to compete against AI.

---

## Community Voting

Vote on:

- Funniest theory
- Most creative theory
- Best debunking

---

## Live Debate Mode

AI agents debate in real time.

---

## Theory Tournament

Generate competing theories and crown a winner.

---

## Historical Events Mode

Apply the system to historical events for entertainment and educational purposes.

---

# Skills Demonstrated

This project showcases:

- Multi-Agent AI Systems
- Prompt Engineering
- Adversarial Reasoning
- Agent Orchestration
- Fact Checking Workflows
- AI Evaluation Techniques
- Full Stack Development
- User Experience Design
- Humor-Oriented Product Design
- Python Development

---

# Why This Matters

The internet is full of narratives, speculation, and misinformation.

AI Conspiracy Generator uses humor to demonstrate how easily stories can be constructed and how important evidence-based reasoning remains.

The goal is to entertain users while encouraging skepticism, curiosity, and critical thinking.

---

# Disclaimer

This project is intended solely for entertainment, satire, and educational purposes.

The generated conspiracy theories are fictional and intentionally exaggerated. The platform is designed to encourage critical thinking and evidence-based reasoning, not to promote or validate conspiracy theories.

---

# License

MIT License