from itertools import combinations


T = int(input())


for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    result = 0

    for i in range(1, n + 1):
        # num_list 의 부분집합 중 갯수가 i인 것 구하기
        # i=1이면 sub_set = [('1'), ('2'), ('1'), ('2')]
        subset = list(combinations(num_list, i))

        for j in range(len(subset)):
            # subset의 원소의 합 구해서 k랑 비교
            if k == sum(subset[j]):
                result += 1

    print("#{0} {1}".format(test_case, result))



