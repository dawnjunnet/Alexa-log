#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:12:46 2020

@author: dawnstaana
"""

alexa = open('alexalog.txt','r')
filetext = alexa.read()

import re
duration_reg = re.compile('Billed Duration: \d+')
total = 0

for num in duration_reg.findall(filetext):
    ind = num.index(': ')
    total += int(num[ind+1:])

print('Total Billed Duration (in milliseconds): ', total)

user_reg = re.compile('ask\.account\.\w+')
user_total = 0
user_distinct = []

for char in user_reg.findall(filetext):
    ind = char.index('t.')
    char = char[ind+2:]
    if char in user_distinct:
        pass
    
    else:
        user_distinct.append(char)
        user_total += 1

print(f"\nThere are {user_total} userId's. They are:") 
for char in user_distinct:
    print(char)

