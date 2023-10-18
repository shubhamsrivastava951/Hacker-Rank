import math
max_wt = float(input())
boxes = int(input())
mu = float(input())
sigma = float(input())
def cdf(x, mu, sigma):
    val = 0.5 *(1+ math.erf((x-mu)/(sigma * math.sqrt(2))))
    return val
val = cdf(max_wt, mu*boxes, sigma * math.sqrt(boxes))
print (val)