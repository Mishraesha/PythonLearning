

def search(lst,n):

    ans = 0
    for i in lst:
        if i==n:
            ans=ans+1

        else:
            pass
    if ans!=0:
        return True
    else:
        return False

list = [2,5,6,5,3,324,9]
if search(list,5)== True:
    print("Element found")
else:
    print("Element not found")






