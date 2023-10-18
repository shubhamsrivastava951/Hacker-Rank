from collections import deque
N = int(input())
d = deque()
for _ in range(N):
    cmd, *val = input().split()
    getattr(d,cmd)(*val)
print(*[item for item in d])