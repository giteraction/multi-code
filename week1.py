홀수만 더하기 

n=int(input())
ll=[]
lll=[]
for i in range(1,n+1):
    l=list(map(int,input().split()))
    for j in l:
        if j%2==1:
            
            ll.append(j)
            lll.append(sum(ll))
            
for i in range(0,n+1):
    print('#',i+1, lll[i])

연월일 달력

n=int(input())

for i in range(1,n+1):
    day=list(int,input())
    s="".join(day)
    if ((day[5]==2 and day[6]>=3)or(day[4]>=2)or(day[6]>=4)):
        print(-1)
    else:
        print(s)

평균값 구하기

n=int(input())

list1=[]    
for i in range(1,n+1):
    data=list(map(int,input().split()))
    avg=sum(data)/len(data)
    list1.append(avg)
for i in range(0,n+1):
    print(list1[i])

간단한 소인수분해

n=int(input())

li=[2,3,5,7,11]
num=[]
for i in range(1,n+1):
    data=int(input())
    for j in range(0,len(li)):
        while data%li[j]!=0:
            num[j]=num[j]+1

print('#',i,num)

지그재그 숫자

n= int(input())
data=int(input())
li=list(range(1,data+1))
for i in range(1,n+1):
    
    
    for j in range(1,data+1):
        if j%2==0:
            li[j-1]=-j
        else:
            li[j-1]=j
    print('#',i,sum(li))
	
		 