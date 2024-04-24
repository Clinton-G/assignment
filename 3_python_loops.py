#   Task 1:


# Your task is to write a function to find the average closing price of a specified stock.


stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("MSFT", "2021-01-02", 230.0),
]
#   ('Stock Symbol', 'Date', 'Closing Price'),

#   to find average, add the closing prices together, divide by # of values


#   Conv. tuple into list:
stock_data = list(stock_data)

#   Find the Average:
#                       close $ 130.0    +  close $ 132.0    /   2   =   131.0
AAPL_Average = print(((stock_data[0][2]) + (stock_data[1][2])) / 2)
#                       close $ 220.0    +  close $ 230.0    /   2   =   225.0
MSFT_Average = print(((stock_data[2][2]) + (stock_data[3][2])) / 2)

#   Conv. list back into a tuple
stock_data = tuple(stock_data)





