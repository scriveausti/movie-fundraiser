import random
import time
num = 3
e ='e'


while True:
    wait = random.randint(1,100)
    wait = wait / 1000000000
    num = random.randint(1,100000000000000000)
    num2 = random.randint(1,100000000000000000)
    num3 = random.randint(1,100000000000000000)
    num4 = random.randint(1,100000000000000000)
    print(num,num2,num3,num4)
    time.sleep(wait)
