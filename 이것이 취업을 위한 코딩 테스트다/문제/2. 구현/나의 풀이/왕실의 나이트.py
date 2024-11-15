m = input()
r, c = int(m[1]), ord(m[0]) - ord("a") + 1

# 나이트의 수평, 수직 이동
dr = [0, 0, -2, 2]
dc = [-2, 2, 0, 0]

s = [-1, 1]

count = 0

# 이동 최소 이동 수와 최대 이동 수는 2, 8
# 수평 검사 후 수직 검사
for i in range(4):
    tr, tc = r + dr[i], c + dc[i]
    if 1 <= tc <= 8 and 1 <= tr <= 8:
        # 이동 가능
        # 수평 이동인지 수직 인동인지 구분
        if i < 2:
            # 수평 이동
            for j in range(2):
                if 1 <= tr + s[j] <= 8:
                    count += 1
        else:
            # 수직 이동
            for j in range(2):
                if 1 <= tc + s[j] <= 8:
                    count += 1

print(count)
