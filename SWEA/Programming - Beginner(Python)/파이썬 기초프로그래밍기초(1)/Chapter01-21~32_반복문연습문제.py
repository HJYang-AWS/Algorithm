# -*- coding: utf-8 -*-
"""
Chapter 01-21
다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
60점 미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
[입력] 입력없음
[출력]
1번 학생은 88점으로 합격입니다.
2번 학생은 30점으로 불합격입니다.
3번 학생은 61점으로 합격입니다.
4번 학생은 55점으로 불합격입니다.
5번 학생은 95점으로 합격입니다.

풀이) 
score_list = [88, 30, 61, 55, 95]

for i in range(len(score_list)):
    if score_list[i] >= 60:
        print("{0}번 학생은 {1}점으로 합격입니다.".format(i + 1, score_list[i]))
    else:
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(i + 1, score_list[i]))


Chapter 01-22
1부터 100까지의 숫자를 for 문과 range 함수를 이용해 출력하십시오.
[입력] 입력값 없음
[출력] 
1
2
3
4
5
...
99
100

풀이)
for i in range(1, 100 + 1):
    print(i)
    

Chapter 01-23
1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.
[입력] 입력값 없음
[출력] 2 4 6 8 10 12 14 16 18 ... 90 92 94 96 98 100

풀이) 1
for i in range(2, 100 + 1, 2):
    print(i, end=" ")    
    
풀이) 2
for i in range(1, 100 + 1):
    if i % 2 == 0:
        print(i, end=" ")
    
    
Chapter 01-24
1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.
[입력] 입력값 없음
[출력] 1, 3, 5, 7, 9, ... 95, 97, 99

풀이)
print("1", end="")
for i in range(3, 100 + 1, 2):
    print(end=", ")
    print(i, end="")   


Chapter 01-25
1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.
[입력] 입력값 없음
[출력] 1부터 100사이의 숫자 중 3의 배수의 총합: 1683

풀이)
result = 0
for i in range(1, 100 + 1):
    if i % 3 == 0:
        result += i

print("1부터 100사이의 숫자 중 3의 배수의 총합: {0}".format(result))
    

Chapter 01-26
다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
[입력] 입력값 없음
[출력] {'A': 3, 'O': 3, 'B': 2, 'AB': 2}

풀이) 
bloodtype_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
bloodtype_count = [0, 0, 0, 0]

for type in bloodtype_list:
    if type == 'A': bloodtype_count[0] += 1
    if type == 'O': bloodtype_count[1] += 1
    if type == 'B': bloodtype_count[2] += 1
    if type == 'AB': bloodtype_count[3] += 1
        
print("{", end="")
print("'A': {0}, 'O': {1}, 'B': {2}, 'AB': {3}".format(bloodtype_count[0], bloodtype_count[1], bloodtype_count[2], bloodtype_count[3]), end="")
print("}")
    
    
Chapter 01-27
다음은 학생의 점수를 나타내는 리스트입니다.
[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
[입력] 입력값 없음
[출력] 454

풀이) 
score_list = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
result = 0

while len(score_list):
    score = score_list.pop()
    if score >= 80:
        result += score
    
print(result)
    
    
Chapter 01-28
while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
[입력] 입력값 없음
[출력] 
*****
****
***
**
*

풀이) 
for i in range(5, 0, -1):
    while i > 0:
        print("*", end="")
        i -= 1
    print()    


Chapter 01-29
while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
[입력] 입력값 없음
[출력] 
*******
 *****
  ***
   *
   
풀이) 
i, j = 0, 7
while (j >= i):
    for blank in range(i):
        print(" ", end="")
        
    for star in range(j - i):
        print("*", end="")
    
    print("")
    
    j -= 1
    i += 1


Chapter 01-30
다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
[입력] 11
[출력] 
0 1 2 3 4 5 6 7 8 9
0 2 0 0 0 0 0 0 0 0
   
풀이) 
T = int(input())

number_list = [0 for _ in range(10)]
remainder = 0

while True:
    remainder = T % 10
    number_list[remainder] += 1
    T //= 10
    
    if T < 10:
        number_list[T] += 1
        break
    
for i in range(10):
    if i == 9:
        print(i)
        break
    
    print(i, end=" ")
    
print(*number_list)



Chapter 01-31
for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
[입력] 입력값 없음
[출력] 
    *
   **
  ***
 ****
*****
   
풀이)
i, j = 1, 5
while j - i >= 0:
    for _ in range(j - i): print(" ", end = "")
    for _ in range(i): print("*", end="")
    print("")
    i += 1
    

Chapter 01-32
다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.
[입력] 9
[출력] 1001
   
풀이)
T = int(input())

T_binary_list = []
T_binary = int()

while True:
    T_binary_list.append(str(T % 2))
    T //= 2
    if T == 0:
        break
    
T_binary = "".join(T_binary_list)
print(T_binary)
"""

"""
다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
60점 미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
[입력] 입력없음
[출력]
1번 학생은 88점으로 합격입니다.
2번 학생은 30점으로 불합격입니다.
3번 학생은 61점으로 합격입니다.
4번 학생은 55점으로 불합격입니다.
5번 학생은 95점으로 합격입니다.
"""


























