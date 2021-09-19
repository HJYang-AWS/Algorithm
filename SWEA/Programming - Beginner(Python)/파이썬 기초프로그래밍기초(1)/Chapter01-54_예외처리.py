# -*- coding: utf-8 -*-
"""
1. 구문오류와 예외
구문오류: 해석 단계에서 발생
예외(Exception): 실행 단계에서 발생
오류 메시지를 잘 확인하는 습관을 들여야 함

1) 구문오류
SyntaxError가 발생한 경우
파이썬의 인터프리터가 해석하지 못해 발생함.
오타나 문법적으로 필수적인 요소가 빠지지 않았는지 찾아 재코딩해야 함

2) 예외
문법적인 문제는 없지만 실행중 발생하는 오류


2. 예외 처리 방법
2-1) if 문을 이용한 예외의 처리
-> 정상적인 흐름을 제어할 경우에만 사용 가능
-> 예외의 발생을 사전에 처리
ex) isdigit(): 숫자를 받으면 True, 아니면 False를 반환

2-2) try ~ except 문을 이용한 예외의 처리
-> 예외가 발생했을 때 except 문으로 처리

2-3) try ~ except ~ else 문을 이용한 예외의 처리
-> 예외가 발생했을 때 except 문으로 처리
-> 예외가 발생하지 않았을 때 else 문으로 처리

2-4) try ~ except ~ else ~ finally 문을 이용한 예외의 처리
-> 예외가 발생했을 때 except 문으로 처리
-> 예외가 발생하지 않았을 때 else 문으로 처리
-> 예외 발생과 상관없이 finally 문을 실행


3. 예외 객체
코드를 실행하는 중 오류가 발생하면 만들어진 것으로,
오류 발생과 관련한 정보를 가지고 있음
ex) except Exception as ex:
        print("{0}: {1}".format(type(ex), ex))

3-1) 다중 except 문을 이용한 예외 객체에 따른 처리의 분기
ex)
except ValueError as ve: 
-> try 문에서 valueError 발생 시 ValueError as ve 코드를 사용해
   except 문의 블록에서 ve 참조
except ZeroDivisionError as ze:
-> try 문에서 ZeroDivisionError 발생 시 ze 참조
except Exception as ex:
-> tyr 문에서 ValueError, ZeroDivisionError 이외의 상황 발생 시 ex 참조


4. 강제로 예외를 발생시키는 방법
특정 조건에서 예외 객체를 만들어 예외를 일으킬 수 있음

raise 문을 이용한 강제 예외 발생
ex)
def calc_area(w, h):
    if w.isdigit() and h.isdigit():
        return int(w) * int(h)
    else:
        raise ValueError("숫자가 아닌 값이 입력되었습니다.")
        # raise 문을 이용해 강제로 ValueError 예외 상황을 일으킴


[예외처리기능을 가진 프로그램 만들기]
사용자로부터 인덱스를 입력 받아 숫자로 변환하는 함수
[결과1]
data_list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
인덱스로 사용할 숫자를 입력하세요: o
<class "ValueError">, invalid literal for int() with base 10: 'o'

[결과2]
data_list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
인덱스로 사용할 숫자를 입력하세요: 10
<class 'IndexError'> list index out or range
인덱스는 0 ~ 9까지 사용할 수 있습니다.
[9]: 10

[풀이]
# 함수를 이용한 예외처리
def input_index():
    num = 0
    try:
        num = int(input("인덱스로 사용할 숫자를 입력하세요: "))
    except ValueError as exception:
        raise exception
    else:
        return num
        

# 경계 영역 안에서 print 하는 함수
def print_in_bounds(list, index):
    value = 0
    try:
        value = list[index]
    except IndexError as exception:
        print("{0}, {1}".format(type(exception), exception))
        index = len(list) - 1
        print("인덱스는 0 ~ {0}까지 사용할 수 있습니다.".format(index))
        value = list[index]
    finally:
        print("[{0}]: {1}".format(index, value))


data_list = [ i for i in range(1, 10 + 1)]
print("data_list: {0}".format(data_list))

try:
    index = input_index()
    print_in_bounds(data_list, index)
except Exception as exception:
    print(exception)

"""

    
























