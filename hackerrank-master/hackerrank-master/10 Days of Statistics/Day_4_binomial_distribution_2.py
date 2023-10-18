r, n = list(map(int, input().split()))
r = float(r/100)
def binomial(n, k, p):
    return combination(n,k) * pow(p,k) * pow(1-p, n-k)
def combination(n, k):
    return factorial(n)/(factorial(k)* factorial(n-k))
def factorial(n):
    return 1 if n==0 else n * factorial(n-1)
prob1 = round(sum([binomial(n,i,r) for i in range(3)]),3)
prob2 = round(sum([binomial(n,i,r) for i in range(2,11)]),3)
print ("{:.3f}\n{:.3f}".format(prob1,prob2))