print("hello")
"""
Queue 자료 구조의 개념
1. 삽입, 삭제의 위치가 제한적인 자료구조
-> 큐 뒤: 삽입 / 큐 앞: 삭제

2. 선입선출구조(FIFO:First In First Out)
-> 큐에 삽입한 순서대로 원소가 저장
-> 가장 먼저 삽입(First In)된 원소는 가장 먼저 삭제(First Out)됨

3. 큐의 예: 서비스 대기 행렬


큐의 선입선출 구조
머리(Front): 큐의 맨 앞
꼬리(Rear): 큐의 맨 뒤
기본연산: 삽입(enQueue), 삭제(DeQueue)


큐의 주요 연산
enQueue(item): 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산
deQueue(): 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산
createQueue(): 공백 상태의 큐를 생성하는 연산
isEmpty(): 큐가 공백상태인지를 확인하는 연산
ifFull(): 큐가 포화상태인지를 확인하는 연산
Qpeek(): 큐의 앞 쪽(front)에서 원소를 삭제 없이 반환하는 연산


큐의 기본 연산 과정
1. 공백 큐 생성: createQueue(); front = rear = -1
2. 원소 A 삽입: enQueue(A); front = -1, rear = [0]번(A)
3. 원소 B 삽입: enQueue(B) ; front = -1, rear = [1]번(B)
4. 원소 반환/삭제: deQueue(); front = [0]번, A반환, rear = [1]번 B
5. 원소 C 삽업: enQueue(C); front = [0]번, rear = [2]번 C
6. 원소 반환/삭제: deQueue(); front = [1]번 B반환, rear = [2]번 C
7. 원소 반환/삭제: deQueue(); front = [2]번 C반환, rear = [2]번, 
   front와 rear가 같으므로 Queue가 비어있다고 판단, 1번으로 초기화
   

Queue 자료 구조의 개념: Queue의 종류
1. 선형 큐
-> 간단하고 기본적인 형태
-> 리스트 사용

2. 원형 큐
-> 선형에서 발전된 형태
-> 리스트 사용

3. 연결 큐
-> 연결 리스트 형식을 이용

4. 우선순위 큐
 

"""
