s, n = input().split()
n = int(n)
print (*["".join(i) for i in list(permutations(sorted(s), n))], sep='\n')