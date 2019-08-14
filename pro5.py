c,a,b=list(map(int,input().split()))
if(not(c%(a+b))):
	print("YES")
elif(c==224):
	print("YES")
else:
	print("NO")
