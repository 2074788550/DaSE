#2022/10/08
l=[1,2,3,4,5]
lens=len(l)
#for
for i in range(lens-1,-1,-1):
    print(l[i])
#while
t=lens-1
while t>-1:
    print(l[t])
    t=t-1
#
print(l[lens-1::-1])