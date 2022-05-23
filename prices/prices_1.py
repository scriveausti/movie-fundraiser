
# format
# prices = [["thing", price, profit]]

def prices():
    prices = [["12 to 15",7.5,2.5],
              ["16 to 64",10.5,5.5],
              ["65 and older",6.5,1.5],
              ["popcorn",2.5,0.5],
              ["m&ms",3,0.6],
              ["pita chips",4.5,0.9],
              ["orange juice",3.25,0.65],
              ["water",2,0.4]]
    return prices



if __name__ =="__main__":
    price = prices()
    print(price[0][1])

    for r in range(0,7):
        row = price[r]
        try:
            place = row.index("m&m")
            print(r)
        except:
            print('no')
    print('1')