Pnum1 = int(input("입력 진수 결정(16/10/8/2) :"))
Pnum2 = int(input("값 입력 :"), Pnum1)

#진수 변환
Pnum_hex = hex(Pnum2)
Pnum_int = (Pnum2)
Pnum_oct = oct(Pnum2)
Pnum_bin = bin(Pnum2)

#출력하기
print("16진수 ==> ", Pnum_hex)
print("10진수 ==> ", Pnum_int)
print("8진수 ==> ", Pnum_oct)
print("2 ==> ", Pnum_bin)