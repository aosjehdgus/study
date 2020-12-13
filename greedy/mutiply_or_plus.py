# 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 
# 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 
# 큰 수를 구하는 프로그램을 작성하세요.

# 단, + 보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 
# 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

# 예를 들어, 02984라는 문자열로 만들 수 있는 가장 큰 수는 
# ((((0+2) x 9) x 8) x 4) = 576 입니다. 또한 만들어질 수 있는
# 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

# 0이거나 1인 경우에는 곱하기 보다 더하기를 하는 것이 
# 더 큰 수를 만들 수 있다.

data = input()

result = int(data[0])

for i in range(1, len(data)):
# 두 수 중에서 하나라도 0이나 1인 경우에는 더하기를 수행한다.
    num = int(data[i])
    if num <= 1 or result <=1:
        result += num
# 나머지 수는 곱하기를 수행한다.        
    else :
        result *= num

print(result)    

        



 