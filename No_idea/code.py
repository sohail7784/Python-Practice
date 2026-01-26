n,m=map(int,input().split()) # creating a variable called n,m n=interger and m=size of sets
array_size=list(map(int,input().split())) # its an array size
set_A=set(map(int,input().split())) # conatining A set mapped into int data type and slpited for both A and B sets
set_B=set(map(int,input().split()))

happiness=0 # happiness just a score

for i in array_size:
    if i in set_A:
        happiness+=1 # incresing number
    elif i in set_B:
        happiness-=1
print(happiness)