from basic_functions.y_n import yes_no

snacks_list = ['popcorn', 'm&ms', 'pita chips']
no_words = ["nothing", 'none', '']
yes_words = ['yes', 'y', 'ya']
more = ['more', 'moresnacks']
snacks = []

def ask_not_frist_snack(snacks):
    while True:
        snack2 = input('what other snacks do you want? ').lower().strip()
        if snack2 in snacks_list:
            snacks.append(snack2)
            yes = yes_no('do you want more snacks? ')
            if yes == True:
                more = True
                return more, snacks

        elif snack2 in no_words:
            break
        else:
            print('<error> please enter one of the snacks or none')


def ask_snacks(snacks):
    print("the snacks we offer are popcorn, m&ms and pita chips or nothing")
    while True:
        snack = input("what snack do you want?").lower().strip()
        if snack in snacks_list:
            snacks.append(snack)
            yes = yes_no('do you just want {} or more snacks'.format(snack),"","")
            if yes == True:
                break
            else:
                while True:
                    out = ask_not_frist_snack(snacks)
                    snacks = out[1]
                    if out[0] != True:
                        break

        elif snacks in no_words:
            yes = yes_no('are you sure you want nothing', "", "")
            if yes == True:
                break
        else:
            print("<error> please enter one of the snacks or nothing")
    return snacks 


snacks = ask_snacks(snacks)
print(snacks)