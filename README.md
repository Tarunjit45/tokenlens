# 🔍 TokenLens — Architectural Token Waste & Cost Profiler for LLMs

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CLI](https://img.shields.io/badge/CLI-TokenLens-FF5722?style=for-the-badge)](cli.py)
[![Focus](https://img.shields.io/badge/Focus-LLM%20Cost%20Optimization-00C853?style=for-the-badge)](README.md)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> *"Token cost is a design problem, not a billing problem."*

Most LLM cost overruns don't come from model provider pricing—they come from **architectural waste**: redundant system instructions, bloated conversation histories, uncompressed tool schemas, and repetitive context injections.

**TokenLens** is a token waste profiler that audits LLM traces, dissects prompt overhead, and identifies exactly where tokens are being wasted.

---

## 📌 What TokenLens Audits

```
+-------------------------------------------------------------+
|                      Captured LLM Trace                     |
|                 (JSON export from LangChain/Llama)          |
+-------------------------------------------------------------+
                              |
                              v  `cli.py --run trace.json`
+-------------------------------------------------------------+
|                 Token Profiler (`profiler.py`)              |
|        Dissects prompt into System, History, Tools, User    |
+-------------------------------------------------------------+
                              |
                              v  `heuristics.py`
+-------------------------------------------------------------+
|                  Waste Detection Heuristics                 |
|  - Repetitive Few-Shot Examples    - Redundant Tool Schemas |
|  - Runaway Chat History Bloat      - Unused Context Chunks  |
+-------------------------------------------------------------+
                              |
                              v  `report.py`
+-------------------------------------------------------------+
|                  Token Waste Scorecard & Savings            |
|       Estimated % cost reduction & actionable optimizations |
+-------------------------------------------------------------+
```

---

## 📁 Repository Structure

```text
tokenlens/
├── cli.py             # TokenLens CLI entry point (`python cli.py --run <file>`)
├── profiler.py        # `LLMCallProfiler` token decomposition engine
├── analyzer.py        # Multi-call trace analyzer & pattern detector
├── heuristics.py      # Token waste heuristic rules & threshold checks
├── report.py          # Summary scorecard & savings breakdown generator
├── examples/          # Sample LLM run trace payloads
├── LICENSE            # MIT License
└── README.md
```

---

## 🚀 Quick Start

### 1. Installation
Clone the repository:

```bash
git clone https://github.com/Tarunjit45/tokenlens.git
cd tokenlens
```

*Runs with pure Python 3.10+ standard libraries; no heavy external frameworks required.*

### 2. Audit an LLM Run Trace
Run TokenLens against any exported LLM call trace:

```bash
python cli.py --run examples/sample_run.json
```

TokenLens generates a terminal scorecard identifying:
* 📉 **System Prompt Ratio:** Percentage of total cost spent on static instructions.
* 🗑️ **Redundancy Score:** Tokens that repeat identical information across sequential turns.
* 💡 **Estimated Dollar Savings:** Projected savings from context compression and cache optimization.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
