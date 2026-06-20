import yfinance as yf
import json
from datetime import datetime

stocks = ["AAPL", "MSFT", "GOOGL", "TSLA", "NVDA"]

stock_data = []

print("=" * 50)
print("STOCK MARKET TRACKER")
print("=" * 50)

for symbol in stocks:
    try:
        stock = yf.Ticker(symbol)

        info = {
            "symbol": symbol,
            "price": stock.info.get("currentPrice"),
            "market_cap": stock.info.get("marketCap"),
            "sector": stock.info.get("sector"),
            "date_collected": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        stock_data.append(info)
        print(f"Loaded {symbol}")

    except Exception as e:
        print(f"Error loading {symbol}: {e}")

with open("stock_data.json", "w") as file:
    json.dump(stock_data, file, indent=4)

print("\nStock data saved successfully!")

print("\nCollected Data:")
for stock in stock_data:
    print(stock)
