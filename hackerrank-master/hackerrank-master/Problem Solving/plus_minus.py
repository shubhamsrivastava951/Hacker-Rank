def plusMinus(arr):
    n = len(arr)
    pos=0
    neg=0
    zer =0
    for i in arr:
        if i>0:
            pos +=1 
        elif i<0:
            neg +=1
        else:
            zer += 1    
    print ("{:.6f}\n{:.6f}\n{:.6f}".format(pos/n, neg/n, zer/n))