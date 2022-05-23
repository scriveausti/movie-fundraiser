from prices.prices_1 import prices
snacks = ['popcorn']
total_price = 10.5
total_profit = 5.5
profit = prices()


def index_array(array,find):
    for r in range(0,len(array)):
        row = array[r]
        try:
            place = row.index(find)
            return place,r
        except:
            not_used = True




def snacks_total(snacks,total_price,total_profit):
    if len(snacks) > 1:
        for i in (0,len(snacks)-1):
            add_row = index_array(profit,snacks[i])
            add_total = profit[add_row[1]][1]
            add_profit = profit[add_row[1]][2]
            total_profit = total_profit + add_profit
            total_price = total_price + add_total
    else:
        add_row = index_array(profit,snacks[0])
        add_total = profit[add_row[1]][1]
        add_profit = profit[add_row[1]][2]
        total_profit = total_profit + add_profit
        total_price = total_price + add_total

    return  total_price , total_profit

if __name__ == '__main__':
    total = snacks_total(snacks,total_price,total_profit)
    print(total)
