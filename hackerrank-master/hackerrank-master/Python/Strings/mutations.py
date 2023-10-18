def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    return "".join(lst)

s = raw_input()
i, c = raw_input().split()
s_new = mutate_string(s, int(i), c)
print s_new