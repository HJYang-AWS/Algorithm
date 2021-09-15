import sys
sys.stdin = open("1860. 진기의 최고급 붕어빵_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    guest_number, making_time, making_count = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_time_set = set(arrive_time)
    arrive_time_dict = {}

    for ele in arrive_time_set:
        arrive_time_dict.update({ele: arrive_time.count(ele)})

    fish_bread = 0
    time = 0
    result = "Possible"

    while max(arrive_time_dict.keys()) >= time:
        if time != 0 and time % making_time == 0:
            fish_bread += making_count

        if time in arrive_time_dict.keys():
            fish_bread -= arrive_time_dict[time]

            if fish_bread < 0:
                result = "Impossible"
                break

        time += 1



    print("#{} {}".format(test_case, result))