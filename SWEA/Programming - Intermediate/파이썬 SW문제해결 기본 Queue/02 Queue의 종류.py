"""
선형 큐의 특징
1. 1차원 리스트를 이용한 큐
-> 큐의 크기 = 리스트의 크기
-> front: 저장된 첫 번째 원소의 인덱스
-> rear: 저장된 마지막 원소의 인덱스

2. 상태표현
-> 초기상태: front = rear = -1
-> 공백상태: front = rear
-> 포화상태: rear = n - 1 (n:리스트의 크기, n-1: 리스트의 마지막 인덱스)


선형 큐의 구현
1. 초기 createQueue()
초기 공백 큐 생성
-> 크기 n인 1차원 리스트 생성
-> front, rear = -1로 초기화

2. enQueue(item)
삽입: enQueue(item)
마지막 원소 뒤에 새로운 원소를 삽입하기 위해
1) rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련함
2) 그 인덱스에 해당하는 리스트원소 Q[rear]에 item을 저장
ex)


3. deQueue
삭제: deQueue()
가장 앞에 있는 원소를 삭제하기 위해
1) front 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동함
2) 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능을 함
ex)

4. isEmpty(), isFull()
공백상태 및 포화상태 검사: isEmpty(). isFull()
-> 공백 상태: front = rear
-> 포화상태: rear = n - 1
   (n: 리스트의 크기, n-1: 리스트의 마지막 인덱스)

5. Qpeek()
검색: Qpeek()
-> 가장 앞에 있는 원소를 검색하여 반환하는 연산
-> 현재 front의 한자리 뒤(front+1)에 있는 원소,
   즉 큐의 첫 번째에 있는 원소를 반환

ex)
def Qpeek():
    if isEmpty(): print("Queue_empty")
    else: return Q[front+1]

def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q) - 1

def enQueue(item):
    global rear
    if isFull(): print("Queue_Full")
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty(): print("Queue_Empty")
    else:
        front += 1
        return Q[front]


선형 큐의 문제점: 잘못된 포화 상태 인식!
리스트의 크기를 고정 -> 사용할 큐의 크기만큼을 미리 확보 -> 메모리의 낭비 발생
1) 삽입, 삭제를 계속할 경우 리스트의 앞부분에 활용할 수 있는 공간이 있음에도,
   rear = n - 1인 상태 즉, 포화 상태로 인식
2) 더 이상의 삽입을 수행할 수 없음

선형 큐의 장점: 삽입, 삭제의 처리속도 빠름
선형 큐의 단점: 메모리 낭비가 심함

선형 큐의 해결방법
* 원형 큐 사용으로 메모리 절약
* 파이썬의 리스트 특성을 사용한 큐 사용으로 메모리 절약
- 단점: 삽입, 삭제 시 복사, 데이터 이동시키는 연산 수행에 많은 시간 소모
* 단순연결 리스트로 구현한 큐 사용으로 메모리 동적 확보
* 큐 라이브러리 사용


원형 큐
-> 1차원 리스트를 사용하되, 논리적으로 리스트의 처음과 끝이 연결되어
   원형 형태의 큐를 이룬다고 가정하고 사용함
-> 원형 큐의 논리적 구조

원형 큐의 특징
1. 초기 공빅 상태
-> front = rear = 0

2. Index의 순환
-> front와 rear의 위치가 리스트의 마지막 인덱스인 n-1를 가리킨 후,
   논리적 순환을 이루어 리스트의 처음 인덱스인 0으로 이동해야 함
-> 이를 위해 나머지 연산자 %를 사용

3. front 변수
-> 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 남겨둠

4. 삽입 위치 및 삭제 위치
삽입 위치: rear = (rear + 1) % n
삭제 위치: front = (front + 1) % n


원형 큐의 구현
1. 초기 createQueue()
초기 공백 큐 생성
-> 크기 n인 1차원 리스트 생성
-> front, rear = 0으로 초기화

2. isEmpty(), isFull()
공백 상태 및 포화상태 검사: isEmpty(), isFull()
-> 공백 상태 및 포화 상태 검사: isEmpty(), isFull()
-> 공백 상태: front = rear
-> 포화상태: 삽입할 rear의 다음 위치 = 현재 front
-> (rear + 1) % n = front

3. enQueue(item)
삽입: enQueue(item)
마지막 원소 뒤에 새로운 원소를 삽입하기 위해
1) rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련함: rear <- (rear + 1) % n
2) 인덱스에 해당하는 리스트원소 cQ[rear]에 item을 저장

4. deQueue
삭제: deQueue(), delete()
가장 앞에 있는 원소를 삭제하기 위해
1) front 값을 조정하여 삭제할 자리를 준비함
2) 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능을 함

ex)
def isEmpty():
    return front == rear

def isFull():
    return (rear + 1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]

def delete():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front + 1) % len(cQ)

cQ_size = 3
cQ = [0] * cQ_size

# front, rear를 0으로 초기화
front = rear = 0

enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())



리스트의 특성을 사용한 Queue
1. 파이썬의 리스트 특성을 사용한 큐
-> 리스트는 크기를 동적으로 변경할 수 있음
-> 메모리 절약
-> 삽입, 삭제 시 복사, 데이터를 이동시키는 연산을 수행하는데 많은 시간 소모

2. 리스트의 메서드
append(item): 마지막에 원소 추가, pop(index): index 위치에 원소 삭제

3. front는 리스트의 맨 앞: -1

4. rear는 리스트의 맨 뒤: len(queue) - 1


파이썬으로 구현한 원형 큐의 삽입 및 삭제 함수
def enQueue(item):
    queue.append(item)

def deQueue():
    if isEmpty():
        print("Queue_Empty")
    else:
        return queue.pop(0)

def isEmpty():
    return len(queue) == 0

def Qpeek():
    if isEmpty():
        print("Queue_Empty")
    else:
        return queue[0]

queue = []
enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())


연귤 큐의 특징
1. 단순 연결 리스트(Linked List)를 이용한 큐
-> 큐의 원소: 단순 연결 리스트의 노드
-> 큐의 원소 순서: 노드의 연결 순서, 링크로 연결되어 있음
-> front: 첫 번째 노드를 가리키는 링크
-> rear: 마지막 노드를 가리키는 링크

2. 상태 표현
-> 초기 상태: front = rear = None
-> 공백 상태: front = rear = None


연결 큐의 연산 과정
1) 큐 생성: createLinkedQueue()
* front = rear = None

2) 원소 A 삽입: enQueue(A)
* front = rear = A가 저장된 주소값
3) 원소 B 삽입: enQueue(B)
* front = A가 저장된 주소값, rear = B가 저장된 주소값
4) 원소 삭제: deQueue()
* front = B가 저장된 주소값, rear = B가 저장된 주소값
5) 원소 C 삽입: enQueue(C)
* front = B가 저장된 주소값, rear = C가 저장된 주소값
6) 원소 삭제: deQueue()
* front = C가 저장된 주소값, rear = C가 저장된 주소값
7) 원소 삭제: deQueue()
* front = rear = None


연결 큐의 구현
1. 초기 공백 큐 생성: createLinkedQueue()
-> 리스트 노드 없이 포인터 변수만 생성함
-> front와 rear를 None로 초기화

2. isEmpty()
공백상태 검사: isEmpty()
-> 공백상태: front = rear = None

3. enQueue(item)
삽입: enQueue(item)
1) 새로운 노드 생성 후 데이터 필드에 item 저장
2) 연결 큐가 공백인 경우, 아닌 경우에 따라 front, rear 변수 지정

4. deQueue()
삭제: deQueue()
1) old가 지울 노드를 가리키게 하고, front 재설정
2) 삭제 후 공백 큐가 되는 겨웅, rear도 None로 설정
3) old가 가리키는 노드를 삭제하고 메모리 반환

ex)
def isEmpty():
    return front == None

def enQueue(item):
    global front, rear
    newNode = node(item)
    if isEmpty():
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def deQueue():
    global front, rear
    if isEmpty():
        print("Queue_Empty")
        return None
    item = front.item
    front = front.next
    if isEmpty():
        rear = None
    return item


큐 모듈
1. 큐 모듈에 정의된 클래스
queue.Queue(maxsize): 선입선출(FIFO) 큐 객체를 생성
queue.Lifo(maxsize): 스택(Stack)개념의 후입선출(LIFO) 큐 객체 생성
queue.PriorityQueue(maxsize)
: 우선순위 큐 객체를 생성, 입력되는 아이템의 형식은 (순위, 아이템)의 튜플로 입력되며,
  우선순위는 숫자가 작을수록 높은 순위를 가짐짐

2. maxsize는 최대 아이템 수, 지정하지 않거나 음수이면 내용만큼 늘어남

3. 제시된 3개의 클래스는 다음과 같은 메서드를 동일하게 가짐
qsize(): 큐 객체에 입력된 아이템의 개수를 반환
put(item[, block[, timeout]]): 큐 객체에 아이템을 입력
get([block[, timeout]]): 생성된 큐 객체 특성에 맞추어, 아이템 1개를 반환
empty(): 큐 객체가 비어있으면 True 리턴
full(): 큐 객체가 꽉차있으면 True 리턴


예시) 선입선출의 큐 개념을 구현한 큐 클래스 활용
import queue
q = queue.Queue() # FIFO 구조 큐 생성
q.put('A')
q.put('B')
q.put('C')

while not q.empty():
    print(q.get())

* put 메서드 입력 시, 큐가 꽉 차 있을 경우, full exception이 발생함
* get 메서드 삭제 시, 큐가 비어 있을 경우, empty exception이 발생함



"""








