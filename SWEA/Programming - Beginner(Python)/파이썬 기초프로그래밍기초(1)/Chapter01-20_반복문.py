# -*- coding: utf-8 -*-
"""
for 변수 in 순회할 객체:
    명령문1
    명령문2
     ---
     
range(범위 시작 값, 종료 값, 증감치)
종료값은 생략 불가능, 나머진 가능

dogs = {1: "골든리트리버", 2: "진돗개", 3: "보더콜리"}
for key in dogs:
    print("{0} : {1}".format(key, dogs[key]))
for key, value in dogs.items():
    print("{0} : {1}".format(key, value))
    
dan = range(2, 10)
num = range(1, 10)

for i in dan:
    for k in num:
        print("{0} x {1} = {2:>2}".format(i, k, i * k))
        if k == 9:
            print("")
            
continue문
이후 코드는 건너뛰고 반복문을 계속 실행할 때 사용

break문
반복문을 빠져 나오는 코드
"""




