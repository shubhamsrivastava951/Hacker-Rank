n = int(input())
mu = float(input())
sigma = float(input())
pct = float(input())
z_score = float(input())
n_error = sigma/n**0.5
print ("{:.2f}\n{:.2f}".format( mu-z_score*n_error,mu+z_score*n_error))