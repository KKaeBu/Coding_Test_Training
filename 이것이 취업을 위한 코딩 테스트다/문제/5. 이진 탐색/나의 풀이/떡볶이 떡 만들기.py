import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dduck = list(map(int, sys.stdin.readline().rstrip().split()))

# 떡 내림차순 정렬
dduck.sort(reverse=True)

# 가장 긴 떡에서 1만큼 뺀 길이부터 시작
h = dduck[0] - 1


# 원소 하나씩 보며 주어진 높이를 뺀 나머지 값의 합을 구해서 비교
def cutting_dduck(d_arr, c_h):
    sum = 0
    i = 0
    while sum < m:
        if d_arr[i] > c_h:
            sum = sum + (d_arr[i] - c_h)
            i += 1
        else:
            sum = 0
            i = 0
            c_h -= 1
            continue

    return c_h


result = cutting_dduck(dduck, h)
print(result)
