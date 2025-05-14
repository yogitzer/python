inFp=None
inStr=""

inFp=open("C:\\Users\\태은\\Desktop\\파이썬\\python\\filetest\\data1.txt","r",encoding="UTF=8")

inStr=inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")

inFp.close()