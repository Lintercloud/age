# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:59:13 2020

@author: Linter
"""

driving = input("請問你有沒有開過車")
if driving !="有" or driving !="沒有":
    print("只能輸入  有\沒有")
    raise SystemExit
    
age = int("請問你的年齡:")

if driving == "有":
    if age >= 18:
        print("恭喜，祝你開車順利")
    else:
        print("你怎麼會有開車經驗")
elif driving == "沒有":
    if age >= 18:
        print("可以去考駕照了喔")
    else:
        print("很好，再等幾年就可以考了")
