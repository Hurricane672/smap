from codecs import raw_unicode_escape_decode
import re


# pattern = "[0-9]+"
# string ="5701-5709"

# match = re.findall(pattern,string,re.I)
# print(match)
# a=int(match[0])
# b=int(match[1])
# for i in range(a,b+1):
#     print("\""+str(i)+"\",",end="")

# str=[0x61,0x62]
# print((bytes(str)).decode('utf-8'))

# str="\x80\\0\\0\\x28\\x72\\xFE\\x1D\\x13\\0\\0\\0\\0\\0\\0\\0\\x02\\0\\x01\\x86\\xA0\\0\\x01\\x97\\x7C\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0"
# str='\u0061'
# print(str)
# print(str.encode("raw_unicode_escape"))

# print("python编码后的结果：")
# print(str.encode("utf-8"))
# str2=b'\x80\0\0\'


# print("\""+str+"\""+",")        
import re
pattern = re.compile(r'\d+.\d+(.\d+)*')
str ="N   5.72.26-log    /xL/Y=s            ODzMq[q mysql_native_password "
id=pattern.search(str)

print(type(id.group()))