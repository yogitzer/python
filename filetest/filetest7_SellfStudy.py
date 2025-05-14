# outFp= None
# outStr = ""

# outFp = open("C:\\Users\\태은\\Desktop\\파이썬\\python\\filetest\\temp\\data2.txt","w")

# while True:
#     outStr = input("내용 입력: ")
#     if outStr != "":
#         outFp.writelines(outStr + "\n")
#     else:
#         break

# outFp.close()
# print("---정상적으로 파일에 씀---")

outFp= None
outStr = ""

fName = input("파일명을 입력하세요: ")
outFp = open(fName, "w", encoding= "utf-8")  

while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("---정상적으로 파일에 씀---")