# AI Workspace

A production-oriented Agentic AI learning project built step by step.

## Features

- Clean Architecture
- Configuration Management
- Production Logging
- Gemini Integration (coming soon)
- Tool Calling
- Memory
- RAG
- Multi-Agent Systems

## Tech Stack

- Python
- Gemini API
- Pydantic
- python-dotenv
- pytest

## Project Structure

```text
ai-workspace/
├── agent/
├── bootstrap/
├── config/
├── llm/
├── logs/
├── memory/
├── rag/
├── tests/
└── tools/
```

## Setup

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

Copy:

```text
.env.example
```

to

```text
.env
```

and add your Gemini API key.

Run:

```bash
python app.py
```