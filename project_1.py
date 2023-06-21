#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:41:59 2023

@author: michael Gaitho
"""
import random

name1 = input('Enter first name:')
name1RandomNumber = random.randint(0, 10)

name2 = input('Enter second name:')
name2RandomNUmber = random.randint(0, 10)

name3 = input('Enter third name:')
name3RandomNumber = random.randint(0, 10)

print(name1, "you got the number:", name1RandomNumber)
print(name2, "you got the number:", name2RandomNUmber)
print(name3, "you got the number:", name3RandomNumber)