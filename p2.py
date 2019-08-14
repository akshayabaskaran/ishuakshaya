from itertools import combinations
N,p=map(int,input().split())
q=len(str(N))
lst=list(combinations(str(N),q-p))
lst=sorted(lst)
print(*lst[0],sep='')
