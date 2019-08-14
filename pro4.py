c2,c3=map(str,input().split())
yas=0
if len(c2)>len(c3):
  c2,c3=c3,c2
p=0
while p<len(c2):
  yas+=(ord(c3[p])-ord(c2[p]))
  p+=1
for p in range(p,len(c3)):
  yas+=ord(c3[p])-ord('a')+1
print(yas)
