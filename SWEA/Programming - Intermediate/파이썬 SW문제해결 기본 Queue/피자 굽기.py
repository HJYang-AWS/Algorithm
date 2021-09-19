"""
N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.
1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.
주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오

- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다.
  이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

[입력]
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

[출력]
#1 4
#2 8
#3 6
"""
"""
1:4번 1:3번          
"""
from queue import Queue

T = int(input())

for test_case in range(1, T + 1):
    brazier_size, piz_num = map(int, input().split())

    # pizza_list에 [cheeze, 번호] 저장
    pizza_list = [[chz, idx+1] for idx, chz in enumerate(map(int, input().split()))]

    # 화덕 사이즈 만큼 피자 리스트 넣기
    brazier = Queue(maxsize=brazier_size)
    for i in range(brazier_size):  # 화덕 사이즈 만큼의 피자를 queue에 넣는다
        brazier.put(pizza_list.pop(i))

    while not brazier.empty():
        # 한 바퀴가 돈 피자의 치즈를 녹인다.
        pizza = brazier.get()
        pizza[0] //= 2

        if pizza[0] != 0:  # 치즈가 다 녹지 않으면 화덕에 다시 넣기
            brazier.put(pizza)
        else:  # 치즈가 다 녹았을 경우
            if len(pizza_list) != 0:  # pizza_list에 남아있는 피자가 있을 경우
                brazier.put(pizza_list.pop(0))  # pizza_list에서 하나 꺼내와 brazier에 넣기

    print("#{0} {1}".format(test_case, pizza[1]))





