import sys

sys.stdin = open("input_퇴사.txt", "r")


def rec(day, cost):
    global answer

    if day > days:
        return

    if day == days:
        if answer < cost:
            answer = cost
        return

    rec(day + time_list[day], cost + pay_list[day])
    rec(day + 1, cost)


answer = 0
days = int(input())
time_list = [0] * days
pay_list = [0] * days

for i in range(days):
    time_list[i], pay_list[i] = map(int, input().split())

rec(0, 0)
print(answer)




























