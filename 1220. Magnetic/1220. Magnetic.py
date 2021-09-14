import sys
sys.stdin = open("1220. Magnetic_input.txt", "r")


T = 10

for test_case in range(1, T + 1):
    table_size = int(input())
    table = []
    cross = 0

    # 테이블에 대한 정보 받기
    for i in range(table_size):
        table.append(list(map(int, input().split())))

    # 테이블 전체를 작업 돌리기
    for i in range(table_size):
        queue = []
        # 테이블의 한 열을 스택에 넣기
        for j in range(table_size):
            if table[j][i] != 0:
                queue.append(table[j][i])

        # queue의 head앞엔 N극(1), tail뒤엔 S극(2)가 있다.
        # N, Head, ..., Tail, S
        # head의 값이 S(2)라면 N(1)이 나올 때까지 계속해서 빼낸다.
        # tail의 값이 N(1)라면 S(2)가 나올 때까지 계속해서 빼낸다.
        while queue[0] == 2 or queue[-1] == 1:
            if queue[0] == 2:
                queue.pop(0)
            if queue[-1] == 1:
                queue.pop(-1)

        # 교차 상태의 갯수를 확인
        for idx in range(len(queue) - 1):
            if queue[idx] == 1 and queue[idx + 1] == 2:
                cross += 1

    # 전체 cross 개수 출력
    print("#{0} {1}".format(test_case, cross))
