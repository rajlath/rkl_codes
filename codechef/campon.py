# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 07:04:13 2018

@author: rinfo
"""

nb_test = int(input())
for _ in range(nb_test):
    ans = "Go Camp"
    days = [0] * 31
    nb_days =  int(input())
    for _ in range(nb_days):
        day, todo = [int(x) for x in input().split()]
        for i in range(day-1, 31):
            days[i] += todo
    nb_qry = int(input())
    for _ in range(nb_qry):
        day, shouldo = [int(x) for x in input().split()]
        if days[day-1] < shouldo:
            print("Go Sleep" )
        else:
            print("Go Camp")
             
            ṇ