#!/usr/bin/env python
# -*- coding: utf-8 -*-# 
# 24.08.2018 19:55:16 
# oorja
# copyright 2018   oh!   oorja.halt@gmail.com
from math import gcd
from datetime import datetime 


def gce(a,b):
	return [gcd(b,a%b),a][b==True]
s = datetime.now()	
print(gcd(103468212,22))
print(datetime.now() - s)
s = datetime.now()
print(gce(103468212,22))
print(datetime.now() - s)	
    
    
    
    


    
