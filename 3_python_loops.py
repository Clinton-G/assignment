def average_closing_price(stock_data, stock_symbol, start_date, end_date):
    total_price = 0
    count = 0
    
    for symbol, date, price in stock_data:
        if symbol == stock_symbol and start_date <= date <= end_date:
            total_price += price
            count += 1
    
    if count == 0:
        return None
    return total_price / count

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("MSFT", "2021-01-02", 230.0),
    # More data...
]

aapl_avg = average_closing_price(stock_data, "AAPL", "2021-01-01", "2021-01-02")
msft_avg = average_closing_price(stock_data, "MSFT", "2021-01-01", "2021-01-02")

print(f"AAPL Average Closing Price: {aapl_avg}")
print(f"MSFT Average Closing Price: {msft_avg}")
