
list = [34,2,4,1,65,9]
print(list)
l = len(list)

for i in list:
    a = list.index(i)
    if list[a]>list[a+1]:
        list[a],list[a+1]=list[a+1],list[a]

print(list)