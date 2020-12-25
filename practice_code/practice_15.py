# 1103 : 폴더명 출력

# printf()함수를 공부하는 진영이는 다음 폴더명을 출력해보기로 했다.

# "c:\test"
# printf함수에는 특별한 제어문자가 몇개 있다.

# 큰따옴표(")를 출력하기 위해선 \" 를 사용해야 하고,

# \를 출력하기 위해선 \\ 를 사용해야 한다.


# 출력 예시

# "c:\test"


# print('"c:\\test"')


# 1106 : int의 범위(pass)

# 앞으로 많이 사용될 변수 int 자료형의 범위를 알아내는 것이 이번 문제의 정답이다.

# int는 정수형이고 32비트 자료형이다.


# 1110 : 정수 그대로 출력하기

# 입력
# 정수를 하나 입력받는다.

# 출력
# 입력받은 정수를 출력한다.

# 입력 예시   
# 5

# 출력 예시
# 5

# 1111 : %출력

# 어떤 정수가 입력되면 %를 붙여 출력하시오.

# 입력 예시   
# 35

# 출력 예시
# 35%

# n = input()

# print(n + "%")

# 1112 : 두 정수 출력


# 입력
# 두 정수를 차례대로 입력받는다.

# 출력
# 입력받은 순서대로 출력한다.

# 입력 예시   
# 5 7

# 출력 예시
# 5 7

# a, b = map(int, input().split())

# print(a,b)

# 1113 : 바꿔서 출력하기

# 입력
# 두 정수를 입력받는다.

# 출력
# 순서를 바꿔서 출력한다.

# 입력 예시   
# 1 2

# 출력 예시
# 2 1

# a,b = map(int, input().split())

# print(b,a)


# 1114 : 두 정수의 덧셈

# 입력
# 두 정수를 입력받는다.

# 출력
# 두정수의 합을 출력한다.

# 입력 예시   
# 5 7

# 출력 예시
# 12


# a, b = map(int, input().split())

# print(a+b)

# 1115 : 두 정수의 덧셈 


# 두 정수의 합을 출력한다.

# 입력 예시   
# 11111111111 22222222222

# 출력 예시
# 33333333333

# a, b = map(int, input().split())

# print(a+b)

# 1116 : 사칙연산 계산기

# 입력
# 두 정수 a, b를 입력받는다.

# 출력
# a와 b에 대한 사칙연산 결과를 양식에 맞추어 출력한다.

# 입력 예시   
# 3 2

# 출력 예시
# 3+2=5
# 3-2=1
# 3*2=6


# a, b = map(int, input().split())

# print(str(a) + "+" + str(b) + "=" + str(a+b))
# print(str(a) + "-" + str(b) + "=" + str(a-b))
# print(str(a) + "*" + str(b) + "=" + str(a*b))
# print(str(a) + "/" + str(b) + "=" + str(a//b))


# 1117 : 두 실수의 곱

# 입력
# 두 실수를 입력받는다.

# 출력
# 두 실수의 곱을 소수 둘째자리까지 출력한다.

# 입력 예시   
# 1.23 4.56

# 출력 예시
# 5.61

# a, b = input().split()

# print( round(float(a) * float(b) ,2))

# 1118 : 삼각형의 넓이 구하기

# 입력
# 밑변(a)과 높이(b)가 정수로 입력된다.

# 출력
# 삼각형의 넓이를 소수 첫째자리까지 출력한다.

# 입력 예시   
# 5 2

# 출력 예시
# 5.0

# a, b = map(int, input().split())

# print(round(a*b*0.5, 1))

# 1119 : 일을 시간으로 변환

# 입력
# 일(day)이 입력된다.

# 출력
# 시간으로 변환해서 출력한다.

# 입력 예시   
# 2

# 출력 예시
# 48

# day = int(input())

# time = day * 24

# print(time)

# 1120 : 세 수의 평균

# 입력
# 세 정수가 입력된다.

# 출력
# 세 수의 평균을 소수 둘째자리까지 출력하시오.

# 입력 예시   
# 1 2 3

# 출력 예시
# 2.00


# a, b, c = map(int, input().split())

# sum = a + b + c
# result = sum / 3

# print(result)              # 출력 값 2.0
# print("%.1f"% result)      # 출력 값 2.0
# print("%.2f"% result)      # 출력 값 2.00
# print("%.3f"% result)      # 출력 값 2.000
# print("%.4f"% result)      # 출력 값 2.0000

# 1121 : 나머지 구하기

# 입력
# 두 정수 a, b를 입력받는다.

# a는 피제수, b는 제수를 나타낸다.

# 예) 7 5 가 입력되었다면  ====>   7  /  5 를 뜻함

# 출력
# 나머지를 출력한다.

# 입력 예시   
# 7 5

# 출력 예시
# 2

# a, b = map(int, input().split())

# result = a % b
# print(result)


# 1122 : 초를 분/초로 변환

# 입력
# 초가 입력된다.(자연수)

# 출력
# 분, 초 순서로 출력한다.

# 입력 예시   
# 70

# 출력 예시
# 1 10


# n = int(input())

# m = n // 60
# s = n - m * 60

# print(m,s)


# 1123 : 섭씨 온도를 화씨 온도로 변환


# 섭씨 온도가 입력되면 화씨 온도로 변환하시오.

# 화씨 온도 = 9 / 5 * 섭씨온도 + 32

# 입력
# 섭씨 온도가 입력된다. (정수)

# 출력
# 화씨온도를 소수 셋째자리 까지 출력한다. (실수)

# 입력 예시   
# 30

# 출력 예시
# 86.000


# c = int(input())

# f = 9 / 5 * c + 32

# print("%.3f"% f)


# 1125 : 8진수 16진수 변환

# 문제 설명    
# 10진수 정수를 입력받아 8진수와 16진수로 출력한다.

# 입력
# 10진수 정수 하나가 입력된다.

# 출력
# 8진수와 16진수를 차례대로 출력한다.

# (16진수는 대문자 출력)

# 입력 예시   
# 10

# 출력 예시
# 12 A

# n = int(input())

# o = format(n, 'o')

# x = format(n, 'x')


# print(o, x.upper())

# 1131 : 문자 출력하기



# 입력
# 문자 하나가 입력된다.

# 출력
# 입력받은문자를 그대로 출력된다.

# 입력 예시   
# a

# 출력 예시
# a

# x = input()

# print(x)

# 1132 : 문자열 출력하기

# 입력 예시   
# cat

# 출력 예시
# cat

# x = input()

# print(x)

# 1133 : 공백이 있는 문자열 입출력

# 입력 예시   
# black sheep wall

# 출력 예시
# black sheep wall

# x = input()

# print(x)

1103
1111-1125
1131-1133