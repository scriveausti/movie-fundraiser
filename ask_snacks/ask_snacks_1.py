snacks_list = ['popcorn', 'm&ms', 'pita chips']

def ask_snacks():
    print("the snacks we offer are popcorn, m&ms and pita chips")
    while True:
        snacks = input("what snack do you want?")
        if snacks in snacks_list:

