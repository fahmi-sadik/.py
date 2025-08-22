len = int(input())

def ssum(n):
    
    if n % 2 == 0 and n % 3 == 0:
        total = sum(i * (i + 1) for i in range(1, n + 1))
    elif n % 3 == 0:
        total = sum(i**3 for i in range(1, n + 1))
    elif n % 2 == 0:
        total = sum(i**2 for i in range(1, n + 1))
    else:
        total = 0 

    return total

print(ssum(len))