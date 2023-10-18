import statistics
n = int(input())
x1 = list(map(float,input().split()))
y1 = list(map(float,input().split()))
mu1 = statistics.mean(x1)
mu2 = statistics.mean(y1)
sigma1 = statistics.pstdev(x1) 
sigma2 = statistics.pstdev(y1)
def pearson_corr(x1,y1,mu1,mu2,sigma1,sigma2):
    rho = 0
    for x,y in zip(x1,y1):
        rho += (x-mu1)*(y-mu2)/(n * sigma1 * sigma2)
    return rho
val =pearson_corr(x1,y1,mu1,mu2,sigma1,sigma2)
print ("{:.3f}".format(val))