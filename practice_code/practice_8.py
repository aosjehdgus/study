# # 1084 : [기초-종합] 빛 섞어 색 만들기

# 빨강(red), 초록(green), 파랑(blue) 빛을 섞어
# 여러 가지 빛의 색을 만들어 내려고 한다.

# 빨강(r), 초록(g), 파랑(b) 각각의 빛의 개수가 주어질 때,
# (빛의 강약에 따라 0 ~ n-1 까지 n가지의 빛 색깔을 만들 수 있다.)

# 주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과
# 총 가짓 수를 계산해보자.

# 입력
# 빨녹파(r, g, b) 각 빛의 강약에 따른 가짓수(0 ~ 128))가 공백을 사이에 두고 입력된다.
# 예를 들어, 3 3 3 은 각 색깔 빛에 대해서 그 강약에 따라 0~2까지 3가지의 색이 있음을 의미한다.


# 출력
# 만들 수 있는 rgb 색의 정보를 오름차순(계단을 올라가는 순, 12345... abcde..., 가나다라마...)으로
# 줄을 바꿔 모두 출력하고, 마지막에 그 개수를 출력한다.


# 입력 예시   
# 2 2 2

# 출력 예시
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
# 8

# r, g, b = input().split()

# for i in range(int(r)):

         
#     for j in range(int(g)):


#         for k in range(int(b)):

#             print(i, j, k)
#             k = k + 1

# print(int(r) * int(g) * int(b))    

# 1085 : [기초-종합] 소리 파일 저장용량 계산하기

# 소리가 컴퓨터에 저장될 때에는 디지털 데이터화 되어 저장된다.

# 마이크를 통해 1초에 적게는 수십 번, 많게는 수만 번 소리의 강약을 체크해
# 그 값을 정수값으로 바꾸고, 그 값을 저장해 소리를 파일로 저장할 수 있다.

# 값을 저장할 때에는 비트를 사용하는 정도에 따라 세세한 녹음 정도를 결정할 수 있고,
# 좌우(스테레오) 채널로 저장하면 2배… 5.1채널이면 6배의 저장공간이 필요하고,
# 녹음 시간이 길면 그 만큼 더 많은 저장공간이 필요하다.

# 1초 동안 마이크로 소리강약을 체크하는 수를 h
# (헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

# 한 번 체크한 결과를 저장하는 비트 b
# (2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

# 좌우 등 소리를 저장할 트랙 개수인 채널 c
# (모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

# 녹음할 시간 s가 주어질 때,

# 필요한 저장 용량을 계산하는 프로그램을 작성해보자.

# 실제로 일반적인 CD 음질(44.1KHz, 16bit, 스테레오)로 1초 동안 저장하려면
# 44100 * 16 * 2 * 1 bit의 저장공간이 필요하다.

# 이렇게 녹음하는 방식을 PCM(Pulse Code Modulation) 방법이라고 하는데,
# 압축하지 않은 순수한(raw) 소리 데이터 파일은 대표적으로 *.wav 가 있다.

# **
#       8 bit(비트)           = 1byte(바이트)     //       8bit=1Byte
# 1024 Byte(210 byte) = 1KB(킬로 바이트) // 1024bit=1KB
# 1024 KB(210 KB)      = 1MB(메가 바이트)
# 1024 MB(210 MB)     = 1GB(기가 바이트)
# 1024 GB(210 GB)      = 1TB(테라 바이트)
 



# 입력
# h, b, c, s 가 공백을 두고 입력된다.
# h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.

 

# 출력
# 필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
# 단, 소수점 둘째 자리에서 반올림해 첫째 자리까지 출력하고 MB를 공백을 두고 출력한다.

# 입력 예시   
# 44100 16 2 10

# 44100 

# 출력 예시
# 1.7 MB

# h, b, c, s = input().split()

# bit = int(h) * int(b) * int(c) * int(s)
# byte = bit / 8
# kbyte = byte / 1024
# mbyte = round(kbyte / 1024, 1)

# print(str(mbyte) + " MB")


# 1086 : [기초-종합] 그림 파일 저장용량 계산하기

# 이미지가 컴퓨터에 저장될 때에도 디지털 데이터화 되어 저장된다.

# 가장 기본적인 방법으로는 그림을 구성하는 한 점(pixel, 픽셀)의 색상을
# 빨강(r), 초록(g), 파랑(b)의 3가지의 빛의 세기 값으로 따로 변환하여 저장하는 것인데,

# 예를 들어 r, g, b 각 색에 대해서 8비트(0~255, 256가지 가능)씩을 사용한다고 하면,

# 한 점의 색상은 3가지 r, g, b의 8비트+8비트+8비트로 총 24비트로 표현해서
# 총 2^24 가지의 서로 다른 빛의 색깔을 사용할 수 있는 것이다.

# 그렇게 저장하는 점을 모아 하나의 큰 이미지를 저장할 수 있게 되는데,
# 1024 * 768 사이즈에 각 점에 대해 24비트로 저장하면 그 이미지를 저장하기 위한
# 저장 용량을 계산할 수 있다.

# 이렇게 이미지의 원래(raw) 데이터를 압축하지 않고 그대로 저장하는 대표적인 이미지 파일이
# *.bmp 파일이며, 비트로 그림을 구성한다고 하여 비트맵 방식 또는 래스터 방식이라고 한다.

# 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
# 압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.


# 예를 들어
# 일반적인 1024 * 768 사이즈(해상도)의 각점에 대해
# 24비트(rgb 각각 8비트씩 3개)로 저장하려면 1024 * 768 * 24 bit의 저장 용량이 필요하다.

# 실제 그런지 확인하고 싶다면, 간단한 그림 편집/수정 프로그램을 통해 확인할 수 있다.


# **
#       8 bit(비트)           = 1byte(바이트)     //       8bit=1Byte
# 1024 Byte(210 byte) = 1KB(킬로 바이트) // 1024bit=1KB
# 1024 KB(210 KB)      = 1MB(메가 바이트)
# 1024 MB(210 MB)     = 1GB(기가 바이트)
# 1024 GB(210 GB)      = 1TB(테라 바이트)




# 입력
# w, h, b 가 공백을 두고 입력된다.
# 단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.


# 출력
# 필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
# 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력한 뒤 MB를 출력한다.


# 입력 예시   
# 1024 768 24

# 출력 예시
# 2.25 MB

# import decimal

# w, h, b = input().split()

# bit = int(w) * int(h) * int(b)

# byte = bit / 8
# kbyte = byte / 1024

# x, y = decimal.Decimal(kbyte) , decimal.Decimal(1024)

# mbyte = round(x / y, 2)

# print(str(mbyte) + " MB")

# from decimal import Decimal

# result_0 = Decimal('1.1') + Decimal('2.2')
# result_1 = Decimal(1.1) + Decimal(2.2)

# print(result_0)   # 문자열을 사용했을 때,
# print(result_1)   # 숫자(int or float)를 사용했을 때, 기본 값 28자리를 가짐
# print(1.1 + 2.2)  # 숫자 연산(이진 연산)

# result_2 = Decimal('8.95') * Decimal('100')
# result_3 = Decimal(8.95) * Decimal(100)

# print(result_2)   # 문자열을 사용했을 때,
# print(result_3)   # 숫자(int or float)를 사용했을 때, 기본 값 28자리를 가짐
# print(8.95 * 100) # 숫자 연산(이진 연산)


