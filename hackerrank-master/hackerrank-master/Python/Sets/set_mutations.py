(_, A) = (int(input()),set(map(int, input().split())))
B = int(input())
for _ in range(B):
    (command, newSet) = (input().split()[0],set(map(int, input().split())))
    getattr(A, command)(newSet)

print (sum(A))