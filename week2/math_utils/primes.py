import math
def isprime(n):
    sq = math.ceil(math.sqrt(n))
    if n==1:
        return False
    for i in range(2,sq+1):
        if n%i==0 and n!=i:
            print(n,i)
            return False
    return True