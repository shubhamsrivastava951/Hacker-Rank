def wrap(string, max_width):
    return '\n'.join([string[i:i+max_width] for i in range(0,len(string),max_width)])

# Takes two input : first input is the string, second is maximum width of paragraph
string, max_width = raw_input(), int(raw_input()) 
result = wrap(string, max_width)
print result