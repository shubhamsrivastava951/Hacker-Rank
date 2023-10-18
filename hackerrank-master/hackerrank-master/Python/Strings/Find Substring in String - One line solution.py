# One line solution using List comprehension
def count_substring(string, sub_string):   
    return (sum([ 1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string]))

# Enter String in first input, substring in second
string = raw_input().strip()
sub_string = raw_input().strip()    
count = count_substring(string, sub_string)
print count
