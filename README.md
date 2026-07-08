# CGAO

> **ChatGPT Guided AI Observatory**

CGAO is an open-source Python framework for collecting and analyzing social media data for Generative AI research.

The project currently focuses on Xiaohongshu (RED) and is designed to support academic research, including large-scale data collection, dataset construction, LLM annotation, and downstream NLP analysis.

---

## Features

### Current (v0.1.0)

- Persistent Login (Playwright Storage State)
- Xiaohongshu Search
- Search Result Collection
- Structured Post Model
- Modular Page Object Architecture
- Parser Layer
- Service Layer

### Planned

- Infinite Scroll
- CSV Export
- SQLite Database
- Post Detail Parser
- Comment Collection
- LLM Annotation
- Sentence-BERT Embedding
- Topic Modeling
- Research Dataset Pipeline

---

## Project Structure

```text
CGAO
│
├── cgao/
│   ├── crawler/
│   ├── pages/
│   ├── parsers/
│   ├── models/
│   ├── services/
│   ├── exporters/
│   └── utils/
│
├── examples/
├── docs/
├── tests/
├── data/
├── outputs/
└── storage/
```

---

## Installation

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/CGAO.git

cd CGAO

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

playwright install
```

---

## Quick Start

### Login

```bash
python -m examples.login_demo
```

### Search

```bash
python -m examples.search_demo
```

### Collect

```bash
python -m examples.collect_demo
```

---

## Roadmap

### v0.1.0

- Browser Engine
- Persistent Login
- Search
- Search Result Collection

### v0.2.0

- Infinite Scroll
- CSV Export
- SQLite Export

### v0.3.0

- Post Detail Parsing
- Comment Collection

### v1.0.0

Research Platform

- Dataset Construction
- LLM Annotation
- Embedding
- Research Pipeline

---

## License

MIT License