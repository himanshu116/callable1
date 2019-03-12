from re import *
num=0
matches=finditer("[ab1]","aaaaaabbbbbb12abbb")
for i in matches:
	print(i.start(),"--",i.end(),"--",i.group())
	num=num+1
print("total matches is--",num)
