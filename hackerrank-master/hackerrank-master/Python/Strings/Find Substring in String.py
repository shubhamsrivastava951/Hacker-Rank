# Rudimentary approach without using in-built functions
def count_substring(string, sub_string):
    cnt_str = 0
    cnt_sub = 0
    match = 0		# Tracks number of matches
    start = -1		# Tracks where the beginning of substring match is found
    flag = 0		# Tracks string and substring counter reset
    while cnt_str<len(string):
        if string[cnt_str] == sub_string[cnt_sub]:
            if cnt_sub == 0:
                start = cnt_str
                flag = 1
            elif cnt_sub == len(sub_string)-1:
                match +=1
                cnt_str = start + 1
                cnt_sub = 0
                continue
            cnt_sub += 1
            cnt_str +=1
        elif flag ==1:
            cnt_sub = 0
            cnt_str = start + 1
            flag = 0
        else :
            cnt_str +=1
                      
    return match

# Enter String in first input, substring in second
string = raw_input().strip()
sub_string = raw_input().strip()    
count = count_substring(string, sub_string)
print count