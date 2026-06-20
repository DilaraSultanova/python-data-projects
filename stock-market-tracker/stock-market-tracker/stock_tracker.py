import yfinance as yf
import json

stocks = ["AAPL", "MSFT", "GOOGL", "TSLA", "NVDA"]

stock_data = []

for symbol in stocks:
    try:
        stock = yf.Ticker(symbol)

        info = {
            "symbol": symbol,
            "current_price": stock.info.get("currentPrice"),
            "market_cap": stock.info.get("marketCap"),
            "sector": stock.info.get("sector")
        }

        stock_data.append(info)

    except Exception as e:
        print(f"Error loading {symbol}: {e}")

with open("stock_data.json", "w") as file:
    json.dump(stock_data, file, indent=4)

print("Stock data saved successfully!")

for stock in stock_data:
    print(stock)
