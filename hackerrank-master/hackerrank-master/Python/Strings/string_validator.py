s = raw_input()
# tests if string contains alphanumeric, alphabetic, digit, lower and uppercase 
for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    print any(eval('c.'+test+"()") for c in s)