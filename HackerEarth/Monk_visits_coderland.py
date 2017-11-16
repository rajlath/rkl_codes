#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
##  Monk_visits_coderland.py
#  
#  Copyright 2017 raj.lath <raj.lath@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#Author     :raj.lath
#Email      :raj.lath@gmail.com
#Created on :25.09.2017 14:30:18 IST

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import sys

# if python 2+
if sys.version_info.major == 2:
    MAXINT =  sys.maxint
    MININT = -sys.maxint - 1

    filter = itertools.ifilter
    map    = itertools.imap
    range  = xrange
    zip    = itertools.izip
    
# if python 3+
else:
    MAXINT =  sys.maxsize
    MININT = -sys.maxsize - 1
    
#single integer from input    
def sifc():return int(input()) 

#single string  from input                                   
def ssfc():return input()  

#array of integer from console default is space delimited                                       
def mifc(dl=" "): return [int(x) for x in input().split(dl)] 

#array of string  from console default is space delimited  
def msfc(dl=" "): return [x for x in input().split(dl)] 


for _ in range(sifc()):
    checkpoints = sifc()
    least_cost  = MAXINT
    petrol_cost = mifc()
    needed      = mifc()
    cost = 0
    for i in range(checkpoints):        
        least_cost  = min(least_cost, petrol_cost[i])
        print(cost)
        cost += least_cost * needed[i]
    print(cost)    
        
        





