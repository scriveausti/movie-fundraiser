from prices.prices_1 import prices

def age_to_price(age,total_price,prices):

    if age <= 15:
        age_thing = "12 to 15"

    li = price.index(age_thing)
    total_price =+ price[li][1]
    print(total_price)

age = 14
total_price = 0

if __name__ == "__main__":
    price = prices()
    total_price = age_to_price(age,total_price,price)
