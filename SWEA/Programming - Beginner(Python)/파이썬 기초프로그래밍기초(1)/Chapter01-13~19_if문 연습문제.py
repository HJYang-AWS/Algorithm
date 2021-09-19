# -*- coding: utf-8 -*-
"""
Chapter01-13
다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오.
입력: 9
출력:
1(은)는 9의 약수입니다.
3(은)는 9의 약수입니다.
9(은)는 9의 약수입니다.

풀이)
T = int(input())
for factor in range(1, T + 1):
    if T % factor == 0:
        print("%d(은)는 %d의 약수입니다." % (factor, T))
  
        
Chapter01-14
다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
(단, 약수가 2개일 경우 소수임을 나타내십시오)
입력: 5
출력:
1(은)는 5의 약수입니다.
5(은)는 5의 약수입니다.
5(은)는 1과 5로만 나눌 수 있는 소수입니다.

풀이)
T = int(input())
count = 0
factor = 1

while(True):
    if T % factor == 0:
        print("%d(은)는 %d의 약수입니다." % (factor, T))
        count += 1
    if factor == T:
        if count == 2:
            print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." % (T, T))
            break
        else:
            break
    factor += 1
  
    
Chapter01-15
다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.
입력: b
출력: b 는 소문자 입니다.

풀이)
T = input()
if ord('a') <= ord(T) and ord('z') >= ord(T):
    print("{0} 는 소문자 입니다.".format(T))
elif ord('A') <= ord(T) and ord('Z') >= ord(T):
    print("{0} 는 대문자 입니다.".format(T))
    

Chapter01-16
다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
[입력]
두 줄에 ["가위", "바위", "보"] 중 하나가 차례로 주어진다.
[출력]
첫 번째 사람은 Man1, 두 번째 사람은 Man2라고 하고, 이긴 사람의 결과를 출력한다.
예를 들어, Man1이 이겼을 경우 Result : Man1 Win! 이라고 출력한다.
단, 비긴 경우는 Result : Draw 라고 출력한다.

풀이)
T = list()
for _ in range(2):
    T.append(input())

if T[0] == '가위':
    if T[1] == '가위': print("Result : Draw")
    elif T[1] == '바위': print("Result : Man2 Win!")
    elif T[1] == '보': print("Result : Man1 Win!")
elif T[0] == '바위':
    if T[1] == '가위': print("Result : Man1 Win!")
    elif T[1] == '바위': print("Result : Draw")
    elif T[1] == '보': print("Result : Man2 Win!")
elif T[0] == '보':
    if T[1] == '가위': print("Result : Man2 Win!")
    elif T[1] == '바위': print("Result : Man1 Win!")
    elif T[1] == '보': print("Result : Draw")
    

Chapter01-17
다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
출력 시 아스키코드를 함께 출력합니다.
입력: c
출력: c(ASCII: 99) => C(ASCII: 67)

풀이)
T = input()

if ord('a') <= ord(T) and ord(T) <= ord('z'):
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(T, ord(T), T.upper(), ord(T.upper())))
elif ord('A') <= ord(T) and ord(T) <= ord('Z'):
    print("{0}(ASCII: {1} => {2}(ASCII: {3})".format(T, ord(T), T.lower(), ord(T.lower())))
    
    
Chapter01-18
1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.
출력:
7,14,21,28,42,49,56,63,77,84,91,98,112,119,126,133,147,154,161,168,182,189,196

풀이)
for i in range(1, 200 + 1):
    if i == 7:
        print(i, end="")
    if i > 7 and i % 7 == 0 and i % 5 != 0:
        print(',', end="")
        print(i, end="")


Chapter01-19
100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.
[출력]
200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,268,280,282,284,286,288

풀이)
print(200, end="")
for i in range(201, 300 + 1):
    k = i
    if (k % 10) % 2 == 0:
        k //= 10
        if (k % 10) % 2 == 0:
            k //= 10
            if k % 2 == 0:
                print(',', end="")
                print(i, end="")
"""

        






























    
    