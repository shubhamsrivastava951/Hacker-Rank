b, g = map(float, input().split())
pb = b/(g+b)
pg = 1 - pb

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

prob = (combination(6,0)*pow(pb, 0)*pow(pg, 6))+(combination(6,1)*pow(pb, 1)*pow(pg, 5))+(combination(6,2) * pow(pb, 2) * pow(pg, 4))
print (round(1-prob,3))