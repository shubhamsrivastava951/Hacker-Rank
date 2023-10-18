n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))
print ("{:.1f}".format(np.dot(x,w)/sum(w)))