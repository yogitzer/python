inFp = None
inList, inStr = [], ""

inFp = open("C:\\Users\\태은\\Desktop\\파이썬\\python\\filetest\\temp\\data1.txt","r",encoding="UTF=8")  
inList = inFp.readlines()
count = 1
for inStr in inList:
    print("%d: %s"%(count,inStr), end="")
    count += 1

inFp.close()