def ask_name():
    while True:
        name = input("what is your name?").lower().strip()
        if name.isdigit():
            print("<error> names can't start with a number")
        else:
            break
    return name

if __name__ == "__main__" :
    name = ask_name()
    print ("hello {}".format(name))
