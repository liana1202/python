# ###튜플 생성
# t1 = (1,2,3)
# t2 = 'a', 'b', 'c'
# print(t1)
# print(t2)
# print(t1+t2)
# print(t2*2)
# print(t1[0])
# print(t2[1:3])

# ## 리스트 복사
# l1 = [1, 2, 3]
# l2 = list(l1)  # 또는 l1[:]
# print(l1)
# print(l2)
# print(l1==l2)   # 비교연산자 ==는 값을 비교
# print(l1 is l2)   #is 연산자 : 같은 객체인지 비교

# ##튜플 복사 : 튜플 복사해도 객체가 생성되지 않는다 / 링크연결
# t1 = (1,2,3)
# t2 = tuple(t1)  # 또는 t1[:]
# print(t1)
# print(t2)
# print(t1==t2)
# print(t1 is t2)

# s = 'GCCoding 2022'
# print(s[0])
# print(s[-3])
# print(s[2:8])

# l = ['G', 'C', 'C', 'o', 'd', 'i', 'n', 'g', '2', '0', '2', '2']
# print(l[3])
# print(l[-3])
# l.remove('d')
# print(l)
# print(l[2:7])

# t = ('G', 'C', 'C', 'o', 'd', 'i', 'n', 'g', '2', '0', '2', '2')
# print(t[4])
# print(t[-3])
# print(t[-4:])

# ##딕셔너리 생성
# dic = {'name':'nahyun', 'age':20, 'school':'korea'}
# print(dic)
# dic['class'] = 'stat'
# dic['age'] = 21
# print(dic)
# del dic['class']
# print(dic)

# fruits = {'apple': 500, 'banana':2500, 'mango':2000}
# print(fruits)
# print('망고는 1개당 %d원 입니다' %fruits['mango'])
# print('망고는 1개당 {}원 입니다'.format(fruits['mango']))
# print(f"사과는 1개당 {fruits['apple']}원 입니다")
# fruits['apple'] = 700
# fruits['strawberry'] = 3000
# del fruits['banana']
# print(fruits)

# d.keys()  #key들을 묶어서 반환
# d.values()  #value들을 묶어서 반환
# d.items()  #key와 value가 쌍으로 묶여서 반환
# d.get('key')  #'key'에 해당하는 value값을 반환
# d1.update({key:value})  #'key'에 해당하는 value값을 반환
# d.clear  #딕셔너리 d의 모든 item을 삭제

# print(fruits.keys())
# print(fruits.values())
# print(fruits.items())
# #반환된 값들은 다른 형태로 저장이 가능함
# names = list(fruits.keys())
# prices = tuple(fruits.values())
# print(names)
# print(prices)
# fruits.update({'apple':700, 'orange':1200})
# print(fruits)
# fruits.clear()
# print(fruits)

# print('과천코딩 매점에 오신 것을 환영합니다')
# menu = [['구운감자','고래밥','초코송이'],['코코팜','초코우유','쿨피스']]
# print('과자 종류: {}'.format(menu[0]))
# print('음료 종류: {}'.format(menu[1]))
# snack = input('새로운 간식을 입력해주세요:')
# menu[0].append(snack)
# print(menu)
# menu[0].sort()
# menu[1].sort()
# print(menu)
# print(f'과자 종류: {menu[0]}')
# print(f'음료 종류: {menu[1]}')

# print('메뉴의 가격을 수정해 주세요')
# snack = [('구운감자',1000),('고래밥',2000),('초코송이',1500)]
# print(snack)
# new = input('새로운 과자를 입력해주세요:')
# price = int(input('가격을 입력해주세요:'))
# tuple = (new, price)
# snack.insert(1,tuple)
# print(snack)

# phoneList = [{'name': '은정', 'phone': '010-1234-5678'},{'name':'준우', 'phone': '010-0000-6789'}]
# print(phoneList)
# phoneList[1]['phone'] = '010-1004-1004'
# print(phoneList)

# name1 = input('새로운 이름을 입력하세요:')
# phone1 = input('새로운 번호를 입력하세요:')
# person3 = {name1, phone1}
# phoneList.append(person3)
# print(phoneList)

# num = int(input('enter a digit number:'))
# if num>5:
#     print('your numer is more than 5')
# elif num<5:
#     print('your number is less than 5')
# else:
#     print('your number is 5')

num1 = int(input('숫자를 입력하세요'))
if num1>=100:
    print('big')
else:
    print('small')
