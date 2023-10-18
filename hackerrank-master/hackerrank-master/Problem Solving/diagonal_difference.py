# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    s1 = 0
    s2 = 0
    n = len(arr)
    for i in range(n):
        s1 = arr[i][i] + s1
        s2 = arr[i][n-i-1] + s2
    return abs(s1-s2)


n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print (result)