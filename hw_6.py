#2022/10/08

#1
c=2
g=0
for i in range(0,c+1):
    if(i*i>c and g==0):
        g=i-1
while(abs(g*g-c)>0.0001):
    g+=0.00001
print(g)

#2
c=2
min=0
max=c
g=(max+min)/2
while(abs(g*g-c)>0.0001):
    if(g*g<c):
        min=g
    else:
        max=g
    g=(min+max)/2
print(g)

#3
c=2
g=c/2
while(abs(g*g-c)>0.0001):
    g=(g+c/g)/2
print(g)