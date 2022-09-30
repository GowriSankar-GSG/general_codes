# Terms default 1,2 
from calendar import c


n1 = 0
n2 = 1
def fibonacci(terms,n1,n2):
    if terms == 1:
        for i in range(n1,n2+1):
            print(i)
    elif terms > 1:
        print(n1)
        print(n2)
        for i in range(2,terms):
            temp = n1 + n2
            n1 = n2
            n2 = temp
            print(temp)
terms = int(input("Number of Fibonacci terms: "))
fibonacci(terms,n1,n2)