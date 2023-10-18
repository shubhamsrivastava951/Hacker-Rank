# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
M1 = set(map(int,input().split()))
N = int(input())
N1 = set(map(int,input().split()))
s  = sorted(M1.symmetric_difference(N1))
print (*s, sep="\n")

