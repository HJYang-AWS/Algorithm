# -*- coding: utf-8 -*-
"""
함수를 새로 만드는 것보단 만들어져 있는 내장 함수를 쓰는 것이 빠르다

1. 수칙연산함수
abs(): 인자로 숫자를 전달하면 그 숫자의 절대값을 반환하는 함수
ex)
val = -10
print("abs({0}) => {1}".format(val, abs(val)))


divmod(): 첫번째 인자를 두 번쨰 인자로 나눴을 때의 목과 나머지를 튜플 객체로 반환하는 함수
ex)
val1, val2 = 9, 5
result_tuple = divmod(val1, val2)

print("divmod({0}, {1}) => 몫: {2}, 나머지: {3}".format(val1, val2, *result_tuple))


pow(): 첫 번째로 전달된 인자 값에 대해 두 번째로 전달된 인자 갑승로 제곱한 결과를 반환하는 함수
ex)
data_list = [1, 2, 3, 4]

print("pow({0}, 2) => {1}".format(data_list[2], pow(data_list[2], 2)))
print("list(map(lambda x: pow(x, 2), {0})) => {1}"
      .format(data_list, list(map(lambda x: pow(x, 2), data_list))))

2. 시퀀스형/반복 가능한 자료형을 다루는 함수
all(): 반복가능한 자료형인 List, Tuple, Set, dictionary, 문자열 등을 인자로 전달하여
       항목 모두가 True로 평가되면 True를 반환하고, False로 평가되는
       항목이 하나라도 있으면 False를 반호나하는 함수
ex)
val = [True, True, True]
print("all({0}) => {1}".format(val, all(val)))
# True 반환

val = [10, 20, 30]
print("all({0}) => {1}".format(val, all(val)))
# True 반환

val = [10, 20, 0]
print("all({0}) => {1}".format(val, all(val)))
# 0 항목으로 False 반환

val = [10, 20, ""]
print("all({0}) => {1}".format(val, all(val)))
# 공백문자열로 인해 False 반환

val = [10, 20, False]
print("all({0}) => {1}".format(val, all(val)))
# False 항목으로 False 반환

val = [10, 20, None]
print("all({0}) => {1}".format(val, all(val)))
# None 항목으로 인해 False 반환


any(): 반복 가능한 자료형인 List, Tuple, Set, dictionary, 문자열 등을 인자로 전달하며
       항목 모두가 False로 평가되면 False를 반환하고,
       True로 평가되는 항목이 하나라도 있으면 True를 반환하는 함수
ex)
val = [True, True, True]
print("any({0}) => {1}".format(val, any(val)))
# True 반환

val = [10, 20, 30]
print("any({0}) => {1}".format(val, any(val)))
# True 반환

val = [10, 20, 0]
print("any({0}) => {1}".format(val, any(val)))
# 0 항목이 있어도 True 반환

val = [True, True, ""]
print("any({0}) => {1}".format(val, any(val)))
# 공백문자열이 있어도 True 반환

val = [10, 20, False]
print("any({0}) => {1}".format(val, any(val)))
# True 반환

val = [10, 20, None]
print("any({0}) => {1}".format(val, any(val)))
# None이 있어도 True 반환

val = [False, False, False]
print("any({0}) => {1}".format(val, any(val)))
# False 반환


enumerate(): List, Tuple, 문자열과 같은 시퀀스형을 입력받아
             인덱스를 포함하는 튜플 객체를 항목으로 구성하는
             enumerate 객체를 반환하는 함수
ex)
data_list = [10, 20, 30, 40, 50]

for idx, val in enumerate(data_list): # data_list를 enumerate 객체로 변환
    print("data_list[{0}]: {1}".format(idx, val))
    
print("-" * 25)

for obj in enumerate(data_list):
    print("{0}: {1}, {2}".format(type(obj), obj[0], obj[1]))
    # 변수 obj: 튜플 객체로 첫 번째 항목에 접근해 인덱스를, 두 번째 항목에 접근해 값을 출력함
print("-" * 25)

for obj in enumerate(data_list):
    print("{0}: {1}, {2}".format(type(obj), *obj))
    
    
filter(): 조건에 해당하는 항목을 걸러내는 함수
첫 번째 매개변수: 인자를 받아 True or False 반환
두 번째 매개변수: 반복가능한 자료형을 인자로 받는다.
이때 자료형 인자가 첫번째 매개변수의 인자로 전달된다.
ex)
def iseven(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ret_val = filter(iseven, numbers)
# ret_val = filter(lambda n: n % 2 == 0, numbers)
print("{0}".format(type(ret_val))) # filter 객체 타입
print("{0}".format(list(ret_val)))


list(), tuple(), set(), dict()
: 각각 반복 가능한 자료형을 인자로 전달 받아
  리스트, 퓨틀, 셋, 딕셔너리로 변환해 반환하는 함수
ex)
data_str = "Hello"

data_list = list(data_str)
print("list('{0}') => {1} {2}".format(data_str, type(data_list), data_list))

data_tuple = tuple(data_list)
print("tuple({0}) => {1} {2}".format(data_list, type(data_tuple), data_tuple))

data_set = set(data_tuple)
print("set({0}) => {1} {2}".format(data_tuple, type(data_set), data_set))

data_dict = dict(enumerate(data_set))
print("dict({0}) => {1} {2}".format(data_set, type(data_dict), data_dict))


map(): 두 번째 인자로 반복 가능한 자료형을 전달 받아
자료형의 각 항목에 대해 첫 번째 인자로 전달 받은 함수를 적용한 결과를
맵 객체로 반환하는 함수
ex)
data_list = list('abcdef')
result = list(map(lambda x: x.upper(), data_list))

print("list(map(lambda x: x.upper(), {0})) => {1} {2}".format(data_list, type(result), result)) 
# result 객체는 모든 값이 대문자로 변환된 항목을 가진 list 객체임


max(): 반복 가능한 자료형을 인자로 받아 항목 중 가장 큰 값을 반환
min(): 반복 가능한 자료형을 인자로 받아 항목 중 가장 작은 값을 반환
ex)
data_list = list([10, 25, 30, 45, 50])
print(data_list)

print("{0} => min: {1}, max: {2}".format(data_list, min(data_list), max(data_list)))


range() : 시퀀스형 객체를 생성하는 함수
첫 번째 인자: 시작값
두 번째 인자: 종료값, 종료값으로 사용된 인자의 값은 포함되지 않음
세 번째 인자: 증감치
ex)
data_list1 = list(range(0, 10, 1))
data_list2 = list(range(0, 10))
data_list3 = list(range(10))

print("list(range(0, 10, 1)) => {0}".format(data_list1))
print("list(range(0, 10)) => {0}".format(data_list2))
print("list(range(10)) => {0}".format(data_list3))
    
    
sorted(): 반복 가능한 자료형을 인자로 전달받아
항목들로부터 정렬된 리스트를 생성해 반환하는 함수
ex)
data_list = [3, 8, 12, 2, 5, 11]

asc_result = sorted(data_list)
# desc_result = sorted(data_list, reverse=True)

print("{0} {1}".format(type(data_list), data_list))
print("{0} {1}".format(type(asc_result), asc_result))

print("-" * 25)

desc_result = list(reversed(asc_result)) # 내림차순의 리스트 객체 생성
print("{0} {1}".format(type(desc_result), desc_result))    


zip(): 둘 이상의 반복 가능한 자료형을 인자로 전달받아,
동일 위치의 항목을 묶어 튜플을 항목으로 구성하는 zip객체를 생성하는 함수
! 인자로 전달된 객체는 동일 자료형이면서, 항목의 개수가 같아야 한다
ex)
data_list1 = [1, 2, 3]
data_list2 = [4, 5, 6]
data_list3 = ["a", "b", "c"]

print("list(zip({0}, {1})) => {2}"
      .format(data_list1, data_list2, list(zip(data_list1, data_list2))))
print("list(zip({0}, {1}, {2})) => {3}"
      .format(data_list1, data_list2, data_list3, list(zip(data_list1, data_list2, data_list3))))
print("list(zip({0}, {1})) => {2}"
      .format(data_list3, data_list1, dict(zip(data_list3, data_list1))))


3. 변환 함수
chr(): 정수 형태의 유니코드 값을 인자로 전달받아 해당 코드의 문자를 반환하는 함수
ord(): 문자를 인자로 전달받아 유니코드 값(10진 정수)을 반환하는 함수
hex(): 10진 정수 값을 인자로 전달 받아 16진수로 변환된 값을 반환하는 함수
ex)
val = 65
print("chr({0}) => {1}".format(val, chr(val)))

val = 97
print("chr({0}) => {1}".format(val, chr(val)))

val = 0xac00
print("chr({0:x}) => '{1}'".format(val, chr(val)))

val = 'A'
print("ord({0}) => {1}".format(val, ord(val)))

val = 'a'
print("ord({0}) => {1}".format(val, ord(val)))

val = '가'
print("ord('{0}') => '{1}'(10진수)".format(val, ord(val)))
print("ord('{0}') => '{1}'(16진수)".format(val, hex(ord(val))))


int(): 인자로 전달된 숫자 형식의 문자열, 부동소수점 숫자를 정수로 변환한 값을 반환하는 함수
float(): 인자로 전달된 숫자 형식의 문자열, 정수를 부동소수점 숫자로 변환한 값을 반환하는 함수
str(): 인자로 전달된 객체에 대한 문자열 변환 값을 반환하는 함수
ex)
x = '10'
y = '3C'
z = 4.5

print("2진수 표현인 문자열 '{0}'은 10진수 {1}로 변환됩니다.".format(x, int(x, 2)))
print("16진수 표현인 문자열 '{0}'은 10진수 {1}로 변환됩니다.".format(x, int(y, 16)))
print("int({1})은 {0} {1}을 {2} {3}로 변환됩니다.".format(type(z), z, type(int(z)), int(z)))
print("int('{1}')은 {0} '{1}'을 {2} {3}로 변환됩니다.".format(type(x), x, type(int(x)), int(x)))
print("int('{1}')은 {0} {1}을 {2} '{3}'로 변환됩니다.".format(type(z), z, type(str(z)), str(z)))


객체조사를 위한 함수
dir(): 인자로 전달된 객체가 가지고 있는 변수, 메서드와 같은 속성 정보를 리스트 객체로 반환
인자를 전달하지 않고 호출하면 현재 지역 스코프에 대한 정보를 리스트 객체로 반환
ex)
print("dir() => {0}".format(dir()))
# 지역 스코프에 대한 정보를 리스트 객체로 반환
data_str = "Hello Python!"
print("dir(data_str) => {0}".format(dir(data_str)))
# 문자열이 가지고 있는 많은 메소드 정보를 리스트 객체에 담아 반환
data_list = [10, 20, 30, 40, 50]
print("dir(data_list) => {0}".format(dir(data_list)))
# 정수형 list 객체가 가지고 있는 메소드 정보들을 list 객체에 담아 반환
data_dict = {'key1': 10, 'key2': 20, 'key3': 30}
print("dir(data_dict) => {0}".format(dir(data_dict)))
# 딕셔너리 객체가 가지고 있는 메소드 정보들을 리스트 객체에 담아 반환


globals(): 현재의 전역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수
-> 전역변수와 함수, 클래스의 정보 포함
locals(): 현재의 지역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수
-> 매개변수를 포함한 지역변수와 중첩함수의 정보 포함
ex)
class MyClass:
    pass

def test_fn(param):
    # 중첩함수로 inner_fn 함수를 가짐
    def inner_fn(): 
        pass
    val1 = 5
    val2 = 8
    
    # Locals 함수가 반환한 딕셔너리 객체에 대해 items 함수로 리스트 객체를 얻음
    for item in locals().items():
        print("\t{0} : {1}".format(item[0], item[1]))
        # 첫 번째 항목인 키를, 두 번째 항목인 값을 접근해 지역 정보 출력
        
value1 = 10
value2 = 20
obj1 = MyClass()

g = dict(globals())
# globals함수가 반환한 dict 객체의 현재 상태를 복사해 g에 저장

print("globals()")
# g의 items 함수로 반환된 리스트 객체를 얻음
for item in g.items():
    print("\t{0}: {1}".format(item[0], item[1]))
    # 튜플 객체인 각 항목에 대해 첫번째 항목인 키,
    # 두 번째 항목인 값에 접근해 전역 정보 출력
    
print("\n\nlocals()")
# test_fn 함수를 호출하면서 인자 값 10을 전달해서 4행~10행까지 차례대로 실행
test_fn(10)


id(): 인자로 전달된 객체의 고유 주소(참조값)를 반환하는 함수
ex)
x, y, z = 10, 10, '10'
print("{0} x의 주소 값: {1}".format(type(x), hex(id(x))))
print("{0} y의 주소 값: {1}".format(type(y), hex(id(y))))
print("{0} z의 주소 값: {1}".format(type(z), hex(id(z))))


isinstance()
첫번째 인자로 전달된 객체가 두 번째 인자로 전달된 클래스의
인스턴스인지에 대한 여부를 True/False로 반환하는 함수
issubclass()
첫 번째 인자로 전달된 클래스가 두 번쨰 인자로 전달된 클래스의
서브클래스인지에 대한 여부를 True/False로 반환하는 함수
ex)
class Parent:
    pass

class Child(Parent):
    pass

p = Parent()
c = Child()

print("p 객체는 Parent 클래스의 인스턴스입니까? {0}".format(isinstance(p, Parent)))
print("c 객체는 Child 클래스의 인스턴스입니까? {0}".format(isinstance(c, Child)))
print("c 객체는 Parent 클래스의 인스턴스입니까? {0}".format(isinstance(c, Parent)))
print("p 객체는 Child 클래스의 인스턴스입니까? {0}".format(isinstance(p, Child)))
print("Child 클래스는 Parent 클래스의 서브클래스입니까? {0}".format(issubclass(Child, Parent)))


eval()
실행 가능한 표현식의 문자열을 인자로 전달받아
해당 문자열의 표현식을 실행한 결과값을 반환하는 함수
ex)
expr = "2 + 5 + 3"
print("{0} => {1}".format(expr, eval(expr)))

expr = "'hello, python!'.upper()"
print("{0} => {1}".format(expr, eval(expr)))


파이썬 활용
map() 함수와 filter() 함수 활용하여 프로그램 만들기
[결과]
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
항목 x에 적용할 표현식을 입력하세요: x + 3
항목 x를 필터링할 조건의 표현식을 입력하세요: x % 5 == 0
map 함수의 적용 결과: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
filter 함수의 적용 결과: [5, 10, 15, 20]

[풀이]
data_list = list(range(1, 20 + 1))

print("data_list: {0}".format(data_list))

map_list = list(map(lambda x: x + 3, data_list))
print("data_list에 대한 map 함수의 적용 결과: {0}".format(map_list))

filter_list = list(filter(lambda x: x % 5 == 0, map_list))
print("map_list에 대한 filter 함수의 적용 결과: {0}".format(filter_list))

map_str = input("항목 x에 대해 적용할 표현식을 입력하세요: ")
map_str_list = list(map(lambda x: eval(map_str), data_list))
print("data_list에 대한 map, eval 함수의 적용 결과: {0}".format(map_str_list))

filter_str = input("항목 x에 대해 필터링할 조건의 표현식을 입력하세요: ")
filter_str_list = list(filter(lambda x: eval(filter_str), map_str_list))
print("map_str_list에 대한 filter, eval 함수의 적용 결과: {0}".format(filter_str_list))
"""
















