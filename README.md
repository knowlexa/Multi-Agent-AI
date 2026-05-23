# Multi-Agent AI Orchestrator using LangGraph + Ollama + Azure OpenAI

## Overview

Enterprise-grade multi-agent orchestration framework built using:
- LangGraph
- LangChain
- Ollama
- Azure OpenAI
- Python

The orchestrator dynamically routes requests between specialized AI agents.

---

## Features

- Multi-agent orchestration
- Dynamic routing
- Shared state management
- Provider-agnostic LLM architecture
- Ollama local model support
- Azure OpenAI support
- LangGraph workflows
- Enterprise-ready architecture

---

## Architecture

(User → Orchestrator → Specialized Agents → Final Response)

---

## Agents

| Agent | Responsibility |
|---|---|
| Research Agent | Knowledge gathering |
| Coding Agent | Code generation |
| Security Agent | Security validation |

---

## Technologies Used

- Python
- LangGraph
- LangChain
- Ollama
- Azure OpenAI
- VS Code

---

## Setup Instructions

### 1. Clone Repository

git clone <repo-url>

### 2. Create Virtual Environment

python -m venv venv

### 3. Activate Environment

venv\Scripts\activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Configure Environment Variables

Copy:
.env.example → .env

### 6. Start Ollama

ollama serve

### 7. Pull Model

ollama pull llama3

### 8. Run Application

python main.py

---

## Future Enhancements

- RAG integration
- Azure AI Search
- Redis memory
- Human approval workflow
- Autonomous planning agents
- AKS deployment

---

## License

MIT