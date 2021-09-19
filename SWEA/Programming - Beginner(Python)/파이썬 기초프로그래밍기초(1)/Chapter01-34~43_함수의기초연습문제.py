# -*- coding: utf-8 -*-
"""
Chapter01-34
다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
[입력] eye
[출력]
eye
입력하신 단어는 회문(Palindrome)입니다.

[풀이]
def make_reverse_words(words: str):
    return ''.join(reversed(words))

words = input("")

reverse_words = make_reverse_words(words)
    
if words == reverse_words:
    print(words)
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")



Chapter01-35
다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.
[입력] 
홍길동
이순신
가위
바위
[출력]
바위가 이겼습니다!

[풀이]
def rock_scissor_paper(rsp_list: list):
    if rsp_list[2] == '가위':
        if rsp_list[3] == '가위': return print("비겼습니다!")
        if rsp_list[3] == '바위': return print("바위가 이겼습니다!")
        if rsp_list[3] == '보': return print("가위가 이겼습니다!")
    if rsp_list[2] == '바위':
        if rsp_list[3] == '가위': return print("바위가 이겼습니다!")
        if rsp_list[3] == '바위': return print("비겼습니다!")
        if rsp_list[3] == '보': return print("보가 이겼습니다!")
    if rsp_list[2] == '보':
        if rsp_list[3] == '가위': return print("가위가 이겼습니다!")
        if rsp_list[3] == '바위': return print("보가 이겼습니다!")
        if rsp_list[3] == '보': return print("비겼습니다!")


rsp_list = [_ for _ in range(4)]

for index in range(4):
    rsp_list[index] =  input()
    
rock_scissor_paper(rsp_list)


Chapter01-36
소수를 검사하는 함수를 정의하고, 다음의 결과와 같이 사용자가 입력한 숫자가
소수인지를 판단하는 프로그램을 작성하십시오.
소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력
[입력] 13
[출력] 소수입니다.

[풀이]
def confirm_prime_number(num: int):
    if num == 1:
        return print("소수가 아닙니다.")
    
    count = 0
    for i in range(2, num + 1):
        if num % i == 0:
            count += 1
        if count == 2 and i != num:
            return print("소수가 아닙니다.")
    return print("소수입니다.")  

T = int(input())

confirm_prime_number(T)


Chapter01-37
다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
[입력] 10
[출력] [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

[풀이]
def make_fibonacci_list(num: int):
    fibonacci_list = [1, 1]
    
    if num == 1:
        return print("[1]")
    if num == 2:
        return print("[1, 1]")
    if num >= 3:
        i = 1
        while i < num - 1 :
            fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i - 1])
            i += 1
        return print(fibonacci_list)


T = int(input())

make_fibonacci_list(T)


Chapter01-38
리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고
이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.
[입력] 없음
[출력]
[1, 2, 3, 4, 3, 2, 1]
[1, 2, 3, 4]

[풀이]

def make_set_list(lst: list):
    set_list = set(lst)
    return print(list(set_list))

num_list = [1, 2, 3, 4, 3, 2, 1]
print(num_list)
make_set_list(num_list)


Chapter01-39
정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력]
[2, 4, 6, 8, 10]
5 => False
10 => True

[풀이]
def confirm_list_in_number(num_list, num):
    print("{0} => ".format(num), end="")
    if num in num_list:
        print("True")
    else:
        print("False")
        

num_list = [2, 4, 6, 8, 10]
print(num_list)
confirm_list_in_number(num_list, 5)
confirm_list_in_number(num_list, 10)   


Chapter01-40
다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
팩토리얼 값을 구하는 프로그램을 작성하십시오.
[입력] 5
[출력] 120


[풀이]



Chapter01-41
숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면
정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오
[입력] 2, 3
[출력]
square(2) => 4
square(3) => 9

[풀이]
def make_square(num_list: int):
    for i in num_list:
        print("square(%d) => %d" % (int(i), int(i) ** 2))


T = list(input().split(sep=", "))
make_square(T)


Chapter01-42
인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고
결과를 출력하는 프로그램을 작성하십시오.
[입력] one, three
[출력] three

[풀이]
def print_longest_string(string_list: list):
    index = 0
    string_len = 0
    
    for i in range(len(string_list)):
        if string_len < len(string_list[i]):
            string_len = len(string_list[i])
            index = i
    return string_list[index]

T = list(input().split(sep=", "))

print(print_longest_string(T))


Chapter01-43
인자로 전달된 숫자를 이용해 카운트다운하는 함수 countdown을 정의하고,
이 함수를 이용하여 countdown(0), countdown(10)을 순서대로 실행하십시오.
0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.
[입력] 입력없음
[출력]
카운트다운을 하려면 0보다 큰 입력이 필요합니다.
10
9
8
7
6
5
4
3
2
1

[풀이]
"""

# def countdown(num: int):
#     if num <= 0:
#         print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
#     else:
#         for i in range(num, 0, -1):
#             print(i)
#
# countdown(0)
# countdown(10)














