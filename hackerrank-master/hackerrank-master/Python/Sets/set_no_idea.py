n, m = input().split()
arr = input().split()
m1 = set(input().split())
m2 = set(input().split())
happy=0
for a in arr:
    if a in m1:
        happy += 1
    if a in m2:
        happy -= 1
print (happy) 