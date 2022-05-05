from ask_name.ask_name_1 import ask_name


min_age = 12
max_age = 130

def ask_age(name,min_age,max_age):
    while True:
        try:
            age = int(input("how old are you {}".format(name)))
            if age >= min_age and age < max_age:
                break
            elif age < min_age :
                print("sorry you are to young to be the ticket holder")
            else:
                print("stop the cap")
        except:
            print("<error> please enter an whole number")
    return age

if __name__ == "__main__":
    name = ask_name()
    age = ask_age(name,min_age,max_age)
    print(age)