mytype = int(input("입력 진수 결정(16/10/8/2) : "))
value = input("값 입력 : ")
num = int(value, mytype)

print("16진수 ==> ", hex(num))
print("10진수 ==> ", num)
print("8진수 ==> ", oct(num))
print("2진수 ==> ", bin(num))
