import random


class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price


class Portfolio:
    def __init__(self, balance):
        self.balance = balance
        self.stocks = {}

    
    def buy_stock(self, stock, quanitity):
        cost = stock.price * quanitity
        if cost <= self.balance:
            self.balance -= cost
            if stock.symbol in self.stocks:
                self.stocks[stock.symbol] += quanitity
            else:
                self.stocks[stock.symbol] = quanitity
            print(f"Bought {quantity} shares of {stock.symbol} for ${cost}.")
        else:
            print("Insufficient funds to buy.")
    

    def sell_stock(self, stock, quantity):
        if stock.symbol in self.stocks and self.stocks[stock.symbol] >= quantity:
            self.balance += stock.price * quantity
            self.stocks[stock.symbol] -= quantity
            print(f"Sold {quantity} shares of {stock.symbol} for ${stock.price * quantity}.")
        else:
            print("Unable to sell. Either stock not owned or insufficient quantity.")


def simulate_stock_market():
    stocks = [Stock("AAPL", 150), Stock("GOOGL", 2500), Stock("AMZN", 3300), Stock("MSFT", 300)]
    portfolio = Portfolio(10000)


    print("Welcome to the Stock Market Simulator.")


    for _ in range(10):
        for stock in stocks:
            stock.price += random.uniform(-10, 10)

        print("\nStock Prices:")
        for stock in stocks:
            print(f"{stock.symbol}: ${stock.price:.2f}")

        action = input("\nDo you want to (B)uy or (S)ell stocks? Press (Q) to quit: ").upper()

        if action == 'Q':
            break
        elif action == 'B':
            symbol = input("Enter stock symbol to buy: ").upper()
            quantity = int(input("Enter quantity to buy: "))
            stock_to_buy = next((s for s in stocks if s.symbol == symbol), None)
            if stock_to_buy:
                portfolio.buy_stock(stock_to_buy, quantity)
            else:
                print("Invalid stock symbol.")
        elif action == 'S':
            symbol = input("Enter stock symbol to sell: ").upper()
            quantity = int(input("Enter quantity to sell: "))
            stock_to_sell = next((s for s in stocks if s.symbol == symbol), None)
            if stock_to_sell:
                portfolio.sell_stock(stock_to_sell, quantity)
            else:
                print("Invalid stock sybol.")
        else:
            print("Invalid action. Please choose (B)uy, (S)ell, or (Q)uit.")


if __name__ == "__main__":
    simulate_stock_market()
            