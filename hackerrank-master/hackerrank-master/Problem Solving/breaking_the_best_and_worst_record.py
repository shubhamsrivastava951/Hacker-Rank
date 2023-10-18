# Complete the breakingRecords function below.
def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    low = 0
    high = 0
    for score in scores:
        if score> max:
            high, max = high+1, score            
        elif score<min:
            low, min = 1+low, score
    return (high,low)