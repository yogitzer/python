inFp = None
inList, inStr = [], ""

inFp = open("C:\\Users\\태은\\Desktop\\파이썬\\python\\filetest\\data1.txt","r",encoding="UTF=8")  
inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")

inFp.close()