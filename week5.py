# ###  중첩 if

# num = int(input('enter a digit number:'))
# if num > 5:
#     print('your number is more than 5')
#     if num %2 == 0:
#         print(f'{num} is even number')
#     else :
#         print(f'{num} is odd number')

# num = int(input('enter a digit number:'))        
# if num>5 and num %2 == 0:
#     print('your number is more than 5')
#     print(f'{num} is even number')
# elif num>5 and num %2 != 0:
#     print('your number is more than five')
#     print(f'{num} is odd number')

# ### 멤버십 연산자 in / not in
# l = [1,2,3,4,5]
# num = int(input('숫자를 입력하시오:'))
# print(num in l)
# print(3 in l)
# s = ['hello, world']
# text = input('문자 입력하시오:')
# print(text in s)

# members = ['tommy', 'marry', 'jake1234']
# id = input('아이디 입력하시오:')
# if len(id) >= 5 and id not in members:
#     print(id)
# elif len(id) < 5 and id not in members:
#     print('아이디가 5자 이상이여야 합니다')
# elif len(id) >= 5 and id in members:
#     print('기존 멤버의 아이디와 겹칩니다')

# count = 0
# while count < 10:   
#     count += 1
#     print(f'나무를 {count}번 찍었습니다')
#     if count == 10:
#         print('나무 넘어간다')

# members = ['tommy', 'marry', 'jake1234']
# id = input('아이디 입력하시오:')

# if len(id) >= 5 and id not in members:
#     print(f'welcome, {id}')
#     members.append(id)
# else:
#     print('try again')
# print(members)

# ###로그인 pg
# trylog = 3  #반복할 횟수

# while trylog > 0:
#     #  trylog -= 1
#     print('로그인')
#     log_id = input('아이디 입력:')
#     if log_id in members:
#         print('로그인 성공')
#         break
#     else:
#         print('로그인 실패, 다시 입력해주세요')
#     trylog -= 1

# star = int(input('별 출력 횟수 입력:'))
# while star > 0:
#     print('*'*star)
#     star -= 1

# cnt = int(input('횟수 입력:'))
# star = 1
# while star <= cnt:
#     print('*'*star)
#     star += 1
    
# member = ['tommy', 'marry', 'jake1234']
# while True:
#     logid = input('아이디 입력:')
#     if logid in member:
#         print('login success')
#         break
#     else:
#         print('try again')

# school = []
# while True :
#     reply = input('학교에 가면? :')
#     if reply not in school:
#         school.append(reply)
#         print(f'{school}이 있고')
#     else:
#         print('탈락')

# l = []
# total = 0
# while True :
#     numm = int(input('숫자 입력:'))
#     if numm !=0:
#         l.append(numm)
#         total += numm   # total = total + num
       
#     else:
#         break  
# print(total)

# l = []
# while True :
#     if: numm = int(input('숫자 입력:'))
#     else: numm = str(input('숫자입력:'))
#         if numm !=0:
#             l.append(numm)
#         else:
#             print(l)
#             print(sum(l))
#             break 

l = []

if: numm = int(input('숫자 입력:'))
else: numm = str(input('숫자입력:'))
 while True :
    if numm !=0:
        l.append(numm)
    else:
        print(l)
        print(sum(l))
        break 