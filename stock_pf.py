"""
Stock Portfolio Tracker
CodeAlpha Python Programming Internship — Task 2

Calculates total investment value based on manually defined (hardcoded)
stock prices and user-entered quantities. Optionally saves the result
to a .txt or .csv file.

Concepts used: dictionary, input/output, basic arithmetic, file handling.
"""

import csv
from datetime import datetime

# Hardcoded stock prices (USD). In a real system this would come from an API.
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 185,
    "META": 480,
    "NFLX": 650,
    "NVDA": 120,
}


def display_available_stocks():
    """Print the hardcoded stock symbols and their prices."""
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price}")
    print()


def get_quantity_input(symbol):
    """Prompt until a valid, positive quantity is entered for the given symbol."""
    while True:
        raw_qty = input(f"Enter quantity for {symbol}: ").strip()
        try:
            quantity = float(raw_qty)
        except ValueError:
            print(">> Please enter a valid number.\n")
            continue

        if quantity <= 0:
            print(">> Quantity must be greater than zero.\n")
            continue

        return quantity


def build_portfolio():
    """
    Collect stock symbol + quantity pairs from the user until they type 'done'.
    Returns a dict of {symbol: total_quantity}, merging repeated entries.
    """
    portfolio = {}
    display_available_stocks()
    print("Enter a stock symbol and quantity for each holding.")
    print("Type 'done' as the symbol when you're finished.\n")

    while True:
        symbol = input("Stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f">> '{symbol}' isn't in the price list. Type 'list' to see available stocks.\n")
            if symbol == "LIST":
                display_available_stocks()
            continue

        quantity = get_quantity_input(symbol)
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f">> Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    """
    Given a {symbol: quantity} dict, return a list of row dicts
    (symbol, quantity, price, subtotal) and the grand total.
    """
    rows = []
    total = 0.0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        subtotal = price * quantity
        rows.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "subtotal": subtotal,
        })
        total += subtotal

    return rows, total


def display_summary(rows, total):
    """Print a formatted table of holdings and the total investment value."""
    if not rows:
        print("\nNo holdings entered. Nothing to summarize.")
        return

    print("\n" + "=" * 50)
    print("PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Symbol':<8}{'Qty':<10}{'Price':<10}{'Subtotal':<12}")
    print("-" * 50)
    for row in rows:
        print(f"{row['symbol']:<8}{row['quantity']:<10}${row['price']:<9}${row['subtotal']:<11.2f}")
    print("-" * 50)
    print(f"TOTAL INVESTMENT: ${total:.2f}")
    print("=" * 50)


def save_to_txt(rows, total, filename):
    """Write the portfolio summary to a .txt file."""
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n")
        f.write(f"{'Symbol':<8}{'Qty':<10}{'Price':<10}{'Subtotal':<12}\n")
        f.write("-" * 50 + "\n")
        for row in rows:
            f.write(f"{row['symbol']:<8}{row['quantity']:<10}${row['price']:<9}${row['subtotal']:<11.2f}\n")
        f.write("-" * 50 + "\n")
        f.write(f"TOTAL INVESTMENT: ${total:.2f}\n")


def save_to_csv(rows, total, filename):
    """Write the portfolio summary to a .csv file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Subtotal"])
        for row in rows:
            writer.writerow([row["symbol"], row["quantity"], row["price"], f"{row['subtotal']:.2f}"])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL", f"{total:.2f}"])


def offer_save(rows, total):
    """Ask the user whether to save results, and in which format."""
    if not rows:
        return

    choice = input("\nSave results to a file? (y/n): ").strip().lower()
    if choice != "y":
        return

    fmt = input("Format — txt or csv?: ").strip().lower()
    if fmt not in ("txt", "csv"):
        print(">> Unrecognized format, defaulting to .txt")
        fmt = "txt"

    filename = f"portfolio_summary.{fmt}"

    if fmt == "csv":
        save_to_csv(rows, total, filename)
    else:
        save_to_txt(rows, total, filename)

    print(f">> Saved to {filename}")


def main():
    portfolio = build_portfolio()
    rows, total = calculate_investment(portfolio)
    display_summary(rows, total)
    offer_save(rows, total)
    print("\nThanks for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()