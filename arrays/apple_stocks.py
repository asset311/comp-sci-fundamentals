'''
Write an efficient function that takes stock_prices and returns the best profit I could 
have made from one purchase and one sale of one share of Apple stock yesterday.

Example:
stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
Returns 6 (buying for $5 and selling for $11)

No shorting is allowed. You cannot buy and sell in the same time step

'''
# outer loop goes through all prices
# inner loop loop goes through one fewer price each time
# O(n^2)
def get_max_profit(stock_prices):
    max_profit = 0

    i=0
    while i < len(stock_prices)-1:
        for j in stock_prices[i:]:
            if j > stock_prices[i]:
                potential_profit = j - stock_prices[i]
                max_profit = max(max_profit, potential_profit)
        i += 1
    return max_profit


# we can do in our for loop, but calculating against the highest remaining price
# this is just syntactic sugar, it is will O(n^2)
def get_max_profit(stock_prices):
    max_profit = 0

    i = 0
    while i < len(stock_prices) - 1:
        potential_profit = max(stock_prices[i:]) - stock_prices[i]
        max_profit = max(potential_profit, max_profit)
        i += 1
    return max_profit

# use a greedy approach
# we'll greedily update min_price and max_profit, so we initialize
# them to the first price and the first possible profit
def get_max_profit(stock_prices):

    # this is reasonable, as we'd need to have at least two prices to buy and sell
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = stock_prices[0] #opening price is the minimum price initiallly
    max_profit = stock_prices[1] - stock_prices[0]  # the first profit we could get

    #start at the second time, because we can't buy and sell in the same time 0
    for current_price in stock_prices[1:]:      
        
        potential_profit = current_price - min_price    #calculate profit before updating min_price to make sure we're selling correctly
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)   #update the min_price to the lowest seen so far

    return max_profit

# O(n) time complexity, and O(1) space complexity