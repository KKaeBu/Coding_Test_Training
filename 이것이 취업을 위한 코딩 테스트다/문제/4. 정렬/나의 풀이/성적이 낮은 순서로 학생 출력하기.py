N = int(input())  

stu = []  

for i in range(N):  
    stu_info = input().split()  
    stu.append((stu_info[0], int(stu_info[1])))  

s_stu = sorted(stu, key=lambda s: s[1])  

for s in s_stu:  
    print(s[0], end=' ')