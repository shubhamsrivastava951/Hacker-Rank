from itertools import combinations
n = int(input())
s = input().split()
k = int(input())
counter=0
for i in list(combinations(s,k)):
    if 'a' in i:
        counter +=1
print ("{0:.3}".format(counter/len(list(combinations(s,k)))))  