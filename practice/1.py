station = '인천공항'
print(''+station+'행 열차가 들어오고 있습니다.')
print(2**3)
print(5%3)
print(10//3)
print(not 1 == 3)
print(3>0 and 3>5)

print(abs(-5))  # 5
print(pow(4,2))  # 4^2 = 16
print(max(5, 12))  #12
print(min(5,12))  # 5
print(round(3.14))  #반올림. 3
print(round(4.99))  #반올림. 5

from math import *
print(floor(4.99))  #내림. 4
print(ceil(3.14))  #올림. 4
print(sqrt(16))  #제곱근. 4

from random import *
print(random())  # 0.0~1.0미만의 임의의 값 생성
print(random() * 10)  # 0.0~10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 11 이하의 임의의 값 생성

from random import *
date = print(int(random() * 28) + 1)
print('오프라인 스터디 모임 날짜는 매월 ',date,'일로 선정되었습니다.')
print('오프라인 스터디 모임 날짜는 매월 (int(random() * 28) + 1) 일로 선정되었습니다.')

date = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월 ',str(date),'일로 선정되었습니다.')

sentence = '나는 소년입니다'
print(sentence)
sentence2 ='''
나는 소년이고,
파이썬은 어려워요
'''
print(sentence2)

jumin = '990120-1234567'
print('성별 : ' ,jumin[7],)
print('성별 : ' + jumin[7])
print('연 :' + jumin[0:2]) # 0부터 2직전까지
print('월 :' + jumin[2:4])
print('생년월일 :' + jumin[:6]) # 처음부터 6직전까지
print('뒤 7자리 :' + jumin[7:])  # 7부터 끝까지
print('뒤 7자리(뒤에부터) :' + jumin[-7:])  # 맨 뒤에서 7번째부터 끝까지

