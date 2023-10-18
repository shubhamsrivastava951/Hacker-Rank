n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))
wt_prod=0
for i in range(len(x)):
    wt_prod += x[i]*w[i]

print ("{:.1f}".format(wt_prod/sum(w)))