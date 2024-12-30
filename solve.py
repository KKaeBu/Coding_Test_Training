n = int(input())
store = list(map(int, input().split()))

m = int(input())
customer = list(map(int, input().split()))

#빠른 탐색을 위해 매장 배열을 정렬
store.sort()

# 손님이 찾는게 매장에 있는지 탐색 (이진 탐색 - 재귀)
def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

result = []

for i in customer:
    isin = binary_search(store, i, 0, n-1)
    result.append("yes") if isin else result.append("no")

for r in result:
    print(r, end=' ')

