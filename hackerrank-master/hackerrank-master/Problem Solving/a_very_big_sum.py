# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return reduce(lambda x, y: x + y, ar, 0)

def reduce(func, arr, s):
    for v in arr:
        s = func(s, v)
    return s