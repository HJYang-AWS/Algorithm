# -*- coding: utf-8 -*-
"""
다양한 데이터의 중복이 필요하지 않는 경우가 생김
ex) 학번 -> 다른 학생들과 구별할 수 있는 중요한 식별자
이러한 식별자를 Key Data(중복허용불가)라고 한다
중복허용되지 않는 자료구조는 셋(Set)이 있다.

키 데이터와 관련된 데이터를 연결한 자료구조를 딕셔너리(Dictionary)라고 한다.

셋과 딕셔너리는 데이터의 중복을 허용하지 않는 반복형 자료구조



1. 셋 생성 및 조작법
[셋]
중괄호 {} 안에 서로 다른 자료형의 유일한 값을 콤마(,)로 구분해
하나 이상 저장할 수 있는 컬렉션 자료형 중의 하나
* 인덱스를 제공하지 않음
* 순서의 개념이 없음
* 중복을 허용하지 않음
ex)
data_set = {10, 20, "파이썬", "파이썬"}
print("{0} {1}".format(type(data_set), data_set))

data_set = set(range(10, 21, 2))
print("{0} {1}".format(type(data_set), data_set))

data_str = "Better Tomorrow"
data_set = set(data_str)
print("{0} {1}".format(type(data_set), data_set))


1) 셋 조작법
교집합(&: intersection()), 합집합(|: union()), 차집합(-: difference())

1-1) 셋 기본 연산
data_set1 = {1, 2, 3, 4, 5, 6, 7, 7, 11}
data_set2 = {2, 3, 5, 9, 11, 12, 15}

print("{0} & {1} = {2}".format(data_set1, data_set2, data_set1 & data_set2))
print("{0} | {1} = {2}".format(data_set1, data_set2, data_set1 | data_set2))
print("{0} - {1} = {2}".format(data_set1, data_set2, data_set1 - data_set2))

print("{0}.intersection({1}) = {2}".format(data_set1, data_set2, data_set1.intersection(data_set2)))
print("{0}.union({1}) = {2}".format(data_set1, data_set2, data_set1.union(data_set2)))
print("{0}.difference({1}) = {2}".format(data_set1, data_set2, data_set1.difference(data_set2)))

1-2) 셋 항목 추가
data_set = {1, 2, 3}

print("data_set: {0}".format(data_set))

# 중복 항목은 포함이 안됨
data_set.add(3)

data_set.add(4)
print("data_set: {0}".format(data_set))

# update 함수로 4, 5, 6을 항목으로 추가
data_set.update({4, 5, 6})
print("data_set: {0}".format(data_set))

1-3) 셋 항목 제거
data_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("data_set: {0}".format(data_set))

data_set.remove(9)
data_set.remove(2)
print("data_set: {0}".format(data_set))

# pop함수를 첫번째 항목 제거
data_set.pop()
print("data_set: {0}".format(data_set))

# data_set.clear() 함수로 모든 객체 제거
data_set.clear()
# {}는 딕셔너리의 리터럴이기 때문에, 비어있는 셋은 set()으로 표시함
print("data_set: {0}".format(data_set))

1-4) 셋 항목 확인
data_set1 = {1, 2, 3, 4, 5}
data_set2 = {2, 3}

# 셋 객체에 해당하는 항목이 있는지 검사
print("3 in data_set1 => {0}".format(3 in data_set1))
# 셋 객체에 해당 항목이 없는지 검사
print("6 not in data_set1 => {0}".format(6 not in data_set1))
# data_set1이 data_set2를 포함하는지 True/False 반환
print("{0}.issuperset({1}) => {2}".format(data_set1, data_set2, data_set1.issuperset(data_set2)))
# data_set2가 data_set!에 포함되는지 True/False 반환
print("{0}.issubset({1}) => {2}".format(data_set2, data_set1, data_set1.issubset(data_set1)))

1-5) for 문을 이용한 셋 항목 접근
data_set = set(range(0, 10 + 1, 2))

for item in data_set:
    print("{0}".format(item), end=" ")

print()

for idx, item in enumerate(data_set):
    print("[{0}] => {1}".format(idx, item))



2. 셋 내포의 특징
data_set1 = {1, 2, 3, 4, 5}
print("data_set1: {0} {1}".format(type(data_set1), data_set1))

data_set2 = {item for item in data_set1}
print("data_set2: {0} {1}".format(type(data_set2), data_set2))

data_set3 = {item for item in data_set1 if item % 2 == 1}
print("data_set3: {0} {1}".format(type(data_set3), data_set3))

data_set4 = {item for item in data_set1 if item % 2 == 0}
print("data_set4: {0} {1}".format(type(data_set4), data_set4))

data_set5 = {x * y for x in data_set1 if x % 2 == 1
                   for y in data_set1 if y % 2 == 0}
print("data_set5: {0} {1}".format(type(data_set5), data_set5))


data_str = "Hello"

data_list = list(data_str)
print("{0} => {1}: {2}".format(type(data_str), type(data_list), data_list))

data_tuple = tuple(data_list)
print("{0} => {1}: {2}".format(type(data_list), type(data_tuple), data_tuple))

data_set = set(data_tuple)
print("{0} => {1}: {2}".format(type(data_tuple), type(data_set), data_set))
      
data_list = list(data_set)
print("{0} => {1}: {2}".format(type(data_set), type(data_list), data_list))



3. 딕셔너리 생성 및 조작법
[딕셔너리]
중괄호{} 안에 키: 값의 형식을 가진 유일한 데이터를 콤마(,)로 구분해
하나 이상 저장할 수 있는 컬렉션 자료형 중의 하나
* 인덱스를 제공하지 않음
* 순서의 개념이 없음
* 중복을 허용하지 않음

3-1) 딕셔너리의 생성
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35
    }

print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

# '키=값' 형식의 매개변수 목록에서 키를 문자열로 작성하지 않도록 주의
data_dict2 = dict(홍길동=20, 이순신=45, 강감찬=35)
print("data_dict2: {0} {1}".format(type(data_dict2), data_dict2))

# (키, 값)으로 구성된 튜플을 항목으로 하는 튜플 객체에서 딕셔너리 객체를 생성할 수 있음
data_tuple1 = (("홍길동", 20), ("이순신", 45), ("강감찬", 35))
data_dict3 = dict(data_tuple1)
print("data_dict3: {0} {1}".format(type(data_dict3), data_dict3))

# (키, 값)으로 구성된 튜플을 항목으로 하는 리스트 객체에서 딕셔너리 객체를 생성할 수 있음
data_list1 = [("홍길동", 20), ("이순신", 45), ("강감찬", 35)]
data_dict4 = dict(data_list1)
print("data_dict4: {0} {1}".format(type(data_dict4), data_dict4))

# (키, 값)으로 구성된 튜플을 항목으로 하는 셋 객체에서 딕셔너리 객체를 생성할 수 있음
data_set1 = {("홍길동", 20), ("이순신", 45), ("강감찬", 35)}
data_dict5 = dict(data_set1)
print("data_dict5: {0} {1}".format(type(data_dict5), data_dict5))

3-2) 딕셔너리 항목 접근
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35
    }

print("data_dict1['홍길동'] => {0}".format(data_dict1["홍길동"]))

# 존재하지 않는 키를 사용하면 KeyError 예외가 발생하고 프로그램 중지
# print("data_dict1['을지문덕'] => {0}".format(data_dict1["을지문덕"]))

3-3) 딕셔너리 조작법
* 딕셔너리 항목 추가
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35
    }
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

# 항목 추가
data_dict1["을지문덕"] = 40
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

# update() 함수를 통한 항목 추가
data_dict1.update({"신사임당": 50, "유관순": 16})
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

* 딕셔너리 항목 변경
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35
    }
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

# 항목 변경
data_dict1["강감찬"] = 38
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

# update() 함수를 통한 항목 변경
data_dict1.update({"홍길동": 25, "이순신": 48})
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

* 딕셔너리 항목 제거
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35,
    "을지문덕": 40
    }
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

# 항목 변경
del data_dict1["강감찬"]
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))
# del data_dict1["강감찬"] # KeyError 발생

# pop() 함수를 호출해 데이터 삭제
data_dict1.pop("이순신")
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

# clear() 함수를 모든 항목 삭제, {} 빈 딕셔너리 객체 리터럴 출력
data_dict1.pop("이순신")
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

* 딕셔너리 항목 확인
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35,
    }
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))


print("'홍길동' in data_dict1 => {0}".format("홍길동" in data_dict1))
print("'신사임당' not in data_dict1 => {0}".format("신사임당" not in data_dict1))

* for 문을 이용한 딕셔너리 항목 접근
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35,
    }
print("data_dict1: {0} / {1}".format(type(data_dict1), data_dict1))

# dict.items(): 튜플로 구성
print("{0} / {1}".format(type(data_dict1.items()), data_dict1.items()))
# dict.keys(): 문자열로 구성
print("{0} / {1}".format(type(data_dict1.keys()), data_dict1.keys()))
# dict.values(): 정수로 구성
print("{0} / {1}".format(type(data_dict1.values()), data_dict1.values()))

print()
for key in data_dict1:
    print("key, data_dict1[key] => '{0}', {1}".format(key, data_dict1[key]))

print()
for key in data_dict1.keys():
    print("key, data_dict1[key] => '{0}', {1}".format(key, data_dict1[key]))

print()
# item[0]: 키, item[1]: 값
for item in data_dict1.items():
    print("item[0], item[1] => '{0}', {1}".format(item[0], item[1]))

print()
for key, value in data_dict1.items():
    print("key, value => '{0}', {1}".format(key, value))

print()
for value in data_dict1.values():
    print("value => {0}".format(value))



4. 딕셔너리 내포의 특징
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35,
    }
print("data_dict1: {0} / {1}".format(type(data_dict1), data_dict1))

print()
# item이 {key: value}형태로 data_set1에 저장되어 dictionary 형태를 띄게 된다
data_set1 = {item for item in data_dict1.items()}
print("data_dict1: {0} / {1}".format(type(data_dict1), data_dict1))

print()
data_dict2 = {key: data_dict1[key] for key in data_dict1}
print("data_dict2: {0} / {1}".format(type(data_dict2), data_dict2))

print()
data_dict3 = {key: data_dict1[key] for key in data_dict1.keys()}
print("data_dict3: {0} / {1}".format(type(data_dict3), data_dict3))

print()
data_dict4 = {item[0]: item[1] for item in data_dict1.items()}
print("data_dict4: {0} / {1}".format(type(data_dict4), data_dict4))

print()
data_dict5 = {key: value for key, value in data_dict1.items()}
print("data_dict5: {0} / {1}".format(type(data_dict5), data_dict5))


"""

# 학생 및 점수 정보 저장

scores = []

count = int(input("총 학생의 수를 입력하세요: "))

for i in range(1, count + 1):
    score = {}
    score["name"] = input("학생의 이름을 입력하세요: ")
    score["kor"] = int(input("{0} 학생의 국어 점수를 입력하세요: ".format(score["name"])))
    score["mat"] = int(input("{0} 학생의 수학 점수를 입려갛세요: ".format(score["name"])))
    score["eng"] = int(input("{0} 학생의 영어 점수를 입려갛세요: ".format(score["name"])))
    scores.append(score)
    
for score in scores:
    total = 0
    for key in score:
        if key != "name":
            total += score[key]
    print("{0} -> 총점: {1}, 평균: {2}".format(score["name"], total, total / 3))

kor_total, mat_total, eng_total = 0, 0, 0
for score in scores:
    for key in score:
        if key == 'kor':
            kor_total += score[key]
        elif key == 'mat':
            mat_total += score[key]
        elif key == 'eng':
            eng_total += score[key]

print("국어 => 총점: {0}, 평균: {1}".format(kor_total, kor_total / len(scores)))
print("수학 => 총점: {0}, 평균: {1}".format(mat_total, mat_total / len(scores)))
print("영어 => 총점: {0}, 평균: {1}".format(eng_total, eng_total / len(scores)))


























