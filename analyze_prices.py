"""Read the documented synthetic CSV, calculate price returns, save results.
Run: uv run --locked python analyze_prices.py
Uses only Python's standard library. Read DATA_DICTIONARY.md first.
"""
import csv
import math
from datetime import date
from pathlib import Path

FOCUS_SECURITY = "SYN_B"  # Change to SYN_B for the assignment.
project = Path(__file__).resolve().parent
data_path = project / "sample_data" / "synthetic_prices.csv"
output_dir = project / "outputs"
output_dir.mkdir(exist_ok=True)
prices = []
seen = set()
with data_path.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    if reader.fieldnames != ["security_id", "date", "price"]:
        raise ValueError("Unexpected columns; check the data dictionary.")
    for row in reader:
        security = row["security_id"].strip()
        day = date.fromisoformat(row["date"])
        price = float(row["price"]) if row["price"].strip() else None
        key = (security, day)
        if not security or key in seen:
            raise ValueError("Missing security or duplicate security/date key.")
        if price is not None and (not math.isfinite(price) or price <= 0):
            raise ValueError("Prices must be positive finite numbers or blank.")
        seen.add(key)
        prices.append((security, day, price))
if not prices:
    raise ValueError("The source has no observations.")
prices.sort(key=lambda row: (row[0], row[1]))
previous_by_security = {}
result = []
for security, day, price in prices:
    previous = previous_by_security.get(security)
    price_return = (price / previous - 1
                    if price is not None and previous is not None else None)
    if security == FOCUS_SECURITY:
        result.append((security, day, price, previous, price_return))
    # Update even when price is missing: do not bridge a missing observation.
    previous_by_security[security] = price
if not result:
    raise ValueError("FOCUS_SECURITY was not found in the source file.")
output_path = output_dir / "returns_python.csv"
with output_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["security_id", "date", "price", "previous_price", "price_return"])
    writer.writerows(result)
with output_path.open(newline="", encoding="utf-8") as f:
    saved = list(csv.DictReader(f))
print("Input:", data_path)
print(f"Source: {len(prices)} rows | {len({r[0] for r in prices})} securities | "
      f"{sum(r[2] is None for r in prices)} missing price")
print(f"Dates: {min(r[1] for r in prices)} through {max(r[1] for r in prices)}")
print(f"Selected: {FOCUS_SECURITY} | {len(result)} rows | "
      f"usable returns: {sum(r[4] is not None for r in result)}")
print("Output:", output_path)
print(f"Reopened {len(saved)} saved rows. Returns are decimals; 0.02 means 2%.")
