import re


pattern = "[0-9]+"
string ="5701-5709"

match = re.findall(pattern,string,re.I)
print(match)
a=int(match[0])
b=int(match[1])
for i in range(a,b+1):
    print("\""+str(i)+"\",",end="")