import sys

sys.stdin = open("1952. 수영장_input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    # 하루, 1개월, 3개월, 1년
    day, month, three_month, year = map(int, input().split())
    # 월 별 운동 횟수
    plan_list = list(map(int, input().split()))

    # plan_list로 받아온 월 별 운동 횟수를 통해, 한달치 vs 하루씩 의 값을 계산하여 min 값으로 치환
    for i in range(len(plan_list)):
        if plan_list[i] * day > month:
            plan_list[i] = month
        else:
            plan_list[i] = plan_list[i] * day

    # 1월, 2월 누적 비용 계산
    dp = [plan_list[0], plan_list[0] + plan_list[1]]

    # 3월부터 계산 시작
    dp.append(min(sum(plan_list[:3]), three_month))
    for i in range(3, 12):
        dp.append(min(dp[i - 3] + three_month, dp[i - 1] + plan_list[i]))

    if dp[-1] > year:
        print("#{0} {1}".format(test_case, year))
    else:
        print("#{0} {1}".format(test_case, dp[-1]))
    # print(three_month)
    # print(plan_list)
    # print(dp)
    # print("#{0} {1}".format(test_case, dp[-1]))
    # print()
