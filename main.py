from ask_name.ask_name_1 import ask_name
from ask_age.ask_age_1 import ask_age
from prices.age_to_prices import age_to_price
from ask_snacks.snacks_to_total import snacks_total
from ask_snacks.ask_snacks_1 import ask_snacks


total_price = 0.0
total_profit = 0.0
min_age = 12
max_age = 130
snacks = []

name = ask_name()
age = ask_age(name,min_age,max_age)
(total_price,total_profit) = age_to_price(age,total_price,total_profit)
snacks = ask_snacks(snacks)
(total_price,total_profit) = snacks_total(snacks,total_price,total_profit)

print("price",total_price)
print("profit",total_profit)

