#2022/10/08
str=input()
lens=len(str)
max=1
res=1
for i in range(1,lens):
    if str[i]==str[i-1]:
        res+=1
        if res>max:
            max=res
    else:
        res=1
if max>1:
    print("yes")
    print(max)
else:
    print('no')