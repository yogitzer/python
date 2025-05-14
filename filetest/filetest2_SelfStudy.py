inFp=None
inStr=""

inFp=open("C:\\Users\\태은\\Desktop\\파이썬\\python\\filetest\\temp\\data1.txt","r",encoding="UTF=8")

count = int(1)
while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print("%d: %s"%(count,inStr), end="")
    count += 1


inFp.close()