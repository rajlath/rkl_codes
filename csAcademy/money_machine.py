# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:22:05 2018
coded by : rinfo
"""

day, money, income, cost, bonus = [int(x) for x in input().split()]
for i in range(day):
    if (day - i) * bonus > cost and money >= cost:
        money -= cost
        income += bonus
    money += income
print(money)    
        
        
    
            
            
    