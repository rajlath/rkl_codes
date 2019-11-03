# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
cost = 0.0
for _ in range(2):
    _, qty, prc = [x for x in input().split()]
    qty = int(qty)
    prc = float(prc)
    cost += qty * prc
print("VALOR A PAGAR: R$ {:.2f}".format(cost))