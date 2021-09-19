import sys

sys.stdin = open("5185. 이진수_input.txt", "r")


def number_to_binary(number: int):
    binary = ""
    for i in range(4):
        if 8 >> i & number:
            binary += '1'
        else:
            binary += '0'

    return binary


def alpha_to_binary(alpha: str):
    alpha_dict = {'A': '1010',
                  'B': '1011',
                  'C': '1100',
                  'D': '1101',
                  'E': '1110',
                  'F': '1111'
                  }

    return alpha_dict[alpha]


T = int(input())

for test_case in range(1, T + 1):
    num, hexa = map(str, input().split())
    result = ""

    for element in hexa:
        if str.isdigit(element):
            result += number_to_binary(int(element))
        elif str.isalpha(element):
            result += alpha_to_binary(element)

    print("#{} {}".format(test_case, result))


