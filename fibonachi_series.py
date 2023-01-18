def fib(n):
    x = 0
    y = 1
    print(0)
    print(1)
    while n-2>0:
        z = x+y
        print(z)
        x = y
        y = z
        n-=1

def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))

fib(3)

n = 3
for i in range(n):
    print(fibo(i))