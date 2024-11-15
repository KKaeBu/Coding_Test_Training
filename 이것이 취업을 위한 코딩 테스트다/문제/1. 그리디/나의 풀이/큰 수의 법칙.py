n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
count = 0

arr.sort(reverse=True)
print(arr)

for _ in range(m):
    if arr[0] == arr[1]:
        sum = arr[0] * m
        break

    if count == k:
        sum += arr[1]
        count = 0
    else:
        sum += arr[0]
        count += 1


print(sum)
