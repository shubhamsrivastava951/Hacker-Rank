import math
def factorial(x):
    return 1 if x==0 else x*factorial(x-1)
def poisson(l, x):
    return round((l**x)* math.exp(-l)/factorial(x),3)

out = poisson(float(input()),int(input()))
print (out)