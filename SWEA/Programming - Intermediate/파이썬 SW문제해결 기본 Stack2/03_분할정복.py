# -*- coding: utf-8 -*-
"""
분할 정복
: 분할 + 정복 + 통합

분할(Divide)
: 해결할 문제를 여러 개의 작은 부분으로 나눔

정복(Conquer)
: 나눈 작은 문제를 각각 해결

통합(Combine)
: (필요하다면) 해결된 해답을 모음


거듭 제곱(Exponentiation) 알고리즘: O(n)
def Power(Base, Exponent):
    if Base == 0: return 1
    result = 1 # Base^0은 1이므로
    for i in range(Exponent):
        result *= Base
    return result

분할 정복 기반의 알고리즘: O(log(2n))
def Power(Base, Exponent):
    if Exponent == 0 or Base == 0:
        return 1
    if Exponent % 2 == 0:
        NewBase = Power(Base, Exponent/2)
        return NewBase * NewBase
    else:
        NewBase = Power(Base, (Exponent-1)/2)
        return (NewBase * NewBase) * Base


퀵 정렬과 합병 정렬의 비교
공통점: 주어진 리스트를 두 개로 분할하고, 각각을 정렬함
차이점
1)
합병 정렬: 분할할 때, 단순하게 두 부분으로 나눔
퀵 정렬: 기준 아이템(Pivot Item)을 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴
2)
합병 정렬: 각 부분 정렬이 끝난 후, '합병'이란 후처리 작업이 필요함
퀵 정렬: 각 부분 정렬이 끝난 후, 후처리 작업이 필요하지 않음


퀵 정렬 알고리즘
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, P+1, end)
        

주어진 리스트에서 피봇을 구하는 알고리즘
def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R): L += 1
        while(a[R] >= a[pivot] and L < R): R -= 1
        if L < R:
            if L == pivot : pivot = R
            a[L], a[R], = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R


퀵 정렬의 최악의 시간 복잡도는 O(n^2)
-> 합병정렬에 비해 좋지 못함
퀵 정렬의 평균 복잡도는 nlogn이기 때문임
"""


def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R): L += 1
        while(a[R] >= a[pivot] and L < R): R -= 1
        if L < R:
            if L == pivot : pivot = R
            a[L], a[R], = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R


a = [37, 28, 74, 37, 13, 1, 56]





















