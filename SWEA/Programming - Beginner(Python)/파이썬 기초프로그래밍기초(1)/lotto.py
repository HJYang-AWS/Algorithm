# -*- coding: utf-8 -*-
"""
Created on Sat May 29 14:55:47 2021

@author: aze14
"""

import random
    
def input_count():
    count = 0
    try:
        count = int(input("구매하실 로또의 갯수를 적어주세요: "))
    except:
        count = 1
    finally:
        return count
    
def print_lotto(count):
    for i in range(count):
        lotto = random.sample(range(1, 45 + 1), 6)
        lotto_bonus = random.sample(range(1, 45 + 1), 1)
        while lotto_bonus in lotto:
            lotto_bonus = random.sample(range(1, 45 + 1), 1)
    
        print("행운의 로또 번호는 ", end="")
        for num in sorted(lotto):
            print("{0}".format(num), end=", ")
        print("{0}".format(lotto_bonus), end="")
        print("입니다.")
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            