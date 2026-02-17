# 🤖 Multi-Agent Code Generator

> **Bade problems ko chhote pieces mein todo. Har piece ko solve karo. Combine karo. Run karo.**

A multi-agent system that breaks down complex coding problems into smaller subproblems, solves each independently, combines the solutions, validates them in a Docker sandbox — and delivers working code every time.

---

## 💡 The Problem I Was Solving

Every developer has faced this: you give a large, complex problem to an LLM — and it either hallucinates, produces broken code, or just gives up mid-way. The bigger the problem, the worse the output.

**My fix?** Don't give the whole problem to one agent. Break it down.

---

## 🏗️ How It Works

The system uses **4 specialized agents** in a pipeline:

```
User Input
    │
    ▼
┌─────────────────────────────────┐
│  Agent 1: Problem Decomposer    │  ← Breaks problem into subproblems
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│  Agent 2: Sub-Solver            │  ← Solves each subproblem independently
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│  Agent 3: Combiner & Builder    │  ← Combines solutions into functions/classes
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│  Agent 4: Input Generator       │  ← Creates dummy inputs to test the code
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│  🐳 Docker Sandbox              │  ← Runs the code safely
└────────────────┬────────────────┘
                 │
           ┌─────┴─────┐
           │           │
         Error?     Success!
           │           │
     Loop back      Return
     to Agent 2    Final Code
```

<img width="745" height="832" alt="Screenshot 2026-02-17 102636" src="https://github.com/user-attachments/assets/d8428dfd-5bb4-4b31-ab25-b2de228a852a" />


---

## 🤖 Agent Breakdown

### Agent 1 — Problem Decomposer
Takes the user's complex question and splits it into **small, independent subproblems**. Each subproblem is specific, focused, and solvable.

### Agent 2 — Sub-Solver
Receives each subproblem and solves it independently. By solving small, focused tasks, this agent produces accurate and reliable solutions.

### Agent 3 — Combiner & Builder
Takes all the individual solutions and **combines them** into a coherent Python function or class. It handles integration, resolves dependencies, and structures the final code properly.

### Agent 4 — Input Generator
Analyzes the generated function/class and creates **realistic dummy inputs** to test it. Edge cases, normal cases — it prepares proper test data automatically.

### 🐳 Docker Sandbox — Code Runner
The generated code + dummy inputs are executed **inside a Docker container** for safe, isolated execution:
- ✅ No risk to host system
- ✅ Controlled environment
- ✅ Captures stdout, stderr
- ✅ Returns output or error

**If error → loop restarts from Agent 2.**  
**If success → final code is returned to user.**

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker (running)
- API key for your chosen LLM provider

```env
LLM_API_KEY=your_api_key_here
LLM_MODEL=gpt-4  # or any model you're using
DOCKER_IMAGE=python:3.11-slim
MAX_RETRY_ATTEMPTS=3
```

### Run

```bash
python main.py
```

Or with a direct prompt:

```bash
python main.py --prompt "Create a function that scrapes product prices from a list of URLs and returns a sorted dictionary"
```

---

---

## 🔄 Retry Logic

If the Docker sandbox returns an error:

1. The error message is sent back to **Agent 2**
2. Agent 2 re-solves the relevant subproblem with the error context
3. Agent 3 re-combines and rebuilds the code
4. Agent 4 generates new inputs if needed
5. Docker runs again

This loop continues until either:
- ✅ Code runs successfully → output returned
- ❌ Max retries reached → error report returned with last attempt

---

## 🛡️ Why Docker Sandbox?

Running LLM-generated code directly on your machine is risky. Docker gives:

| Feature | Benefit |
|---|---|
| Isolation | Code can't access your host files |
| Reproducibility | Same environment every run |
| Safety | Malicious/broken code stays contained |
| Clean state | Fresh container for every execution |

---

## 🧠 Why Multi-Agent?

| Single LLM Approach | Multi-Agent Approach |
|---|---|
| One big prompt, high failure rate | Small focused prompts, reliable output |
| Context overflow on large problems | Each agent handles a small context |
| Hard to debug | Failure isolated to one agent |
| No validation | Code actually runs and is verified |

---

## 📌 Example

**User Input:**
```
Create a system that reads a CSV file of student marks, 
calculates grade, GPA, and pass/fail status, 
and exports a summary report as JSON.
```

