# AI Conspiracy Generator

An AI-powered comedy platform where one AI agent creates increasingly ridiculous conspiracy theories while another AI agent investigates, fact-checks, and debunks them.

The goal is not to promote misinformation.

The goal is to demonstrate how easily narratives can be constructed around incomplete information while using humor, critical thinking, and adversarial AI reasoning to separate fact from fiction.

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

# Why This Project Exists

Humans are naturally wired to seek patterns and explanations.

Given limited information, it is surprisingly easy to construct convincing stories that appear logical but have little connection to reality.

AI Conspiracy Generator uses humor to illustrate:

* Confirmation bias
* Narrative construction
* Critical thinking
* Evidence evaluation
* Fact checking
* Adversarial reasoning

The platform is designed as entertainment first and educational second.

---

# Core Concept

Input:

```text id="6xv4nr"
Why did the neighborhood power go out?
```

---

## Theory Agent

Creates a conspiracy theory.

```text id="w9ry2z"
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

```text id="n2ck1h"
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

```text id="q7tu4e"
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

* Creating theories
* Connecting unrelated events
* Escalating absurdity
* Defending its claims

---

### Investigator Agent

Responsible for:

* Fact checking
* Evidence review
* Logical analysis
* Debunking claims

---

### Judge Agent

Responsible for scoring:

* Creativity
* Plausibility
* Evidence quality
* Entertainment value

---

### Evidence Agent (Optional)

Responsible for:

* Gathering facts
* Finding contradictions
* Building timelines
* Supporting investigations

---

# Game Modes

## Classic Conspiracy Mode

Create increasingly elaborate conspiracy theories.

---

## X-Files Mode

Every event must involve:

* Aliens
* Government coverups
* Secret facilities
* Paranormal activity

---

## Corporate Conspiracy Mode

Every event is blamed on a fictional mega-corporation.

Example:

```text id="k0zn5m"
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

* Lost civilizations
* Ancient technology
* Mysterious artifacts

---

## AI Debate Mode

Theory Agent and Investigator Agent engage in multiple rounds.

Example:

### Round 1

```text id="g1kv6o"
Squirrels caused the outage.
```

### Round 2

```text id="pr5gxp"
The squirrels are organized.
```

### Round 3

```text id="9vx5pk"
The squirrels report to an
interdimensional acorn council.
```

### Investigator

```text id="n1khm6"
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

```text id="p5k8m9"
Actual Cause

A contractor accidentally struck
a power transformer while digging.

Case Closed.
```

---

# Example Scenarios

## Power Outage

```text id="p0v5gj"
Why did the power go out?
```

---

## Missing Package

```text id="a8gx3n"
Why was my package delayed?
```

---

## Slow Internet

```text id="p9b72q"
Why is my internet slow?
```

---

## Traffic Jam

```text id="k4t1hd"
Why was traffic stopped?
```

---

## Broken Coffee Machine

```text id="d2p7fx"
Why did the office coffee machine stop working?
```

---

# Educational Goals

Although designed as comedy, the platform demonstrates:

* Confirmation bias
* Logical fallacies
* Correlation vs causation
* Evidence evaluation
* Critical thinking
* Fact verification

The project encourages users to question assumptions and examine evidence.

---

# Architecture

```text id="r5y9zk"
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

* Python
* FastAPI
* PostgreSQL
* Redis

---

## AI

* OpenAI GPT Models
* Anthropic Claude
* Local LLM Support

---

## Agent Framework

* Multi-Agent Orchestration
* Prompt Chaining
* Reasoning Pipelines

---

## Frontend

* React
* TailwindCSS

---

## Deployment

* Docker
* Docker Compose
* Linux

---

# Setup

## Prerequisites

* **Docker & Docker Compose** (recommended) — for running the full stack with one command
* **Node.js 20+** — for local frontend development
* **Python 3.12+** — for local backend development
* **PostgreSQL 16** and **Redis 7** — required when running the backend outside Docker

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

## API Endpoints

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

## Project Structure

```text
AI-Conspiracy-Generator/
├── backend/
│   ├── app/
│   │   ├── agents/          # Theory, Investigator, Judge, Evidence agents
│   │   ├── api/             # FastAPI routes
│   │   ├── models/          # Pydantic schemas and database models
│   │   ├── services/        # LLM providers and orchestration
│   │   ├── config.py        # Settings from environment
│   │   └── main.py          # FastAPI application entry point
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/      # React UI components
│   │   ├── api/             # API client
│   │   └── App.tsx          # Main application
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# Future Enhancements

## Multiplayer Theory Battles

Allow users to compete against AI.

---

## Community Voting

Vote on:

* Funniest theory
* Most creative theory
* Best debunking

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

* Multi-Agent AI Systems
* Prompt Engineering
* Adversarial Reasoning
* Agent Orchestration
* Fact Checking Workflows
* AI Evaluation Techniques
* Full Stack Development
* User Experience Design
* Humor-Oriented Product Design
* Python Development

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
