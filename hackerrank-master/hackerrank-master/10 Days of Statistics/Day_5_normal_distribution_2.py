import math
mean, std = map(float,input().split())
x1 = float(input())
x2 = float(input())
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# greater than 80
print('{:.2f}'.format((1 - cdf(x1))*100.00))
# greater than equal to 60
print('{:.2f}'.format((1-cdf(x2))*100.00))
# less than 60
print('{:.2f}'.format(cdf(x2)*100.00))