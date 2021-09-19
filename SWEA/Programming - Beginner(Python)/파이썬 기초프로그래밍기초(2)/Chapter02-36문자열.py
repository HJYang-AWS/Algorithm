# -*- coding: utf-8 -*-
"""
웹에서 수집한 카탈로그 -> 수 많은 html 태그가 존재
해당 태그에서 문자열을 추출

전처리 과정: 불필요한 데이터 삭제 및 추출
-> 문자열 찾기, 조작, 치환



1. 문자열 연산
1-1) 문자열의 연결
message = "안녕하세요"
guest = "홍길동"

greeting = guest + "님 " + message
# greeting = "{0}님, {1}".format(guest, message)
# -> str.format() 함수를 이용해 위치 지시자 {0}, {1}을 guest와 message에 저장된 값으로 변경
print(greeting)


1-2) 문자열의 반복
print("=" * 40)
print("-" * 13, end="")
print(" 문자열의 반복 ", end="")
print("-" * 13)
print("=" * 40)


1-3) 문자의 선택
data_str = "안녕하세요, 파이썬입니다"

idx = 0
cnt = len(data_str)
while True:
    print("data_str[{0}] : {1}".format(idx, data_str[idx]))
    if idx == cnt - 1:
        break
    idx += 1
print("-" * 40)

# 역순 출력
data_str = "안녕하세요, 파이썬입니다"

idx = -1
cnt = len(data_str)
while True:
    print("data_str[{0}] : {1}".format(idx, data_str[idx]))
    if idx == -cnt:
        break
    idx -= 1
print("-" * 40)


1-4) 문자열의 범위 선택
data_str = "와우! 안녕하세요, 파이썬입니다."

start = input("시작 인덱스를 입력하세요: ")
end = input("종료 인덱스를 입력하세요: ")

try:
    start = int(start)
except ValueError:
    start = None
try:
    end = int(end)
except ValueError:
    end = None
    
print("'{0}'".format(data_str[start: end]))



2. 문자열 함수
2-1) 문자열 출현 횟수 확인: str.count(문자열)
data_str = "Have a nice day!"

print("'{0}'".format(data_str))
input_str = input("위에서 찾고자하는 문자열을 입력하세요: ")

print("'{0}'에서 '{1}'은(는) {2} 번 나타납니다."
      .format(data_str, input_str, data_str.count(input_str)))

    
2-2) 문자열의 길이: len(문자열)
data_str = "Have a nice day!"
print("len()을 이용한 '{0}' 문자열의 길이 검사: {1}".format(data_str, len(data_str)))
    
    
2-3) 문자열 찾기
: str.find(문자열) 앞에서 찾기 시작, 찾으면 index위치, 못찾으면 -1 반환
: str.rfind(문자열) 뒤에서 찾기 시작, 찾으면 index위치, 못찾으면 ValueError 반환
data_str = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."

print("'{0}'".format(data_str))
input_str = input("위에서 찾고자하는 문자열을 입력하세요: ")

print("str.find() ...")
idx = data_str.find(input_str)

if idx != -1:
    print("\t'{0}' : [{1}] <= 문자열을 가장 먼저 찾은 위치".format(input_str, idx))
else:
    print("\t'{0}'를 찾을 수 없습니다.".format(input_str))
    
    
2-4) 문자열의 삽입: str.join(문자열), str을 문자열 사이에 끼워넣음
data_str = "가나다라마바사아자차카타파하"

comma_space = ", "

output = comma_space.join(data_str)
print("{0}: {1}".format(type(output), output))


2-5) 대소문자 바꾸기
: str.capitalize(), 첫 문자만 대문자로 변환한 문자열 반환
: str.lower(), 모든 문자를 소문자로 한 새로운 문자열 반환
: str.upper(), 모든 문자를 대문자로 한 새로운 문자열 반환
data_str = "better Tomorrow"
data_str = data_str.capitalize()
print("'{0}'".format(data_str))

data_str = data_str.lower()
print("'{0}'".format(data_str))

data_str = data_str.upper()
print("'{0}'".format(data_str))


2-6) 공백 제거
:str.lstrip(문자열), 인자로 전달된 문자열을 왼쪽에서 제거
:str.rstrip(문자열), 인자로 전달된 문자열을 오른쪽에서 제거
:str.strip(문자열), 인자로 전달된 문자열을 양쪽에서 제거
data_str = "   홍  길동   "
print("'{0}': ({1})".format(data_str, len(data_str)))
data_str = data_str.lstrip(" ")
print("'{0}': ({1})".format(data_str, len(data_str)))

data_str = "___홍  길동______  "
data_str = data_str.rstrip("_ ")
print("'{0}' : ({1})".format(data_str, len(data_str)))

data_str = " 0?홍  길동 _#      "
data_str = data_str.strip(" 0?_#")
print("'{0}' : ({1})".format(data_str, len(data_str)))


2-7) 문자열 교체
:str.replace(문자열1, 문자열2), 문자열1을 전달받고, 문자열2로 바꿈
data_str = "10....20....30....40....50"
data_str = data_str.replace("." * 4, '\t')
print(data_str)


2-8) 문자열 자르기
:str.split(문자열), 전달된 인자로 문자열을 잘라 이를 항목으로 갖는 리스트를 생성
data_str = "10, 20, 30, 40, 50"

data_str = data_str.replace(" ", "") # 공백제거
print(data_str)

data_list = data_str.split(",")
for val in data_list:
    print(val)
    

2-9) 문자열 구성 확인
isdigit(): 숫자문자열인 경우 true 반환
data_str = "10, 20, 3o, 40, 50"

data_str = data_str.replace(" ", "")
print(data_str)

data_list = data_str.split(",")
for val in data_list:
    print(val, end=" ")
    if not val.isdigit():
        print("<= ", end=" ")
    print()
    


[문자열을 마스크 문자열로 치환하기]
[결과]
'파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다.'
마스킹할 문자열을 입력하세요: $$$$$$
찾을 문자열을 입력하세요: 객체
[14] ~ [15]
파이썬은 클래스를 이용해 $$$$$$를 생성하는 객체지향 프로그래밍 언어입니다.
[23] ~ [24]
파이썬은 크래스를 이용해 $$$$$$를 생성하는 $$$$$$지향 프로그래밍 언어입니다.
조건
* 문자열을 찾을 경우 해당 문자열의 인덱스를 출력하고 마스킹된 결과 출력
* find, replace 함수 활용

"""

data_str = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."
print("'{0}'".format(data_str))

mask_str = input("마스킹할 문자열을 입력하세요: ")

find_str = input("찾을 문자열을 입력하세요: ")
idx = -1
count = 1
while True:
    idx = data_str.find(find_str, idx + 1)
    if idx != -1:
        print("[{0}] ~ [{1}]".format(idx, idx + len(find_str) - 1))
        new_str = data_str.replace(find_str, "****", count)
        print(new_str)
        count += 1
    else:
         break   

print(idx)


























