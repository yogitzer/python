inFp = None
inList = ""

inFp = open("C:\\Users\\태은\\Desktop\\파이썬\\python\\filetest\\data1.txt","r",encoding="UTF=8")  
inList = inFp.readlines()
print(inList)

inFp.close()