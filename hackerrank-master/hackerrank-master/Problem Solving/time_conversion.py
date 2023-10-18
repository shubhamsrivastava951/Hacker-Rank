def timeConversion(s):
    #
    # Write your code here.
    #
    if (s[-2:] == "PM") & (s[:2] != "12"):
        k = int(s[:2])+12
        s = str(k)+s[2:]
    elif (s[-2:] == "AM") & (s[:2] == "12"):
        s = "00"+s[2:]
    return s[:-2]

timeConversion("12:05:45AM")