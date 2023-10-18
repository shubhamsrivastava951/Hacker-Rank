from collections import namedtuple
N = (int(input()))
varNames = input().split()
Stu = namedtuple('Stu', varNames)
marks = [int(Stu._make(input().split()).MARKS) for _ in range(N)]
print (sum(marks)/N)