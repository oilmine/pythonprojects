import time
import random

user = [-1]
cmp = [0]
nxt = 2

while 1 + 2 == 3:
    num = int(input("> "))
    user.append(num)
    time.sleep(random.uniform(0.3, 1))

    nxt = num + 1
    cmp.append(nxt)

    if cmp[-1] - 3 != user[-2]:
        print("You miscounted! Try again. The next number is 1.")
        break

    print("~>", nxt)
