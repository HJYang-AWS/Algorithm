# -*- coding: utf-8 -*-
"""
[시퀀스형] -> 리스트, 튜플


1. 리스트의 생성 및 조작방법
[리스트]
대괄호[] 안에 서로 다른 자료형의 값을 콤마(,)로 구분해
하나 이상 저장할 수 있는 컬렉션 자료형
ex) data_list = [10, 21.5, "파이썬", True]

1-1) 리스트 항목 접근
인덱스를 이용해 접근
항목의 갯수 N, 0 ~ N-1까지의 인덱스 or -N ~ -1까지의 역순의 인덱스
범위를 벗어날 경우 IndexError가 발생함
콜론(:)을 이용한 범위 지정이 가능 list[start:end] -> start부터 end - 1까지

1-2) 리스트 기본 연산
data_list1, data_list2 = [1, 2, 3], [4, 5]

print("data_list1: {0} {1}".format(hex(id(data_list1)), data_list1))
print("{0} + {1} = {2}".format(data_list1, data_list2, data_list1 + data_list2))
print("{0} x 3 = {1}".format(data_list1, data_list1 * 3))

1-3) 리스트 항목 추가
list.append(항목): 항목 추가
list.insert(위치, 항목): list의 위치에 항목 추가
list.extend(list2): list2의 원소만 추가
list.append(list2): list2 통째로 list에 추가

1-4) 리스트 항목 변경
data_list = [1, 2, 3, 4]
data[2] = 5
print("data_list: {0}".format(data_list)) # [1, 2, 5, 4]

data_list[1:3] = [12, 15]
print("data_list: {0}".format(data_list)) # [1, 12, 15, 4]

data_list[2:3] = [31, 25]
print("data_list: {0}".format(data_list))
# [1, 12, 31, 25, 4] -> 리스트의 길이 변경

1-5) 리스트 항목 제거
data_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

del data_list[2]
print("data_list: {0}".format(data_list))
# [10, 20, 40, 50, 60, 70, 80, 90, 100]

del data_list[3:5]
print("data_list: {0}".format(data_list))
# [10, 20, 40, 70, 80, 90, 100]

data_list.pop(5)
print("data_list: {0}".format(data_list))
# [10, 20, 40, 70, 80, 100]

data_list.remove(100)
print("data_list: {0}".format(data_list))
# [10, 20, 40, 70, 80]

data_list.clear()
print("data_list: {0}".format(data_list))
# []

1-6) 리스트 항목 확인
data_list = [10, 20, 30, 40, 50, 60, 70, 80]

print("50 in data_list => {0}".format(50 in data_list))
print("50 in data_list => {0}".format(50 not in data_list))
print("data_list.count(50) => {0}".format(data_list.count(50)))
print("data_list.count(55) => {0}".format(data_list.count(55)))

1-7) 리스트와 for 문 (개별 항목 접근법)
data_list = list(range(0, 10 + 1, 2))

for item in data_list:
    print("{0}".format(item), end=" ")
print()
for idx, item in enumerate(data_list):
    print("data_list[{0}] => {1}".format(idx, item))
    
    

2. 리스트 내포의 특징
data_list1 = [1, 2, 3, 4, 5]

print("data_list1: {0} {1}".format(type(data_list1), data_list1))

data_list2 = []
for item in data_list1:
    data_list2.append(item)
print("data_list2: {0} {1}".format(type(data_list2), data_list2))

data_list3 = [item for item in data_list1]
print("data_list3: {0} {1}".format(type(data_list3), data_list3))

data_list4 = []
for item in data_list1:
    if item % 2 == 1:
        data_list4.append(item)
print("data_list4: {0} {1}".format(type(data_list4), data_list4))

data_list5 = [item for item in data_list1 if item % 2 == 1]
print("data_list5: {0} {1}".format(type(data_list5), data_list5))

data_list6 = [item for item in data_list1 if item % 2 == 0]
print("data_list6: {0} {1}".format(type(data_list6), data_list6))

data_list7 = []
for x in data_list1:
    if x % 2 == 1:
        for y in data_list1:
            if y % 2 == 0:
                data_list7.append(x * y)
print("data_list7: {0} {1}".format(type(data_list7), data_list7))

data_list8 = [x * y for x in data_list1 if x % 2 == 1
                   for y in data_list2 if y % 2 == 0]
print("data_list8: {0} {1}".format(type(data_list8), data_list8))

data_str = "Hello, Python!"
data_list9 = [item.lower() for item in data_str]
print("data_list9: {0} {1}".format(type(data_list9), data_list9))



3. [튜플]
중괄호() 안에 서로 다른 자료형의 값을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형
개별 항목은 0부터 시작하는 인덱스를 이용해 접근
저장된 항목은 변경 불가

3-1). 튜플 항목 접근
data_tuple = (10, 20, 30, 40, 50)

print("datatupe[0] => {0}".format(data_tuple[0]))
print("datatupe[-5] => {0}".format(data_tuple[-5]))

3-2). 튜플 기본 연산
data_tuple1, data_tuple2 = (10, 20, 30), (40, 50)

print("data_tuple1: {0} + data_tuple2: {1} => {2}".format(data_tuple1, data_tuple2, data_tuple1 + data_tuple2))
print("data_tuple2: {0} * 3 => {1}".format(data_tuple2, data_tuple2 * 3))

3-3). 튜플 항목 확인
ex) in, not in
list와 동일...

3-4) 튜플과 for 문
data_tuple = tuple(range(0, 11, 2))
for item in data_tuple:
    print("{0}".format(item), end=" ")

print()

for idx, item in enumerate(data_tuple):
    print("data_tuple[{0}] => {1}".format(idx, item))


  
4. 튜플 내포의 특징
data_tuple1 = (1, 2, 3, 4, 5)
data_tuple5 = tuple(x *y for x in data_tuple1 if x % 2 == 1
                         for y in data_tuple1 if y % 2 == 0)
print("data_tuple5: {0} {1}".format(type(data_tuple5), data_tuple5))



"""




# scores = []
#
# count = int(input("총 학생 수를 입력하세요: "))
#
# for i in range(1, count + 1):
#     score = []
#     kor = int(input("학생{0}의 국어 점수를 입력하세요: ".format(i)))
#     score.append(kor)
#     mat = int(input("학생{0}의 수학 점수를 입력하세요: ".format(i)))
#     score.append(mat)
#     eng = int(input("학생{0}의 영어 점수를 입력하세요: ".format(i)))
#     score.append(eng)
#     scores.append(score)
#
# for i, score in enumerate(scores):
#     total = 0
#     for s in score:
#         total += s
#     print("학생{0} 총점: {1}, 평균: {2:0.2f}".format(i + 1, total, total / len(score)))


data_list1 = [1, 2, 3, 4, 5]

data_list2 = []
for item in data_list1:
    data_list2.append(item)


data_list3 = [item for item in data_list1]
print("data_list3: {0} {1}".format(type(data_list3), data_list3))




































