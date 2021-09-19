# -*- coding: utf-8 -*-
"""
Memoizaiton

Memoization의 의미
-> 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서
   매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
-> DP(동적계획법)의 핵심이 되는 기술

meomoization 단어의 의미
-> 글자 그대로 해석하면 '메모리에 넣기(to put in memory)라는 의미'
-> '기억되어야 할 것'이라는 뜻의 라틴어 Memorandum에서 파생
-> 흔히 '기억하기', '암기하기'라는 뜻의 Memorization과 혼동하지만,
   정확한 단어는 Memoization으로 동사형은 memoize임
   
Memoization 방법을 적용한 알고리즘
-> 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을
   계산하지마자 저장하면 실행 시간을 줄일 수 있음
-> 만약 기존에 계산하여 저장된 값이 있을 경우에는 다시 계산하지
   않겠다는 알고리즘

"""

# memo를 위한 리스트를 생성하고,
# memo[0]을 0으로 memo[1]는 1로 초기화 한다

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]

print(fibo1(4))