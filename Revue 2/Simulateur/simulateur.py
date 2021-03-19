# Script by Viktor

import random

r = random.randint(0, 22)
print(r)
print("choisir scènario voulue :")
print("1. 18°")
print("2. 16°")
print("3. 10°")
t_voulue = int(input())
if t_voulue == 1:
    t_voulue = 18
if t_voulue == 2:
    t_voulue = 16
if t_voulue == 3:
    t_voulue = 10
t_final = t_voulue-r
t_final = t_final+r
print(t_final)
