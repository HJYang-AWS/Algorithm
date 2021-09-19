# -*- coding: utf-8 -*-
"""
Chapter02-27
다음과 같이 등록된 학생의 이름을 출력하고, 이름을 입력하면 전화번호를 출력해주는
딕셔너리 객체를 이용한 전화번호부 프로그램을 작성하십시오.
[등록된 학생]
홍길동: 010-1111-1111
이순신: 010-1111-2222
강감찬: 010-1111-3333
[프로그램]
아래 학생들의 전화번호를 조회할 수 있습니다.
홍길동
이순신
강감찬
전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.

[입력] 이순신
[출력]
아래 학생들의 전화번호를 조회할 수 있습니다.
홍길동
이순신
강감찬
전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.
이순신의 전화번호는 010-1111-2222입니다.

[풀이]
phone_book = {
    '홍길동': '010-1111-1111',
    '이순신': '010-1111-2222',
    '강감찬': '010-1111-3333'
}

print("아래 학생들의 전화번호를 조회할 수 있습니다.")
for name in phone_book.keys():
    print(name)
print("전화번호를 저회하고자 하는 학생의 이름을 입력하십시오.")

search_name = input()

print("{0}의 전화번호는 {1}입니다.".format(search_name, phone_book[search_name]))



Chapter02-28
아래의 상품 딕셔너리 데이터를 가격에 따라 내림차순으로 정렬하는 프로그램을 작성하십시오.
"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000,

[입력] 입력없음
[출력] 
TV: 2000000
냉장고: 1500000
노트북: 1200000
세탁기: 1000000
책상: 350000
가스레인지: 200000

[풀이]
home_appliance = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000
}

# key=lambda x : x[0] -> key 값으로 정렬
sort_home_appliance = dict(sorted(home_appliance.items(), key=lambda x : x[1], reverse=True))
for key, value in sort_home_appliance.items():
    print("{0}: {1}".format(key, value))



Chapter02-29
다음 두 딕셔너리 객체를 합쳐 중복된 메뉴가 없는 딕셔너리를 만들고
가격이 3000원 이상인 메뉴를 아래와 같이 출력하는 프로그렘을 작성하십시오.
중복된 메뉴의 가격이 다를 경우 딕셔너리 a의 가격을 사용하세요.
a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

[입력] 입력없음
[출력] {('카페모카', 3300), ('밀크커피', 3300), ('샷크린티라떼', 3300)}

[풀이]
a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

a.update(b)
print_list = dict()
for key, value in a.items():
    if value >= 3000:
        print_list.update({key: value})

print("{", end="")
for idx, key in enumerate(print_list.keys()):
    if idx == len(print_list) - 1:
        print("('{0}', {1})".format(key, value), end="")
    else:
        print("('{0}', {1})".format(key, value), end=", ")
print("}")



Chapter02-30
리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해봅시다.
이 때 딕셔너리 내포 기능을 사용하며, 원소의 공백은 제거합니다.
리스트 fruit는 다음과 같습니다. fruit = ['   apple    ','banana','  melon']

[입력] 입력없음
[출력] {'apple': 5, 'banana': 6, 'melon': 5}

[풀이]
fruit = ['    apple    ','banana','  melon']
fruit_dict = dict()

for idx, fru in enumerate(fruit):
    spelling = str()
    for alphabet in fru:
        if alphabet != ' ':
            spelling += alphabet
    fruit_dict.update({spelling: len(spelling)})

print(fruit_dict)



Chapter02-31
다음과 같이 정수 N을 입력받아서 1부터 N까지의 정수를 키로 하고, 
그 정수의 제곱을 값으로 하는 딕셔너리 객체를 만드는 코드를 작성하십시오.
[입력] 5
[출력] {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

[풀이]
num = int(input())
num_dict = {}

for i in range(1, num + 1):
    num_dict.update({i: i ** 2})

print(num_dict)



Chapter02-32
다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.
[입력] hello world! 123
[출력] 
LETTERS 10
DIGITS 3

[풀이]
info_dict = {
    'LETTERS': 0,
    'DIGITS': 0
}


T = input()

for element in T:
    if ord('a') <= ord(element) <= ord('z'):
        info_dict['LETTERS'] += 1
    if ord('A') <= ord(element) <= ord('Z'):
        info_dict['LETTERS'] += 1
    if '0' <= element <= '9':
        info_dict['DIGITS'] += 1
        
for key, value in info_dict.items():
    print("{0} {1}".format(key, value))



Chapter02-33
다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.
[입력] Hello World! 123
[출력] 
UPPER CASE 2
LOWER CASE 8

[풀이]
info_dict = {
    'UPPER CASE': 0,
    'LOWER CASE': 0
}


T = input()


for element in T:
    if ord('a') <= ord(element) <= ord('z'):
        info_dict['LOWER CASE'] += 1
    if ord('A') <= ord(element) <= ord('Z'):
        info_dict['UPPER CASE'] += 1
        
for key, value in info_dict.items():
    print("{0} {1}".format(key, value))



Chapter02-34
다음과 같은 기존의 맥주 가격을 5% 인상하려고 할 경우
딕셔너리 내포 기능을 이용한 코드를 작성하십시오.
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}

[입력] 입력없음
[출력] 
{'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}            # 인상 전
{'하이트': 2100.0, '카스': 2205.0, '칭따오': 2625.0, '하이네켄': 4200.0, '버드와이저': 525.0}  # 인상 후

[풀이]
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}

print(beer)
for key, value in beer.items():
    beer.update({key: float(value) * 1.05})
print(beer)



Chapter02-35
다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.
[입력] abcdefgabc
[출력] 
a,2
b,2
c,2
d,1
e,1
f,1
g,1

[풀이]
T = input()
T_dict = {}

for alphabet in T:
    if alphabet not in T_dict.keys():
        T_dict.update({alphabet: 1})
    else:
        T_dict[alphabet] += 1

for key, value in T_dict.items():
    print("{0}, {1}".format(key, value))
"""


















