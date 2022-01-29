T=int(input())

for i in range(1,T+1):
    li=[]
    N=int(input())
    print("len",len(li))
    while len(li)==10:
        
        N2=N*num
        N2=list(map(int,str(N2)))
        li=+N2
        num=+1

#수도 요금 경쟁

t=int(input("테스트 케이스개수를 입력하시오: "))

for i in range(1,t+1):


	p,q,r,s,w=map(int,input().split())

	a=w*p
	if w<=r:
		b=q
	else:
		b=q+(w-r)*s
	c=[a,b]
	print("#",i, min(c))

#초심자의 회문 검사
t=int(input())
for i in range(1,t+1):
    w=input()
    li=list(w)
    li2=[None for _ in range(len(li))]
    for j in range(0,len(li)):
        
        if li[j]==li[len(li)-j-1]:
            li2[j]=0
        else: li2[j]=1
    if sum(li2)!=0:
        a=0
    else:
        a=1
    print('#',i,a)

#두 개의 숫자열

t=int(input())
for i in range(1,t+1):
    a,b=map(int,input().split())
    
    c=[]
    
    a1=list(map(int,input().split()))
    
    b1=list(map(int,input().split()))
    li=[]
    for l in range(0,abs(b-a)+1):
        
        li.append(a1[l]*b1[l])
    for m in range(0,l):
        
        if a<b:
            li.append(a1[l]*b1[l+m])
        else:
            li.append(b1[l]*a1[l+m])
        c.append(sum(li))
    print('#',i,max(c))
            
    



            