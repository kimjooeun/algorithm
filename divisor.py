import math

def divisor(n):
    divisor = []
    i = 1
    sqrt = math.sqrt(n)
    while(i<=sqrt):
        if n == 1:
            break;
        
        if n%i == 0:
            divisor.append(i)
            divisor.append(int(n/i))
            i = i+1
    return divisor