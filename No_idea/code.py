n,m=map(int,input().split())
array_size=list(map(int,input().split()))
set_A=set(map(int,input().split()))
set_B=set(map(int,input().split()))

happiness=0

for i in array_size:
    if i in set_A:
        happiness+=1
    elif i in set_B:
        happiness-=1
print(happiness)