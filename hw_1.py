out1=[i for i in range(100) if i%2==1]
print(out1)
sum=1
for i in out1:
    if i<=50:
        sum*=i
    else:
        break
print(sum)