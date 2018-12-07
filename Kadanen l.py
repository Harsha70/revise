a=int(input())/*test case*/
for i in range(a):
    p=int(input())*/size of array/*
    l=list(map(int,input().strip().split(' ')))/*0 -1 -5 1 5*/
    maxsum=l[0]
    temp=l[0]
    for j in range(1,len(l)):
        temp=max(l[j],temp+l[j])
        if maxsum<temp:
            maxsum=temp
    print(maxsum)/*6*/
