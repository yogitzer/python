inFp, outFp = None, None
inStr = ""

fName = input("파일명을 입력하세요: ")
inFp = open(fName, "r", encoding= "utf-8")  
fName2 = input("파일명을 입력하세요: ")
outFp = open(fName2, "w", encoding= "utf-8")  

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)
inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---")