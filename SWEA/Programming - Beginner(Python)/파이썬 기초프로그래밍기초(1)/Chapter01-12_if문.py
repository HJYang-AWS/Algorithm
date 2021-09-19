# -*- coding: utf-8 -*-

'''
if 조건식 :
    명령문
    명령문
    명령문
'''
a, operator, b = 0, "", 0

a = int(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
b = int(input("두 번째 숫자를 입력하세요: "))

if operator == '+':
    print("{0} {1} {2} = {3}".format(a, operator, b, a + b))
elif operator == '-':
    print("{0} {1} {2} = {3}".format(a, operator, b, a - b))
elif operator == '*':
    print("%d * %d = %d" % (a, b, a * b))
elif operator == '/':
    print("%d / %d = %0.2f" % (a, b, a / b))
else:
    print("{0}는 본 프로그램에서 지원하지 않는 연산자입니다.".format(operator))