num, den = map(int, input().split())
n = int(input())
p = num/den
prob = round(sum([pow(1-p,i-1) * p for i in range(1,6)]),3)
print ("{}".format(prob))