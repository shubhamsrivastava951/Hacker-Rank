num, den = map(int, input().split())
n = int(input())
p = num/den
print ("{:.3f}".format(pow(1-p,n-1) * p))