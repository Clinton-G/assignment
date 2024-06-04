stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("MSFT", "2021-01-02", 230.0),
]

#   Find the Average:
#                       close $ 130.0    +  close $ 132.0    /   2   =   131.0
AAPL_Average = print(((stock_data[0][2]) + (stock_data[1][2])) / 2)
#                       close $ 220.0    +  close $ 230.0    /   2   =   225.0
MSFT_Average = print(((stock_data[2][2]) + (stock_data[3][2])) / 2)


