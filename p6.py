shen,vig=map(str,input().split())
if(len(shen)!=len(vig)):
 print("no")
else:
 s3=[shen.count(i) for i in shen]
 s4=[vig.count(i) for i in vig]
if(s3==s4):
 print("yes")
else:
 print("no")
 #b
