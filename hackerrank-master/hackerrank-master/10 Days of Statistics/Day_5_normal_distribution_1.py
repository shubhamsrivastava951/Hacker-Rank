import scipy.stats as stats
mu, sigma = map(float, input().split())
x1 = float(input())
x2, x3 = map(float, input().split())
z1 = (x1-mu)/sigma
z2 = (x2-mu)/sigma
z3 = (x3-mu)/sigma

print ("{:.3f}\n{:.3f}".format(stats.norm.cdf(z1, loc = 0, scale = 1),stats.norm.cdf(z3, loc = 0, scale = 1)-stats.norm.cdf(z2, loc = 0, scale = 1)))