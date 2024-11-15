def dfs(graph, x, y):
    # 범위 체크
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 방문 체크
    if graph[x][y] == 0:
        # 방문하지 않았다면
        graph[x][y] = 1  # 방문 처리
        # 상하좌우 탐색(재귀식)
        dfs(graph, x - 1, y)  # 상
        dfs(graph, x, y - 1)  # 좌
        dfs(graph, x + 1, y)  # 하
        dfs(graph, x, y + 1)  # 우
        return True

    # 방문 했다면
    return False


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j) == True:
            result += 1

print(result)
