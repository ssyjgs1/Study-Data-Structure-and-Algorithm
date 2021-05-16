"""
# 세 정수를 입력받아 최댓값 구하기

print("세 정수의 최댓값을 구합니다.")
a=int(input("정수 a값을 입력하세요. : "))
b=int(input("정수 b값을 입력하세요. : "))
c=int(input("정수 c값을 입력하세요. : "))
max=a
if b > max:
    max=b
if c >max:
    max=c
print(f'최댓값은 {max}입니다.')
"""

"""
# 이름을 입력받아 인사하기
print("이름을 입력하세요. :", end=' ')
name=input() # input 함수를 통해 문자열(str) 형태의 값을 얻을 수 있음
print(f'안녕하세요? {name}님.')

# 이름을 입력받아 인사하기
name=input('이름을 입력하세요.: ')
print(f'안녕하세요? {name}님.')
"""

"""
#세 정수의 최댓값 구하기
def max3(a,b,c):
    print("세 수의 최댓값을 구하여 반환")
    max=a
    if b > max:
        max=b
    if c > max:
        max=c
    return max # 최댓값 반환
print(f'max3(3,2,1) = {max3(3,2,1)}')
print(f'max3(3,2,2) = {max3(3,2,2)}')
print(f'max3(3,1,2) = {max3(3,1,2)}')
print(f'max3(3,2,3) = {max3(3,2,3)}')
print(f'max3(2,1,3) = {max3(2,1,3)}')
print(f'max3(3,3,2) = {max3(3,3,2)}')
print(f'max3(3,3,3) = {max3(3,3,3)}')
print(f'max3(2,2,3) = {max3(2,2,3)}')
print(f'max3(2,3,1) = {max3(2,3,1)}')
print(f'max3(2,3,2) = {max3(2,3,2)}')
print(f'max3(1,3,2) = {max3(1,3,2)}')
print(f'max3(2,3,3) = {max3(2,3,3)}')
print(f'max3(1,2,3) = {max3(1,2,3)}')
"""

"""
#세 정수를 입력받아 중앙값 구하기 1
def med3(a,b,c):
    # a,b,c의 중앙값을 구하여 반환
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else :
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else :
        return b
print('세 정수의 중앙값을 구합니다.')
a=int(input("정수 a"))
b=int(input("정수 b"))
c=int(input("정수 c"))
print(f'중앙값은 {med3(a,b,c)}입니다.')
"""

"""
# 입력받은 정수의 부호 출력하기
n=int(input())
if n > 0:
    print('+')
elif n < 0:
    print('-')
else :
    print('0')
"""

"""
#1부터 n까지 정수의 합 구하기 1(while문)
print('1부터 n까지 정수의 합을 구합니다.')
n=int(input("input n :"))
sum=0
i=1  # 반복을 제어할 때 사용하는 i를 카운터용 변수라고 함
while i <= n:
    sum = sum+i
    i=i+1
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
print(f'i값은 {i}입니다.')
"""

"""
# 1부터 n까지의 정수의 합 구하기 2(for문)
print('from 1 to n, find a sum of ints')
n=int(input('input n'))
sum=0
for i in range(1,n+1):
    sum += i
print(f'from 1 to {n}, sum of ints is {sum}.')
"""

"""
# 가우스의 덧셈으로 정수의 합 구하기
n=int(input('input n'))
sum = n * (n+1) // 2
print(sum)
"""

# range(n) 0 이상 n 미만인 수를 차례로 나열하는 수열
# range(a,b) a 이상 b 미만인 수를 차례로 나열하는 수열
# range(a,b,step) a 이상 b 미만인 수를 step 간격으로 나열하는 수열
# 이터러블 객체는 반복할 수 있는 객체를 말함

"""
# a부터 b까지 정수의 합 구하기 (for문)
print('from a to b, calc a sum')
a=int(input('input a'))
b=int(input('input b'))
if a > b:
    a,b=b,a
sum=0
for i in range(a,b+1):
    sum += i
print(f'from {a} to {b}, sum of ints is {sum}.')
"""

"""
# a부터 b까지 정수의 합 구하기 1
print('a부터 b까지 정수의 합을 구합니다.')
a=int(input('input a'))
b=int(input('input b'))
if a>b:
    a,b=b,a
sum=0
for i in range(a,b+1):
    if i < b:
        print(f'{i} +', end='')
    else :
        print(f'{i} =', end='')
    sum = sum + i
print(sum)
"""

"""
# a부터 b까지  정수의 합 구하기 2
print('a부터 b까지 정수의 합을 구합니다.')
a=int(input('input a'))
b=int(input('input b'))
if a > b:
    a,b=b,a
sum=0
for i in range(a,b):
    print(f'{i} + ', end='')
    sum=sum+i
print(f'{b} = ', end='')
sum=sum+b
print(sum)
"""

"""
# +와 -를 번갈아 출력하기 1
print('+와 -를 번갈아 출력합니다.')
n=int(input('몇 개를 출력할까요? :'))
for i in range(n):
    if i % 2 :
        print('-', end='')
    else :
        print('+', end='')
print()
"""

"""
print(bool(5%5))
"""

"""
# +와 -를 번갈아 출력하기 1 (for문 수정)
print('+와 -를 번갈아 출력합니다.')
n=int(input('몇 개 출력할까요?:'))
for i in range(1,n+1):
    if i % 2:
        print('+', end='')
    else :
        print('-',end='')
print()
"""

"""
# +와 -를 번갈아 출력하기 2
print('+와 -를 번갈아 출력합니다.')
n=int(input('몇 개를 출력할까요?:'))
for _ in range(n//2):  #무시하고 싶은 값을 언더스코어(_)로 표현할 수 있다.
    print('+-',end='')
if n % 2:
    print('+',end='')
print()
"""

"""
# *를 n개 출력하되 w개마다 줄바꿈하기 1
print('*를 출력합니다.')
n=int(input('몇 개를 출력할까요?:'))
w=int(input('몇 개마다 줄바꿈할까요?:'))
for i in range(n):
    print('*',end='')
    if i % w == w-1: # n번 판단
        print()      # 줄바꿈
if n % w:   # 1번 판단
    print() # 줄바꿈
"""

"""
# *를 n개 출력하되 w개마다 줄바꿈하기 2
print('*를 출력합니다.')
n=int(input('몇 개를 출력할까요?: '))
w=int(input('몇 개마다 줄바꿈할까요?: '))
for _ in range(n//w):  # n//w번 반복
    print('*' * w)
rest = n % w
if rest:   # if문 판단 1번
    print('*' * rest)
"""

"""
# 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)
print('1부터 n까지 정수의 합을 구합니다.')
while True:
    n=int(input('n값을 입력하세요.: '))
    if n > 0:
        break  #n이 0보다 커질 때까지 반복
sum=0
i=1
for i in range(1,n+1):
    sum += i #sum에 i를 더함
    i += 1   #i에 1을 더함
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
"""

"""
# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기 (약수 나열)
area=int(input('직사각형의 넓이를 입력하세요. :'))
for i in range(1,area+1):  # 1부터 사각형의 넓이 계산
    if i * i > area:
        break
    if area % i:
        continue
    print(f'{i} x {area // i}')
"""

"""
# 10~99 사이의 난수 n개 생성하기 (13이 나오면 중단)
import random
n=int(input('난수의 개수를 입력하세요. :'))
for _ in range(n):
    r=random.randint(10,99)
    print(r, end=" ")
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else:
    print('\n난수 생성을 종료합니다.')
"""

"""
# 1~12까지 8을 건너뛰고 출력하기 1
for i in range(1,13):
    if i == 8:
        continue
    print(i, end=' ')
print()
"""

"""
# 1부터 12까지 8을 건너뛰고 출력하기 2
for i in list(range(1,8)) + list(range(9,13)):
    print(i, end=' ')
print()
"""

"""
# 2자리 양수(10~99) 입력받기
print('2자리 양수를 입력하세요.')
while True:
    no = int(input("값을 입력하세요. :"))
    if no >= 10 and no <= 99:
        # if 10 <= no <= 99:
        # if not(no < 10 or no > 99):
        break
print(f'입력받은 양수는 {no}입니다.')
"""

"""
# 구구단 곱셈표 출력하기
print('-' * 27)
for i in range(1,10):
    for j in range(1,10):
        print(f'{i * j:3}', end=' ')    # i * j를 3자리로 출력하라는 말
    print()
print('-' * 27)
"""

"""
# 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기
print('왼쪽 아래가 직각인 이등변삼각형을 출력합니다.')
n=int(input('짧은 변의 길이를 입력하세요. :'))
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()  # 줄바꿈
"""

"""
# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기
print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n=int(input('짧은 변의 길이를 입력하세요. :'))
for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')
    print()
"""

"""
#함수 내부, 외부에서 정의한 변수와 객체의 식별 번호를 출력하기
n=1
def put_id():
    x=1
    print(f'id(x) = {id(x)}')
print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()
"""

"""
# 1부터 100까지 반복하여 출력하기
for i in range(1,101):
    print(f'i={i:3} id(i) = {id(i)}')
"""

