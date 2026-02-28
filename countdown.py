import time

n = int(input(f'How long should the countdown be (in seconds)? => '))
msg = input("What should be said after the countdown ends? => ")
num = n

while num != 0:
    print(num)
    time.sleep(1)
    num = num - 1
if num == 0:
    print(msg)
