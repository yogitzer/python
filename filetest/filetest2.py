inFp=None
inStr=""

inFp=open("C:\\Users\\태은\\Desktop\\파이썬\\python\\filetest\\data1.txt","r",encoding="UTF=8")


while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print(inStr, end="")


inFp.close()