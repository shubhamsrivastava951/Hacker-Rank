def birthdayCakeCandles(ar):
    max = 0
    cnt = 0
    for i in ar:
        if i > max:
            max = i
            cnt = 0
        if i == max:
            cnt +=1
    return cnt