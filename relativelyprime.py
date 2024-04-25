def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def coprime(a,b):
    return gcd(a,b)==1
print(coprime(14,13))


