# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (v2 >= v1):
        return "NO"
    elif (x2-x1)%(v2-v1) == 0:
        return "YES"
    return "NO"