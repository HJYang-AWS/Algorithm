# -*- coding: utf-8 -*-
"""
인자는 매개변수를 통해서 함수로 들어와서 반환값으로 나간다.
순수 함수(pure function): 결과값 반환 외에 외부에 영향을 주지 않는 함수
함수형 프로그래밍 지원 언어에서는 순수 함수를 인자, 반환 값으로 사용


함수의 호술
함수는 표준명 뒤에 괄호()를 붙여서 출력
괄호 안에는 인자를 넣는다.
ex)
a, b = 2, 3
c = a + b

print("내장함수 str.format() 과 print()를 이용한 c의 결과 출력: {0}".format(c))


함수의 선언
def 함수명(매개변수):
    명령문1
    명령문...
    return값
ex)
a, b = 2, 3
c = calc_sum(a, b)
d = calc_sum(a, c)
print("사용자 정의 함수 calc_sum 호출을 이용한 c의 결과: {0}".format(c))
print("사용자 정의 함수 calc_sum 호출을 이용한 d의 결과: {0}".format(d))    


함수 선언의 위치 문제
인터프리터 언어의 경우 함수 선언의 위치가 중요
실행 공간의 함수가 먼저 선언 되어야 작동 가능


함수의 유형
매개변수, 반환값에 유무의 따라 유형이 나뉨
1) 매개변수와 반환 값이 있는 함수
2) 매개변수는 없고, 반환 값이 있는 함수 
3) 매개변수는 있고 반환 값은 없는 함수
4) 매개변수와 반환 값이 없는 함수

    
매개변수
함수 호출 시 입력 값을 전달 받기 위한 변수
전달받은 인자의 값에 의해 타입이 결정됨
선언된 매개변수의 개수만큼 인자 전달 가능


언팩 연산자(*)
매개변수의 개수를 가변적으로 사용할 수 있도록 언팩 연산자(*) 제공
매개변수에 적용 시 인자를 튜플 형식으로 처리함
가변형 매개변수를 하나만 지정할 수 있으며 가장 마지막에 지정해야 부작용 없이 사용할 수 있음
ex)
def calc_sum(*params):
    total = 0
    for val in params:
        total += val
    return total


명시적 매개변수와 가변 매개변수의 혼합 사용
ex)
def calc_sum(precision, *params):
    if precision == 0:
        total = 0
    elif 0 < precision < 1:
        total = 0.0
    
    for val in params:
        total += val
    return total


언팩 연산자를 사용하는 튜플 형식의 반환값
함수의 반환 값으로 하나 이상의 값을 처리할 수 있음
ex)
def calc_sum(precision1, precision2, *params):
    if precision1 == 0:
        total1 = 0
    elif 0 < precision1 < 1:
        total1 = 0.0
        
    if precision2 == 0:
        total2 = 0
    elif 0 < precision2 < 1:
        total2 = 0.0
        
    for val in params:
        total1 += val
        total2 += val
        
    # 튜플을 반환해서 하나 이상의 값을 반환할 수 있음  
    return total1, total2 
            
ret_val1 = calc_sum(0, 0.1, 1, 2)
ret_val2 = calc_sum(0.1, 0, 1, 2)
print("{0}, {1}".format(*ret_val1))
print("{0}, {1}".format(*ret_val2))


키워드 언팩 연산자(**)
매개변수의 개수를 가변적으로 사용할 수 있도록 함
키워드 인자들을 전달해 매개변수를 딕셔너리 형식으로 처리함
ex)
def use_keyword_arg_unpacking(**params):
    # 함수 호출 시, 키=값 형식의 인자들이
    # params 매개변수에 딕셔너리 형식으로 전달
    for k in params.keys():
        # key는 매개변수 이름, 값은 전달된 인자 값
        print("{0}: {1}".format(k, params[k]))
        
        
기본 값을 갖는 매개변수
매개변수에 전달할 인자 값이 생략되었다면? -> 사용할 기본 값 지정
기본 값을 가지는 매개변수는 일반 매개변수 앞에 위치할 수 없다.
ex)
def calc(x, y, operator="+"): # "+"를 기본값으로 지정
    if operator == "+":
        return x + y
    else:
        return x - y
    
    
scope
변수의 유호범위
전역 스코프: 어디서나 접근 가능한 전역 변수
함수 스코프: 함수 내에서만 접근 가능한 지역 변수
지역 변수와 전역변수 이름이 같을 경우! 전역변수가 가려져 접근 못할 수도 있음
-> 접근하고자 하는 전역변수 앞에 global을 기술함
ex)
def test_scope(a): # 매개변수 a: 함수 스코프를 가지는 지역 변수
    result = a + 1
    print("\n\ttest_scope() 안에서의 a의 값: {0}".format(a))
    print("\ttest_scope() 안에서의 result 값: {0}\n".format(result))
    return result

x = 5
print("test_scope() 호출 전 x의 값: {0}".format(x))
ret_val = test_scope(x)
print("test_scope() 함수가 반환한 값: {0}".format(ret_val))
print("test_scope() 호출 후 x의 값: {0}".format(x))


고급 함수 - 중첩 함수
함수 내에 중첩함수를 선언해 사용 가능
1) 중첩함수를 포함하는 함수 내에서만 호출이 가능
2) 중첩함수를 포함하는 함수의 스코프에도 접근이 가능
함수 내에서 직접 선언해 호출할 수도 있고, 
함수의 매개변수로 함수 인자를 전달받아 함수 내에서 호출해서 사용 가능
ex)
def calc(operator_fn, x, y):
    return operator_fn(x, y)

def plus(op1, op2):
    return op1 + op2

def minus(op1, op2):
    return op1 - op2

ret_val = calc(plus, 10, 5)
print("calc(plus, 10, 5)의 결과값: {0}".format(ret_val))
ret_val = calc(minus, 10, 5)
print("calc(minus, 10, 5)의 결과값: {0}".format(ret_val))


람다식
프로그램의 유연성을 높이기 위해 함수를 매개변수로 전달하는 방식 선호
좀 더 간단하고 효율적으로 사용할 수 있게 한 것이 람다식
1) 변수에 저장해 재사용이 가능한 함수처럼 사용함
2) 기존의 함수처럼 매개변수의 인자로 전달함
3) 함수의 매개변수에 직접 인자로 전달함
ex)
def calc(operator_fn, x, y):
    return operator_fn(x, y)

ret_val = calc(lambda a, b: a + b, 10, 5)
print("calc(lambda a, b: a + b, 10, 5)의 결과값: {0}".format(ret_val))
ret_val = calc(lambda a, b: a - b, 10, 5)
print("calc(lambda a, b: a - b, 10, 5)의 결과값: {0}".format(ret_val))


클로저
중첩함수에서 중첩함수를 포함하는 함수의 scope에 접근 가능
중첩함수 자체를 반환값으로 사용한다면?
1) 정보 은닉 구현 가능
2) 전역변수의 남용 방지
3) 메서드가 하나밖에 없는 객체를 만드는 것보다 우아한 구현 가능
ex)
def outer_func():
    id = 0 # 지역변수: 함수 내의 코드 또는 중첩함수에서만 접근 가능

    def inner_func():
        # 변수 id가 중첩함수인 inner_func함수의 지역변수가 아님
        # 변수 id접근 시 outer_func함수 스코프에서 찾게 만듦
        nonlocal id
        id += 1
        return id

    # inner_func() 함수 호출이 아닌 함수에 대한 참조를 반환함에 유의함
    return inner_func

make_id = outer_func()
print("make_id() 호출의 결과: {0}".format(make_id()))
print("make_id() 호출의 결과: {0}".format(make_id()))
print("make_id() 호출의 결과: {0}".format(make_id()))    

# 반지름 입력: 표준 입력을 통해 반지름을 입력받아 숫자로 변환하는 함수
# 원의 면적 계산:  반지름을 통해 원의 면적 계산하는 함수
# 원의 둘례 계산: 반지름을 통해 원의 둘레 계산 함수
# [결과]
# 반지름을 입력하세요: 5
# 원의 면적: 78.50, 원의 둘레:31.40

ex)
PI = 3.14

def input_radius():
    radius_str = input("반지름을 입력하세요: ")
    return float(radius_str)

def calc_circle_area(r):
    return PI * r * r

def calc_circumference(r):
    return 2 * PI * r

radius = input_radius()
circle_area = calc_circle_area(radius)
circumference = calc_circumference(radius)

print("원의 면적: {0:0.2f}, 원의 둘레: {1:0.2f}".format(circle_area, circumference))
"""






















