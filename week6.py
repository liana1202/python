# students = ['지수','은서','경민','예빈']

# # print(students[0])
# index = 0
# while index < 4:
#     print(students[index])
#     index += 1

# for i in students:
#     print(i)

# score = {'m':100, 'en':80, 'wb':80, 'cw':70, 'sc':90, 'ss':70}
# # for i in score:
# #     print(i)
# # for i in score:
# #     print(score[i])

# for i in score:
#     # if score[i] >= 80:
#     #     print(f'{i}:축하합니다')
#     # else :
#     #     print(f'{i}:80 못넘었습니다')
#     if score[i] <80:
#         continue
#     # else:
#         print(f'{i} : 축하합니다')

# range - stop: stop-1까지 출력, start : 시작값,  step : 간격
# range(start, stop, step)

# for i in range(10):
#     print(i, end=' ')
# print()
# for i in range(3,10):
#     print(i, end=' ')
# print()
# for i in range(3,10,3):
#     print(i, end=' ')

# for i in range(10, 1, -1):
#     print(i, end=' ')
# num = int(input('숫자입력:'))
# for i in range(1,num+1):
#     print(i, end=' ')
# num1= int(input('숫자입력:'))
# num2= int(input('숫자입력:'))
# for i in range(num1, num2+1):
#     print(i)

# cnt=0
# for i in range(3,101,3):
#     print(i, end=' ')
#     cnt += 1
#     if cnt%10 == 0:
#         print()

# num = input()
# print(num)
# num = num.split()
# print(num)
# num = [int(i) for i in num]
# print(num)

# num = input().split()
# num = [int(i) for i in num]
# print(num)

# num = input().split()
# num = [int(i) for i in num]
# print(sum(num))

# num = int(input('숫자입력:'))
# for i in range(1,num+1):
#     print('*'*i)

# num = int(input('숫자입력:'))
# for i in range(1, num+1):
#     print(' '*(5-i)+'*'*i)

# for i in range(1,5):
#     print('*'*i)
#     for i in range(1,3):
#         print('#'*i)

line = int(input('입력:'))
for i in range(1,line+1):
    for j in range(line,i,-1):
        print(' ', end='')
    print('*'*i)