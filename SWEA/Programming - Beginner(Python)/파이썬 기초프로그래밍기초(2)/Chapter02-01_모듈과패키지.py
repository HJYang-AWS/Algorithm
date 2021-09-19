# -*- coding: utf-8 -*-
"""
1. 표준 모듈
각기 목적에 맞게 설계되어 있고 다양한 함수, 클래스 등을 제공하며,
별도의 추가 설치 과정 없이 import 문으로 로딩해 사용함

1-1) import 문과 모듈 로딩
ex) import 모듈명
import math
# 각도를 인자로 전달하면 라디안 값을 반환
print("math.radians(90) = {0}".format(math.radians(90)))
# 인자로 전달된 숫자보다 큰 값 중 최소 정수 반환(올림)
print("math.ceil(3.2) = {0}".format(math.ceil(3.2)))
# 인자로 전달된 숫자보다 작은 값 중 최대 정수 반환
print("math.floor(3.2) = {0}".format(math.floor(3.2)))
# 3.14 원주율 값 저장
print("math.pi = {0}".format(math.pi))

1-2) import ~ as ~ 문과 모듈 별칭의 사용
가독성과 편리성을 위해 사용
ex) import 모듈명 as 별칭
import math as m -> math 모듈을 m이란 별칭으로 참조 가능
print("m.radians(90) = {0}".format(m.radians(90)))
print("m.ceil(3.2) = {0}".format(m.ceil(3.2)))
print("m.floor(3.2) = {0}".format(m.floor(3.2)))
print("m.pi = {0}".format(m.pi))

1-3) from ~ import ~ 문을 이용한 선택적 로딩
ex) from 모듈명 import
from ~ import * 문을 사용하면 모듈 혹은 패키지가 가지고 있는
함수, 값 등의 모든 정보를 로딩해 사용할 수 있음
from math import *
from math import radians, ceil, floor, pi
-> 명시적으로 선언해 사용하면, 해당 함수가 어느 모듈에서 
로딩되어 사용했는지 명확히 알 수 있으므로 사용을 권장함
print("radians(90) = {0}".format(radians(90)))
print("ceil(3.2) = {0}".format(ceil(3.2)))
print("floor(3.2) = {0}".format(floor(3.2)))
print("pi = {0}".format(pi))


2) sys 모듈
시스템과 관련된 정보에 접근하거나 명령행에서 전달된
명령행 매개변수로부터 인자 값을 읽어올 때 활용됨

import sys

# sys.argv: 리스트 타입, 명령행에서 python 명령에 전달된
            인자들의 정보를 담고 있음
print("sys.argv => {0} {1}".format(type(sys.argv), sys.argv))

for i, val in enumerate(sys.argv):
    print("sys.argv[{0}] => {1}".format(i, val))
    

3) random 모듈
난수(연속적인 임의의 수)를 생성하는 기능 제공

from random import random, uniform, randrange, choice, choices, sample, shuffle

# random 함수: 0.0 <= N < 1.0 범위의 부동소수점 난수 N 반환
print("random() => {0}".format(random()))

# uniform 함수: 지정된 범위 내의 부동소수점 난수 N 반환
print("uniform({0}, {1}) => {2}".format(1.0, 10.0, uniform(1.0, 10.0)))

start, stop, step = 1, 45, 2
# randrange(start, stop): start <= N < end 범위의 정수형 난수 N 반환
print("randrange({0}, {1}) => {2}".format(start, stop, randrange(start, stop)))
# range(stop): 0 <= N < stop 범위의 저웃형 난수 N 반환
print("randrange({0}) => {1}".format(stop, randrange(stop)))
# start로부터 end까지 step 만큼의 간격을 가지는 범위 중 정수형 난수 N 반환
print("randrange({0}, {1}, {2}) => {3}".format(start, stop, step,
      randrange(start, stop, step)))

data_list = [1, 2, 3, 4, 5]
# choices() 함수: 인자로 전달된 시퀀스 객체의 항목 중 임의의 K개 반환 복원 추출 기능을 가진 시뮬레이션 함수
print("choice({0}) => {1}".format(data_list, choice(data_list)))
print("choices({0}) => {1}".format(data_list, choices(data_list, k=2)))
# sample() 함수: 인자로 전달된 시퀀스 객체, 혹은 set 객체항목 중 임의의 K개 반환, 비복원추출 기능을 가진 시뮬레이션 함수
print("sample({0}) => {1}".format(data_list, sample(data_list, k=5)))
# shuffle() 함수: 인자로 전달된 시퀀스 객체의 항목을 뒤섞는 함수, 반환 값은 없고 원본 객체의 항목의 순서를 뒤섞음
shuffle(data_list)
print("data_list => {0}".format(data_list))


4) datetime 모듈
날짜와 시간 정보를 확인하고 조작하는 클래스, 함수 등을 제공함
ex)
from datetime import datetime, timezone, timedelta

now = datetime.now()
print("{0}-{1:02}-{2:02} {3:02}:{4:02}:{5:02}".format(now.year, now.month, now.day, now.hour, now.minute, now.second))

# %Y: 네 자리의 연도 정보
# %m: 월 정보
# %d: 일 정보
# %H: 24시간 체계의 시간 정보
# %M:분 정보
# %S: 초 정보
fmt = "%Y{0} %m{1} %d{2} %H{3} %M{4} %S{5}"
print(now.strftime(fmt).format(*"년월일시분초"))



2. 서드파티 모듈
다른 누군가에 의해 만들어져 배포되고 공유되는 모듈
파이썬은 기본적으로 pip모듈을 함꼐 설치
서드파티 모듈 설치 및 제거 방법
pip install 모듈명: 설치
pip uninstall 모듈명: 제거
ex)
from datetime import datetime
from pytz import common_timezones, timezone, utc

# 타입존 정보 출력
for tz in list(common_timezones):
    # common_timezones 객체를 리스트 객체로 변환해서 반복문을 수행
    # common_timezones 객체는 timezones 정보들을 갖고 있음
    if tz.lower().find("seoul") >= 0:
        # 타임존 정보는 문자열로, 문자열은 모두 소문자로 변환
        print(tz)

tz_utc = timezone(utc.zone)
tz_seoul = timezone("Asia/Seoul")
tz_pacific = timezone("US/Pacific")
tz_paris = timezone("Europe/Paris")

# %Z: 타임존의 명칭, %z: UTC 기준시각과의 시간 차이
fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# UTC 현재 시각
now_utc = datetime.now(tz_utc)
print(now_utc.strftime(fmt))

# Asia/Seoul 타임존
now_seoul = now_utc.astimezone(tz_seoul)
print(now_seoul.strftime(fmt))

# US/Pacific 타임존
now_pacific = now_seoul.astimezone(tz_pacific)
print(now_pacific.strftime(fmt))

# Europe/Paris 타임존
now_paris = now_pacific.astimezone(tz_paris)
print(now_paris.strftime(fmt))



3. 사용자 정의 모듈
파이썬에서 모듈은 2가지 목적으로 구분
1) 실행의 목적(파이썬 명령에 의해 실행)
2) 라이브러리의 목적(import 문에 의해 로딩)
ex)
import module_mycalc_1, module_mycalc_2

op1, op2 = 2, 3

result = module_mycalc_1.plus(op1, op2)
print("plus({0}, {1}) => {2}".format(op1, op2, result))

result = module_mycalc_1.minus(op1, op2)
print("plus({0}, {1}) => {2}".format(op1, op2, result))

result = module_mycalc_2.multiply(op1, op2)
print("plus({0}, {1}) => {2}".format(op1, op2, result))

result = module_mycalc_2.divide(op1, op2)
print("plus({0}, {1}) => {2}".format(op1, op2, result))


모듈의 __name__ 속성
1) 실행 목적의 모듈은 __name__ 속성에 "__main__" 문자열 값이 들어가 있음
2) 라이브러리 목적의 모듈은 __name__ 속성에 모듈의 이름이 저장되어 있음
    
    

4. 사용자 정의 패키지
모듈이 모여 폴더를 구성하면 패키지를 만들 수 있다.
패키지를 사용하는 방법은 모듈과 동일하다.
from 패키지명 import 모듈명
ex)
from package_mycalc import module_mycalc_1, module_mycalc_2
# from package_myclac import -> 모든 모듈 로딩

op1, op2 = 2, 3

result = module_mycalc_1.plus(op1, op2)
print("plus({0}, {1}) => {2}".format(op1, op2, result))

result = module_mycalc_1.minus(op1, op2)
print("plus({0}, {1}) => {2}".format(op1, op2, result))

result = module_mycalc_2.multiply(op1, op2)
print("plus({0}, {1}) => {2}".format(op1, op2, result))

result = module_mycalc_2.divide(op1, op2)
print("plus({0}, {1}) => {2}".format(op1, op2, result))
"""
































