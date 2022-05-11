from prices.prices_1 import prices

def age_to_price(age,total_price):
    price = prices()
    if age <= 15:
        total_price = + price[0][1]
    elif age >= 16 and age <=64:
        total_price =+ price[1][1]
    elif age >= 65 :
        total_price =+ price[2][1]
    return total_price

age = 65
total_price = 0

if __name__ == "__main__":

    total_price = age_to_price(age,total_price)
    print(total_price)
