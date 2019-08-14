    
c,b=input().split()
char=abs(len(b)-len(c))
for g in range(len(c)):
  if(len(b)==1 and b[g] in c):
    break
  if(c[g]!=b[g]):
    char=char+1
print(char)
