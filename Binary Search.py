#Test
from math import *
n = int(input("Enter the number:"))
list = [3,44,22,4,12,542,78]
list.sort()

min= 0
max = len(list)-1
avg = floor((min+max)/2)

ans = False

while ans==False:
    if n==list[avg] and min>=0 and max<=len(list):
        print("element found at",avg,"position")
        ans=True
        break

    elif n<list[avg]:
        max=avg-1
        avg = floor((min + max) / 2)
    else:
        min=avg+1
        avg = floor((min + max) / 2)

if ans==False:
    print("Element not found in the list")









