from collections import Counter
num_shoes = int(input())
shoes = Counter(map(int, input().split()))
num_cust = int(input())
earnings = 0

for i in range(num_cust):
    size, price = map(int, input().split())
    if shoes[size]: # shorter : if dictionary contains non-zero entry for the key
        earnings += price
        shoes[size] -= 1

print (earnings)