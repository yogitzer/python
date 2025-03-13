import math
r = float(input("원의 반지름을 입력해주세요.\n"))
circle_length = r * math.pi * 2
circle_area = r ** 2 * math.pi
print("반지름이",r ,"인 원의 둘레는 %.2f 이고 넓이는 %.2f 입니다." %(circle_length, circle_area))