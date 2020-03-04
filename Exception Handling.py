
a = 5
b = 2

try:
    print(a/b)
    k = int(input("Enter a number")) #Run time try to enter a character

except ZeroDivisionError as e:
    print("Cannot divide by zero")
except Exception as e:
    print("something went wrong...")

finally:
    print("Resource closed")