from basic_functions.y_n import yes_no

snacks_list = ['popcorn', 'm&ms', 'pita chips']
no_words = ["nothing",'none','']

def ask_snacks():
    print("the snacks we offer are popcorn, m&ms and pita chips or nothing")
    while True:
        snacks = input("what snack do you want?").lower().strip()
        if snacks in snacks_list:
             
        elif snacks in no_words:
            yes = yes_no('are you sure you want nothing',"","")
            if yes == True:
                break
        else:
            print("<error> please enter one of the snacks or nothing")



