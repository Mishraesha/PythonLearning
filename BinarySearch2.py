from math import *

n = int(input("Enter the number:"))
pos = -1
list = [23,4,12,535,3,1,89]

lower = 0
upper = len(list)-1



while lower<=upper:
    avg = floor((lower + upper / 2))
    if list[avg]==n:
        print("Element found at:",avg,"position")
        pos=1

    elif n > list[avg]:
        lower=avg+1
    else:
        upper=avg+1

if pos== -1:
    print("Element not found")















