def print_formatted(number):
    # your code goes here
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        print " ".join([eval('format'+ "(" + 'i' + "," + "'"+ f + "'" +").rjust(w)") for f in ['d', 'o', 'x', 'b']] )

n = int(raw_input())
print_formatted(n)