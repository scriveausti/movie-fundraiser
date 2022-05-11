def yes_no(ask_user,y_out,n_out):
    yes_words = ['yes','y','ye','sure']
    no_words = ['no','n',]
    while True:
        answer = input(ask_user).lower().strip()
        if answer in yes_words:
            print(y_out)
            yes = True
            break
        elif answer in no_words:
            print(n_out)
            yes = False
            break
        else:
            print("<error> please enter yes or no")
    return yes


if __name__ == '__main__':
    ask = "is your name joe "
    yes_out = "yooooooo i knew"
    no_out = "dam"
    yes_no(ask,yes_out,no_out)
