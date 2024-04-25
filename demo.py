def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
a=220
b=15
print("gcd(",a,",",b,")=",gcd(a,b))