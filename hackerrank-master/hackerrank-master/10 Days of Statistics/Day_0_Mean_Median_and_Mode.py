import numpy as np
from scipy import stats
n = int(input())
nums = list(map(int,input().split()))
print (np.mean(nums), np.median(nums), *stats.mode(nums)[0], sep="\n")