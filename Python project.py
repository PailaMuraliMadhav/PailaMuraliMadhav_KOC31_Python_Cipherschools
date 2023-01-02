# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:21:36 2023

@author: singam s3
"""


    
m=input("enter a WORD to convert: ")
Word = m.split()
acronym=""
for i in Word:
    acronym+=i[0].upper()
print("acronym : ",acronym)
for i in range(len(acronym)):
    print(acronym[i]," -",Word[i])