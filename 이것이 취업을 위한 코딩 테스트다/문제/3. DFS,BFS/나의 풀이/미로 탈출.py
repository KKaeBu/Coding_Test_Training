from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 목적지는 (0, 0) -> (n-1, m-1) 이기에
# 오른쪽과 아래쪽으로만 이동하면됨
dx = [0, 1]
dy = [1, 0]


# 범위 체크
def is_valid_coord(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(sx, sy):
    q = deque()
    q.append((sx, sy, 1))  # 1은 경로 값(depth)
    graph[sx][sy] = 0  # 방문 처리
    while q:
        x, y, d = q.popleft()
        if x == n - 1 and y == m - 1:
            print(d)
            return

        nd = d + 1
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            print(f"n: {nx}, {ny}")
            if is_valid_coord(nx, ny) and graph[nx][ny]:
                q.append((nx, ny, nd))
                graph[nx][ny] = 0  # 방문 처리


bfs(0, 0)
