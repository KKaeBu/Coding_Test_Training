n, m = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
  if min(num_list[i]) > result:
    result = min(num_list[i])

print(result)