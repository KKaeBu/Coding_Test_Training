n, m = map(int, input().split())
a, b, d = map(int, input().split())
stage = [list(map(int, input().split())) for _ in range(n)]
# d: 0(북), 1(동), 2(남), 3(서)
# map: 0 = 육지, 1 = 바다, 2 = 방문칸

da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
count = 0  # 4면 바다 카운트
move = 1  # 이동한 칸의 개수

while True:
    stage[a][b] = 2  # 방문칸 표시
    # 바라보는 방향의 "왼쪽 방향" 길 여부 확인
    ld = 3 if d == 0 else d - 1
    if stage[a + da[ld]][b + db[ld]] == 0:
        # 육지임 -> 이동
        a += da[ld]
        b += db[ld]
        d = ld
        count = 0
        move += 1
    else:
        # 바다 or 방문한 칸임 -> 다시 회전
        d = ld
        count += 1

    if count == 4:
        # 4면이 막힌 경우
        # 뒤로 가기 여부 확인 (뒷칸이 2인지 확인)
        if stage[a - da[ld]][b - db[ld]] == 2:
            # 뒤로 가기
            a -= da[ld]
            b -= db[ld]
            count = 0
        else:
            # stop
            break

print(move)

# 확인용 맵 출력
for i in range(n):
    print(" ".join(list(map(str, stage[i]))))
