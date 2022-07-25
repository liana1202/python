# print('10**2')
# fruit1 = '복숭아'
# fruit2 = '딸기'
# print(fruit1)
# print(fruit2)
# print(fruit1 + fruit2)  # 문자열도 덧셈이 가능하다.
# # print(fruit1 * fruit2)
# # print(fruit1 / fruit2)
# # print(fruit1 + fruit2)
# print(fruit*3)  # 문자열도 곱셈이 가능하다

# hi = 'Hello, World!'
# print(hi[0])
# print(hi[-1])

# s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# s2 = 'abcdefghijklmnopqrstuvwxyz'

# print(s1[11]+s2[8]+s2[0]+s2[13]+s2[0])
# print(s1[10]+s2[8]+s2[12])

# Name = 'Liana'
# print(Name[0:2])
# print(Name[2:5])
# print(Name[:4])
# print(Name[:])
# print(Name[1:-1])
# print(Name[2:])

# lipsum = "\'There is no one \nwho loves pain itself,\nwho seeks after it \nand wants to have it, \nsimply because it is pain...\'"
# print(lipsum)
# # \n 문자열 안에서 줄바꿈
# # \t 문자열 사이에 탭 간격
# # \' 문자를 그대로 표현
# # \\ 뮨저 \를 그대로 표현

# .count('') 특정 문자의 갯수 반환
# .upper() 문자열을 대문자로 변환
# .lower() 문자열을 소문자로 변환
# .replace('')
# .isalpha()  문자로만 구성되었는지 확인
# .isdigit()  숫자로만 구성되었는지 확인
# .split('') 해당 문자에서 문장 분리
# len()  문장의 길이 반환 

# lipsum = "\'There is no one \nwho loves pain itself,\nwho seeks after it \nand wants to have it, \nsimply because it is pain...\'"
# print(lipsum.count('a'))
# print(lipsum.upper())
# print(lipsum.lower())
# print(lipsum.replace('who','that'))
# print(lipsum.isalpha())
# print(lipsum.isdigit())
# print(lipsum.split(','))
# lipsum_list = lipsum.split(',')
# print(lipsum_list)
# print(lipsum_list[0])
# print(lipsum_list[2])
# phone = '010-4608-6666'
# phone_list = phone.split('-')
# print(phone_list)
# print(len(lipsum))

# ##김밥 만들기
# item0 = '김'
# item1 = '밥'
# item2 = '햄'
# item3 = '우엉'
# item4 = '계란'
# print(item0,item1, item2, item3, item4)

# items = ['김','밥','우엉','햄','계란']
# print(items)

# students = ['지수', '경연', '은서', '예빈']
# print(students)
# print(type(students))

# print(items[0])
# print(items[-1])
# print(items[1:3])

score = [80, 90, 88, 95]
# print(score)
# print(type(score))
# print(score[2])
# print(score[:2])

# print(students * 2)

# # max()  최댓값 반환
# # min()  최솟값 반환
# # len()  길이
# # list()  list로 변환
# print(max(score))
# print(min(score))
# print(len(score))

# age = 21
# print(age, type(age))

# text = 'hello'
# print(text, type(text))
# text = list(text)
# print(text, type(list))

# # list.append(x)  리스트 마지막에 x값 추가
# # list.insert(n,x)  리스트의 n번째 위치에 x값 추가
# # list.pop()  리스트의 마지막 값 삭제
# # list.remove(x)  리슨트의 x값 삭제
# # list.extend(list2)  리스트에 다른 리스트 병합


# score.append(99)
# print(score)
# score.insert(2,97)
# print(score)

# # list.index(x)  리스트에서 해당 값의 인데스 반환
# # list.count(x)  리스트에서 해당 값의 개수 반환

# print(score.index(90))
# print(score.count(90))

# # list.reverse()  역순 정렬
# # list.sort()   오름차순 정렬
# # list.sort(reverse=True)  내림차순으로 정렬

# score.reverse()
# print(score)
# score.sort()
# print(score)
# score.sort(reverse=True)
# print(score)

student = [['nahyun', 'woman', 20, 'stat', '01046086666'],['jisu', 'woman', '20', 'stat', '01044443333']]
print(student)
print(student[0][0], student[1][0])
print(student[0])