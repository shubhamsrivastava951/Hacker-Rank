bill = OrderedDict()
N = int(input())
for _ in range(N):
    name, space, price = input().rpartition(' ')
    if name not in bill.keys():
        bill[name] = int(price)
    else:
        bill[name] += int(price)
for k in bill:
    print (k,bill[k])