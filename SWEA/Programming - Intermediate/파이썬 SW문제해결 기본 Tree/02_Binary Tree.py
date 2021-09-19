"""
이진트리
1. 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
2. 노드가 자식 노드를 최대한 2개까지만 가질 수 있는 트리

특징
1. 레벨 i에서의 노드의 최대 개수는 2^i개
2. 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개,
   최대 개수는 (2^(h+1) - 1) 개가 됨

종류
1. 포화 이진 트리(Full binary Tree)
2. 완전 이진 트리(Complete binary Tree)
3. 편향 이진 트리(Skewed binary Tree)

1. 포화 이진 트리(Full Binary Tree)
-> 모든 레벨에 노드가 포화 상태로 차 있는 이진 트리
   1. 최대의 노드 개수인 (2^(h+1) - 1)의 노드를 가진 이진 트리
      ex) 높이가 3일 때: 2^(3+1) - 1 = 15개의 노드
   2. 루트를 1번으로 하여 2^(h+1 - 1) 까지 정해진 위치에 대한 노드 번호를 가짐

2. 완전 이진 트리(Complete binary Tree)
-> 높이가 h이고 노드 수가 n개일 때  (단, 2^h <= n < 2^(h+1) - 1),
   Full 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리

3. 편향 이진 트리 (Skewed binary Tree)
-> 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드 마을 가진 이진 트리
   왼쪽, 오른쪽 이진 편향 트리가 있음


순회(Traversal)
-> 트리의 각 노드를 중복되지 않게 전부 방문(Visit) 하는 것을 말하는데,
   트리는 비 선형 구조이기 때문에 선형 구조에서와 같이 선후 연결 관계를 알 수 없음
   
3가지의 기본적인 순회 방법
1. 선위 순회(Preorder traversal)
   -> VLR
   -> 자손 노드보다 루트 노드를 먼저 방문
   수행방법
   1) 현재 노드 n을 방문하여 처리: V
   2) 현재 노드 n의 왼쪽 서브트리로 이동: L
   3) 현재 노드 n의 오른쪽 서브트리로 이동: R
예시)
def preorder_traverse(T):  # 전위순회
    if T:  # T is not None
        visit(T)  # print(T.item)
        preorder_traverse(T.left)
        preorder_traverse(T.right)

2. 중위 순회(Inorder traversal)
   -> LVR
   -> 왼쪽 자손, 루트, 오른쪽 자손 순으로 방문
   수행방법
   1) 현재 노드 n의 왼쪽 서브트리로 이동 : L
   2) 현재 노드 n을 방문하여 처리 : V
   3) 현재 노드 n의 오른쪽 서브트리로 이동 : R
예시)
def inorder_traverse(T) :  # 중위순회
    if T :  # T is not None
        inorder_traverse(T.left)
        visit(T)  # print(T.item)
        inorder_traverse(T.right)

3. 후위 순회
   -> LRV
   -> 루트노드보다 자손을 먼저 방문
   수행방법
   1) 현재 노드 n의 왼쪽 서브트리로 이동 : L
   2) 현재 노드 n의 오른쪽 서브트리로 이동 : R
   3) 현재 노드 n을 방문하여 처리: V
예시)
def postorder_traverse(T):  # 후위순회
    if T:  # T is not None
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)  # print(T.item)
"""























