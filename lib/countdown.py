# your code goes here!
import time

def countdown(num):
    x = num
    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1
    if x == 0:
        print('HAPPY NEW YEAR!')

def countdown_with_sleep(num):
    x = num
    while x > 0:
        time.sleep(1)
        print(f'{x} SECOND(S)!')
        x -= 1
    if x == 0:
        time.sleep(1)
        print('HAPPY NEW YEAR!')