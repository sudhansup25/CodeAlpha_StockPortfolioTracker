# CodeAlpha - Stock Portfolio Tracker

A console-based stock investment calculator built as Task 2 of the CodeAlpha Python
Programming Internship.

## What it does

You enter stock symbols and quantities; the script calculates your total investment value
using a hardcoded price dictionary and displays a formatted summary. Results can optionally
be saved to `.txt` or `.csv`.

## Features

- 8 hardcoded stock prices (AAPL, TSLA, GOOGL, MSFT, AMZN, META, NFLX, NVDA)
- Rejects unknown symbols and invalid quantities instead of crashing
- Merges repeated entries of the same stock instead of overwriting them
- Formatted table output with per-stock subtotal and grand total
- Optional export to `.txt` or `.csv`

## Concepts used

Dictionaries, input/output, basic arithmetic, file handling (`csv` module)

## How to run

```bash
python3 stock_tracker.py
```

Type `done` when finished entering stocks, or `list` to see available symbols and prices.
Requires Python 3.6+. No external dependencies.

## What I learned

Separating the calculation logic (`calculate_investment()`) from the display logic
(`display_summary()`) made it obvious how I'd unit test the math independently of anything
printed to the console — a pattern I plan to keep using.