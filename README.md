# TokenLens: A Token Waste Profiler

Token cost is a design problem, not a billing problem. Most LLM cost overruns come from architectural waste, not model pricing.

This tool is a token waste profiler that helps you understand where your tokens are going and which ones are useless. It's like `valgrind` for LLMs.

## The Problem

Most LLM systems waste 30-60% of their tokens on:
- Repeated instructions
- Bloated context
- Unused history
- Overlong outputs

Teams have no visibility into this waste. That's where TokenLens comes in.

## What TokenLens Is Not

- A token counter
- A billing dashboard
- A UI with charts
- A cost calculator

## What TokenLens Is

A token waste profiler that:
- Wraps LLM calls
- Tracks token-in vs value-out
- Identifies repeated context, redundant instructions, and oververbose responses
- Produces actionable recommendations

## Usage

```bash
python cli.py --run examples/sample_calls.json
```

This will output a JSON report with a breakdown of token waste and recommendations for optimization.
