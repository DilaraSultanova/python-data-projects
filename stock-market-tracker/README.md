# Stock Market Tracker

Python project that retrieves stock market data and saves it in a structured format for analysis.

## Project Overview

This project uses Python to collect stock market data, store it in a JSON file, and prepare it for analysis. It demonstrates API usage, JSON processing, automation, and file handling.

## Skills Demonstrated

- Python
- APIs
- JSON Processing
- Data Collection
- File Handling
- Automation
- Error Handling

## Project Goal

Build a tool that collects stock price data and stores it in a structured format for analysis.

## Project Files

- `stock_tracker.py` — collects stock data
- `stock_data.json` — stores collected stock data
- `requirements.txt` — lists required Python packages
- `README.md` — explains the project

## How to Run

```bash
pip install -r requirements.txt
python stock_tracker.py
```

## Output

The script saves collected stock data to:

```text
stock_data.json
```

## Example Output

```json
[
    {
        "symbol": "AAPL",
        "price": 210.15,
        "market_cap": 3200000000000,
        "sector": "Technology",
        "date_collected": "2025-06-20 15:30:00"
    }
]
```

## Future Improvements

- Add more stock symbols
- Calculate daily returns
- Visualize stock performance with charts
- Export data to CSV
- Build a stock dashboard
