import math
tckts_left = float(input())
students_left = int(input())
mu = float(input())
sigma = float(input())
def cdf(x, mu, sigma):
    val = 0.5 *(1+ math.erf((x-mu)/(sigma * math.sqrt(2))))
    return val
val = cdf(tckts_left, mu*students_left, sigma * math.sqrt(students_left))
print (val)