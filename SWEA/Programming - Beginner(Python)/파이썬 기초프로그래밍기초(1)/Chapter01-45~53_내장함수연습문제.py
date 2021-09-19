# -*- coding: utf-8 -*-
"""
Chapter01-45
다음의 결과와 같이 이름과 나이를 입력 받아
올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.
[입력] 홍길동 \n 20
[출력] 홍길동(은)는 2099년에 100세가 될 것입니다.

[풀이]
name = str(input())
age = int(input())

def print_100age(name, age):
    print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(name, 2021 + (100 - age)))
    
print_100age(name, age)


Chapter01-46
"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때
문자열에 사용된 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.
[입력] 입력 없음
[출력] 184

[풀이]
def string_to_score(string: str):
    str_list = list(string)
    result = 0
    
    for word in str_list:
        if word == "A": result += 4
        if word == "B": result += 3
        if word == "C": result += 2
        if word == "D": result += 1
    
    return result

string_list = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
sumation = list(map(lambda x: string_to_score(x), string_list))
print(sum(sumation))


Chapter01-47
가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,
단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력] 에러발생

[풀이]
def multiple_index(int_list: list):
    try:
        result = 1
        for element in int_list:
            result *= int(element)
    except:
        return print("에러발생")
    
    return print(result)
        
    
int_list = list(input().split(sep=", "))
multiple_index(int_list)


Chapter01-48
ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오
[입력] 65
[출력] ASCII 65 => A

[풀이]
T = int(input())
print("ASCII {0} => {1}".format(T, chr(T)))


Chapter01-49
1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력] [2, 4, 6, 8, 10]

[풀이]
T = [ i for i in range(1, 10 + 1)]

T_even_list = list(filter(lambda x: x % 2 == 0, T))
print(T_even_list)


Chapter01-50
1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해
항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력] [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[풀이]
T = [i for i in range(1, 10 + 1)]

result = list(map(lambda x: x ** 2, T))
print(result)


Chapter01-51
1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와
람다식을 이용해 짝수만을 선택한 후, map 함수와 람다식을 이용해
항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력] [4, 16, 36, 64, 100]

[풀이]
T = [i for i in range(1, 10 + 1)]
T_even_list = list(filter(lambda x: x % 2 == 0, T))
T_even_square_list = list(map(lambda x: x**2, T_even_list))
print(T_even_square_list)


Chapter01-52
가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고,
다음과 같은 결과를 출력하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력] max(3, 5, 4, 1, 8, 10, 2) => 10

[풀이]
def print_max_element(int_list: list):
    print("max(", end="")
    print(*T, sep=", ", end="")
    print(") => {0}".format(max(int_list)))


T = [3, 5, 4, 1, 8, 10, 2]

print_max_element(T)


Chapter01-53
다음의 결과와 같이 'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를
값으로 하는 딕셔너리 객체를 생성하고, 이 딕셔너리 객체의 키와 값 정보를 출력하는
프로그램을 작성하십시오.
[입력] 입력없음
[출력] 
a: 0
b: 1
c: 2
d: 3
e: 4
f: 5

[풀이]
T = 'abcdef'
T_dict = dict(enumerate(T))

for i in range(len(T)):
    print("{0}: {1}".format(T_dict[i], i))
"""














