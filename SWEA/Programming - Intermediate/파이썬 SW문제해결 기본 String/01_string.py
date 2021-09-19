# -*- coding: utf-8 -*-
"""
String
컴퓨터에서 글자를 저장하는 방법
코드체계: 영어 대소문자 합쳐 52개를 대응대는 숫자로 저장하는 것

ASCII코드
7bit 인코딩으로 33개의 출력 불가능한 제어 문자들과 공백을 비록한
95개의 출력 문자들로 이루어져 있음

유니코드(다국어 처리를 위한 표준)
각 국가들은 자국의 문자를 표현하기 위하여 코드체계를 만들어서 사용
다국어 처리를 위해 유니코드를 만듦

Character Set
UCS-2(Universal Character Set 2)
UCS-4(Universal Character Set 4)
유니코드를 저장하는 변수의 크기를 정의
파일을 인식 시 이 파일이 UCS-2, UCS-4인지 인식하고 각 경우를 구분하여
모두 다르게 구현해야 하는 문제 발생

유니코드 인코딩(UTF: Unicode Transformation Format)
UTF-8(in web), min: 8bit, max: 32bit
UTF-16(in windows, Java), min: 16bit, max: 32bit
UTF-32(in unix), min: 32bit, max: 32bit

파이썬 인코딩 방식
2.x 버전 - ASCII
3.x 버전 - 유니코드 UTF-8
2.x 버전의 경우 #-*- coding:utf-8 -*-을 작성해주어야 함

문자열(String)
-> Fixed length, Variable length

Variable length
-> Length controlled(java 언어에서의 문자열)
-> Delimited(C언어에서의 문자열)


C언어에서의 문자열 처리: 문자들의 배열 형태로 구현된 응용 자료형
-> 문자배열에 문자열을 저장할 때는 항상 마지막에 끝을 표시하는 널문자('\n')을 넣어줘야 함
# char ary[] = {'a', 'b', 'c', '\n');
-> 문자열 처리에 필요한 연산을 함수형태로 제공
# strlen(), strcpy(), strcmp(), ...


Java에서의 문자열 처리: 문자열 데이터를 저장, 처리해주는 클래스 제공
-> String 클래스를 이용
# String str = 'abc';
-> 문자열 처리에 필요한 연산을 연ㅅ나자, 메소드 형태로 제공
# +, length(), replace(), split(), substring() 등 풍부한 연산을 제공


파이썬에서의 문자열 처리: char 타입은 없으며, 텍스트 데이터 취급방법이 통일되어 있음
문자열 기호(', ", ''', 쌍따옴표 3개) 등의 방법으로 표현 가능

문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱,
슬라이싱 연산들을 사용할 수 있음
# replace(), split(), isalpha(), find()

문자열은 튜플과 같이 요소값을 변경할 수 없음(immutable)

"""

print("Hello")