# -*- coding: utf-8 -*-
"""
Chapter02-37
다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
[입력] madam
[출력]
madam
입력하신 단어는 회문(Palindrome)입니다.

[풀이]
T = input()
T_reverse = str()

i = -1
cnt = -len(T)

while True:
    T_reverse += T[i]
    i -= 1
    
    if i < cnt:
       break
   
if T == T_reverse:
    print("{0}".format(T))
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")



Chapter02-38
다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.
[입력] A better tomorrow
[출력] tomorrow better A

[풀이]
T = input()

T_word_list = T.split(sep=" ")

print(T_word_list)

T_word_reverse = str()
for i in range(-1, -(len(T_word_list) + 1), -1):
    if i == -len(T_word_list):
        T_word_reverse += T_word_list[i]
    else:
        T_word_reverse += T_word_list[i] + " "
    
print(T_word_reverse)



Chapter02-39
다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로
구분하는 프로그램을 작성하십시오.
[입력] http://www.example.com/test?p=1&q=2
[출력]
protocol: http
host: www.example.com
others: test?p=1&q=2

[풀이]
homepage_input = input()
protocol_endpoint = homepage_input.find("://")
host_startpoint = protocol_endpoint + 3
host_endpoint = homepage_input.find("/", host_startpoint)

print("protocol: {0}".format(homepage_input[:protocol_endpoint]))
print("host: {0}".format(homepage_input[host_startpoint:host_endpoint]))
print("others: {0}".format(homepage_input[host_endpoint+1:]))



Chapter02-40
다음의 결과와 같이 여러 문장을 입력받아 대문자로 변환해 출력하는 프로그램을 작성합니다.
아무 것도 입력하지 않고 엔터만 입력하면 입력이 종료됩니다.
[입력] 
Hello World
hello world
Python
[출력]
>> HELLO WORLD
>> HELLO WORLD
>> PYTHON

[풀이]
while True:
    data = input()
    if data is not None:
        break
    else:
        print(">> {0}".format(data.upper()))



Chapter02-41
사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고,
중복된 단어없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성하십시오.
[입력] 산 하늘 강 바다 하늘 강 들
[출력] 강,들,바다,산,하늘

[풀이]
input_data = set(map(str, input().split()))
input_data = sorted(list(input_data))
for i in range(len(input_data)):
    if i == len(input_data) - 1:
        print(input_data[i])
    else:
        print(input_data[i] + ",", end="")



Chapter02-42
다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.
[입력] H1e2l3l4o5w6o7r8l9d
[출력] Helloworld

[풀이]
input_str = input()
result = str()

for i in range(len(input_str)):
    if i % 2 == 0:
        result += input_str[i]
    else:
        continue

print(result)
"""

data = input()
while data is not None:
    print(">> {0}".format(data.upper()))
    data = input()
        










