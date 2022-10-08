#2022/10/08
str=input()
list_str=list(str)
lens=len(list_str)
i=0
while i<lens:
    if(list_str[i]==' '):
        del list_str[i]
        lens=lens-1
    else:
        i+=1
print("".join(list_str))