s, n = input().split()
print (*["".join(j) for j in list(combinations_with_replacement(sorted(s), int(n)))], sep="\n")