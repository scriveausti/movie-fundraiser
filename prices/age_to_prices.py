import time

from prices.prices_1 import prices
import os
price = prices()


def price_profit(row,total_price,total_profit):
    total_profit =+ price[row][2]
    total_price =+ price[row][1]
    return total_price,total_profit

def age_to_price(age,total_price,total_profit):

    if age <= 15:
        (total_price,total_profit) = price_profit(0,total_price,total_profit)
    elif age >= 16 and age <=64:
        (total_price,total_profit) = price_profit(1,total_price,total_profit)
    elif age >= 65 :
        (total_price,total_profit) = price_profit(2,total_price,total_profit)
    return total_price,total_profit

age = 16
total_price = 0.0
total_profit = 0.0

if __name__ == "__main__":

    (total_price,total_profit) = age_to_price(age,total_price,total_profit)
    print('price' , total_price)
    print('profit' , total_profit)