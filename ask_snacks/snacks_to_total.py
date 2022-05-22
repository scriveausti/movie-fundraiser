from prices.prices_1 import prices
snacks = ['popcorn','m&m']
total_price = 0.0
profit = prices()


def index_array(array,find):
    for r in range(0,len(array)):
        row = array[r]
        try:
            place = row.index(find)
            return place,r
        except:
            not_used = True




def snacks_total(snacks,total_price):
    if len(snacks) > 1:
        for i in (0,len(snacks)-1):
            add_row = index_array(profit,snacks[i])
            add_total = profit[add_row[1]][1]
            print(add_total)
            total_price = total_price + add_total
    else:
        add_row = index_array(profit,snacks[0])
        add_total = profit[add_row[1]][1]
        print(add_total)
        total_price =+ add_total

    return  total_price

if __name__ == '__main__':
    total_price = snacks_total(snacks,total_price)
    print(total_price)
