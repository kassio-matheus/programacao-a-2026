quantidade = int(input())

def fibonacci(n) :
    if 0 <= n <= 1 :
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))