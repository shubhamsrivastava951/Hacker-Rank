# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
words = OrderedDict()
N = int(input())
for _ in range(N):
    k = input()
    if k not in words.keys():
        words[k] = 1
    else:
        words[k] += 1
print(len(words))
x = words.values()
print (*x)
