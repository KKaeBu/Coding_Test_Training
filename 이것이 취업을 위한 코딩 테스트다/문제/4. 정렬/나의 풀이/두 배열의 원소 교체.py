n, k = map(int, input().split())  
arr_a = list(map(int, input().split()))  
arr_b = list(map(int, input().split()))  

# a배열 오름차순 정렬  
arr_a.sort()  
# b배열 내림차순 정렬  
arr_b.sort(reverse=True)  

# a의 최소 원소와 b의 최대 원소를 k번 swapfor i in range(k):  
    arr_a[i], arr_b[i] = arr_b[i], arr_a[i]  

# a배열의 합 출력  
print(sum(arr_a))