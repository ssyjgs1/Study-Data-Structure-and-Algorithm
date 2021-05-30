"""
# 학생 5명의 시험 점수를 입력받아 합계와 평균을 출력하기
print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1=int(input('1번 학생의 점수를 입력하세요. : '))
score2=int(input('2번 학생의 점수를 입력하세요. : '))
score3=int(input('3번 학생의 점수를 입력하세요. : '))
score4=int(input('4번 학생의 점수를 입력하세요. : '))
score5=int(input('5번 학생의 점수를 입력하세요. : '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계는 {total}점입니다.')
print(f'평균은 {total / 5}점입니다.')
"""

"""
# 리스트와 튜플 풀어내기 (unpack)
x = [1,2,3]
a, b, c = x
print(a, b, c)
"""

'''
# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형 a원소의 최댓값을 반환"""
    maximum=a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요. :'))
    x = [None] * num     # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요. :'))

    print(f'최댓값은 {max_of(x)}입니다.')


# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)

from max import max_of

print('배열의 최댓값을 구합니다.')
print('주의 : "End"를 입력하면 종료합니다.')

number=0
x=[]     # 빈 리스트
while True:
    s = input(f'x[{number}]값을 입력하세요. :')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')
'''