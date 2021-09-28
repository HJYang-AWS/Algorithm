import sys

sys.stdin = open("input_test.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    # 하루, 1개월, 3개월, 1년
    day, month, three_month, year = map(int, input().split())
    # 월 별 운동 횟수
    plan_list = list(map(int, input().split()))

    answer = 0
    cost = 0
    idx = 0

    while idx < 12:
        # 현재를 기준으로 하루 & 1개월 조합으로 3개월 치의 최소값(cost) 구하기
        cost = 0
        for i in range(3):
            # 12월을 넘을 경우, 반복문 탈출
            if idx + i > 11:
                break
            else:
                if plan_list[idx + i] * day >= month:
                    cost += month
                else:
                    cost += plan_list[idx + i] * day

        # 하루 & 1개월 조합으로 3개월 치의 최소값(cost) vs 3개월 치 통으로 끊는 가격을 비교
        # 만약 3개월 치 통으로 끊는게 더 쌀 경우 idx를 +3해서 넘김
        if cost > three_month:
            idx += 3
            answer += three_month
        else:
            if plan_list[idx] * day >= month:
                answer += month
            else:
                answer += plan_list[idx] * day
            idx += 1

    if answer <= year:
        print("#{0} {1}".format(test_case, answer))
    else:
        print("#{0} {1}".format(test_case, year))