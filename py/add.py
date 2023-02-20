def pprint(lsc,c):
    flag=0
    for i in range(c-1,-1,-1):
        if lsc[i]!=0 and flag==0:
            flag=1
        if flag==1:
            print(lsc[i],end="")
    if flag==0:
        print("0",end="")
    print()

lsaa=[9]*100
lsa=[]
lsa=[0]*(100-len(lsaa))
lsa=lsaa+lsa

lsbb=[8]+[9]*99
lsb=[]
lsb=[0]*(100-len(lsbb))
lsb=lsbb+lsb

print("a  =",end="")
pprint(lsa,100)
print("b  =",end="")
pprint(lsb,100)

lsc=[0]*101                 #加法
of=0
for i in range(100):
    lsc[i]=lsa[i]+lsb[i]+of
    of=lsc[i]//10
    lsc[i]=lsc[i]%10
lsc[100]=of
print("a+b=",end="")
pprint(lsc,101)

lsd=[0]*100                 #减法
of=0
for i in range(100):
    lsd[i]=lsa[i]-lsb[i]-of
    if lsd[i]>=0:
        of=0
    if lsd[i]<0:
        of=1
        lsd[i]=lsd[i]+10
print("a-b=",end="")
pprint(lsd,100)

lse=[0]*201               #乘法
of=0
for j in range(100):
    for i in range(100):
        lse[i+j]=lse[i+j]+lsa[i]*lsb[j]
for k in range(200):
    of=lse[k]//10
    lse[k]=lse[k]%10
    lse[k+1]=lse[k+1]+of
print("a*b=",end="")
pprint(lse,201)