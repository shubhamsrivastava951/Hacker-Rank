from textwrap import wrap
def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    for x in range(0, n, k):
        substring = string[x : x+k]
        l=[]
        for s in substring:
            if s not in l:
                l.append(s)
        print ("".join(l))