# -*- coding: utf-8 -*-
"""
Chapter02-03
한 학생의 국어, 수학 점수를 튜플로 저장하고 이 튜플을 항목으로 갖는 리스트 객체가 있습니다.
이 때 첫 번째 학생은 (90, 80), 두 번째 학생은 (85, 75), 세 번째 학생은 (90, 100)의 점수를 갖습니다.
다음과 같이 결과를 만들기 위한 프로그램을 작성하십시오.
[입력] 입력없음
[출력]
1번 학생의 총점은 170점이고, 평균은 85.0입니다.
2번 학생의 총점은 160점이고, 평균은 80.0입니다.
3번 학생의 총점은 190점이고, 평균은 95.0입니다.

[풀이]
student_scores = tuple(((90, 80), (85, 75), (90, 100)))

for i in range(len(student_scores)):
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2}입니다.".format(i + 1, sum(student_scores[i]), sum(student_scores[i]) / 2))
    
    
Chapter02-04
리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
[입력] 입력없음
[출력] Pythn s pwrfl... nd fst; plys wll wth thrs; rns vrywhr; s frndly & sy t lrn; s Opn.

[풀이]
words = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

word_list = [word for word in words if word != 'a' and word != 'e' and word != 'i' and word != 'o' and word != 'u']

print("".join(word_list))


Chapter02-05
다음의 결과와 같이 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를
제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.

[입력] 입력없음
[출력] [[2, 4, 8, 10, 16], [], [4, 8, 16, 20, 32], [5, 10, 20, 25, 40], [], [], [8, 16, 32, 40, 64], []]

[풀이]
result = []

for i in range(2, 10):
    dan = []
    for j in range(1, 10):
        if i * j % 3 != 0 and i * j % 7 != 0:
            dan.append(i * j)
    result.append(dan)
print(result)


Chapter02-06
리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
[입력]
10
10
20
30
40
[출력]
입력된 값 [10, 10, 20, 30, 40]의 평균은 22.0입니다.

[풀이]
T = [ int(input()) for i in range(5)]
average = sum(T) / 5
print("입력된 값 {0}의 평균은 {1}입니다.".format(T, average))


Chapter02-07
다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.
[입력] 12
[출력] [1, 2, 3, 4, 6, 12]

[풀이]
result = []

T = int(input())

for i in range(1, T + 1):
    if T % i == 0:
        result.append(i)
print(result)


Chapter02-08
다음의 결과와 같이 정수를 입력하면 리스트 내포를 이용해
약수 리스트를 출력하는 코드를 작성하십시오.
[입력] 32
[출력] [1, 2, 4, 8, 16, 32]

[풀이]


Chapter02-09
[1, 3, 11, 15, 23, 28, 37, 52, 85, 100] 와 같은 리스트 객체가 주어졌을 때
다음의 결과를 출력하는 짝수만 항목으로 가지는 리스트 객체를 생성하는 코드를 작성하십시오.

[입력] 입력없음
[출력] [28, 52, 100]

[풀이]
list_obj = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
list_even_obj = []

for obj in list_obj:
    if obj % 2 == 0:
        list_even_obj.append(obj)

print(list_even_obj)


Chapter02-10
리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력] [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

[풀이]
fibonacci = [1, 1]

for i in range(1, 9):
    fibonacci.append(fibonacci[i] + fibonacci[i - 1])

print(fibonacci)


Chapter02-11
리스트 내포 기능을 이용하여 1부터 20사이의 숫자 중 3의 배수가 아니거나
5의 배수가 아닌 숫자들의 제곱 값으로 구성된 리스트 객체를 출력하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력] [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 256, 289, 324, 361, 400]

[풀이]
data_list = [i ** 2 for i in range(1, 20 + 1) if i % 3 != 0 or i % 5 != 0]
print(data_list)


Chapter02-12
사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오.
예를 들어 123을 입력하면 1 + 2 + 3 = 6의 결과를 반환합니다.
[입력] 12345
[출력] 15

[풀이]
num = int(input())

result = 0
if num < 0:
    print("잘못된 입력입니다.")

while num >= 10:
    result += (num % 10)
    num //= 10
result += num
        
print(result)


Chapter02-13
입력 받은 문자열 리스트를 가나다 순으로 따로 묶으려고 합니다.
다음과 같은 리스트가 주어졌을 때 결과처럼 가나다순(사전순)으로
따로 묶은 리스트가 출력되도록 리스트 내포를 이용한 프로그램을 작성하십시오.
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),
           ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',
             '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
             '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
[입력] 입력없음
[출력]
[['계시다', '가지다', '그', '개'], ['놀이'], ['들다', '다', '뒤', '듣다', '데리다'], [],
 ['막', '무척', '마리'], ['부모님', '비용', '비행기', '보이다'], ['싶다', '수출'],
 ['원래', '아이', '옳다'], ['좀', '자르다', '정도'], ['처리', '최초'], [], [], [], ['함께']]

[풀이]
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),
           ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',
             '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
             '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
outputWord = []

for i in range(len(dicBase)):
    sort_word = []
    for word in inputWord:
        if ord(dicBase[i][0]) <= ord(word[0]) <= ord(dicBase[i][1]):
            sort_word.append(word)
    outputWord.append(sort_word)
print(outputWord)


Chapter02-14
콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.
[입력] 12, 34, 56, 78
[출력]
[12, 34, 56, 78]
(12, 34, 56, 78)

[풀이]
num_list = list(map(int, input().split(sep=", ")))
num_tuple = tuple(num_list)
print(num_list)
print(num_tuple)


Chapter02-15
다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.
[입력] 2, 3, 4, 5
[출력] 12.57, 18.85, 25.13, 31.42

[풀이]
import math

PI = math.pi

num_list = list(map(float, input().split(sep=", ")))

circumference_list = [round(2 * PI * r, 2) for r in num_list]

for idx in range(len(circumference_list)):
    if idx == len(circumference_list) - 1:
        print(circumference_list[idx])
    else:
        print(circumference_list[idx], end=", ")


Chapter02-16
다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고,
이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.
[입력]
[출력]

[풀이]
row, col = map(int, input().split(sep=", "))

matrix = [ [r * c for c in range(col)] for r in range(row) ]
print(matrix)


Chapter02-17
단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.
[입력] python, hello, world, hi
[출력] hello, hi, python, world

[풀이]
word_list = list(map(str, input().split(sep=", ")))

for i, word in enumerate(sorted(word_list)):
    if i == len(word_list) - 1:
        print(word)
    else:
        print(word, end=", ")


Chapter02-18
콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는
리스트 내포 기능을 이용한 프로그램을 작성하십시오.
[입력] 1, 2, 3, 4, 5
[출력] 1, 3, 5

[풀이]
num_list = list(map(int, input().split(sep=", ")))
for i in range(len(num_list)):
    if num_list[i] % 2 == 1:
        if i == len(num_list) - 1:
            print(num_list[i])
        else:
            print(num_list[i], end=", ")


Chapter02-19
주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오.
[입력] 입력 없음
[출력]
(1, 2, 3, 4, 5)
(6, 7, 8, 9, 10)

[풀이]
data_tuple = (1,2,3,4,5,6,7,8,9,10)
front_data_tuple = tuple(data_tuple[:len(data_tuple)//2])
back_data_tuple = tuple(data_tuple[len(data_tuple)//2:])
print(front_data_tuple)
print(back_data_tuple)


Chapter02-20
리스트 내포 기능을 이용해 [5, 6, 77, 45, 22, 12, 24]에서 짝수를 제거한 후 리스트를
출력하는 프로그램을 작성하십시오.
[입력] 입력 없음
[출력] [5, 77, 45]

[풀이]
data_list = [5, 6, 77, 45, 22, 12, 24]

i = 0
while i < len(data_list):
    if data_list[i] % 2 == 0:
        del data_list[i]
    else:
        i += 1
print(data_list)


Chapter02-21
리스트 내포 기능을 이용해 [12, 24, 35, 70, 88, 120, 155]에서
홀수번째 항목을 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.
[입력] 입력 없음
[출력] [24, 70, 120]

[풀이]
data_list = [12, 24, 35, 70, 88, 120, 155]

i = 0
while i < len(data_list):
    del data_list[i]
    i += 1
print(data_list)


Chapter02-22
항목 값으로는 0을 갖는 2*3*4 형태의 3차원 배열을 생성하는
리스트 내포 기능을 이용한 프로그램을 작성하십시오.
[입력] 입력없음
[출력] [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

[풀이]
matrix = [[[0 for _ in range(4)] for _ in range(3)] for _ in range(2)]
print(matrix)


Chapter02-23
리스트 내포 기능을 이용해 [12, 24, 35, 70, 88, 120, 155]에서
첫번째, 다섯번째, 여섯번째 항목을 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력] 

[풀이]
data_list = [12, 24, 35, 70, 88, 120, 155]
del data_list[0]
del data_list[3]
del data_list[3]
print(data_list)


Chapter02-24
두 개의 리스트 [1,3,6,78,35,55]와 [12,24,35,24,88,120,155]를 이용해
양쪽 리스트에 모두 있는 항목을 리스트로 반환하는 프로그램을 작성하십시오.
[입력] 입력없음
[출력] [35]

[풀이]
data_list1 = [1,3,6,78,35,55]
data_list2 = [12,24,35,24,88,120,155]
common_list = [x for x in data_list1 if x in data_list2]
print(common_list)


Chapter02-25
리스트의 항목 중 중복이 되는 항목을 제거하는 함수를 정의하고 이 함수를 이용해
[12,24,35,24,88,120,155,88,120,155]에서 중복이 제거된 리스트를 출력하십시오.
[입력] 입력없음
[출력] [12, 24, 35, 88, 120, 155]

[풀이]
data_list = [12,24,35,24,88,120,155,88,120,155]
data_list = list(set(data_list))
print(sorted(data_list))
"""



words = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

word_list = [word for word in words if word != 'a' and word != 'e' and word != 'i' and word != 'o' and word != 'u']

print("".join(word_list))
