def fact(n):

    if n<=1:
        return 1
    else:
        return (n*(fact(n-1)))

x = int(input('Enter the number to find the factorial : '))

print(fact(x))

fact = 1

for i in range(1, x+1):
    fact = fact*i
print(fact)