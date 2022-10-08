#2022/10/08
import math
import random
s=1*4
n=100000
c=0
for i in range(n):
    x=random.uniform(0,1)
    y=random.uniform(0,4)
    if y<x*x*x+x*x:
        c+=1
sum=c/n*s
print(sum)