N = int(input())  
arr = []  
for i in range(N):  
    x = int(input())  
    arr.append(x)  

s_arr = sorted(arr, reversed=True)  

for i in s_arr:  
    print(i, end=' ')