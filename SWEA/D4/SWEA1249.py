from collections import deque


def bfs(q):
    global visit
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] > visit[x][y] + supplyload[nx][ny]:
                    visit[nx][ny] = min(visit[nx][ny], visit[x][y] + supplyload[nx][ny])
                    q.append((nx, ny))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, int(input()) + 1):
    n = int(input())
    supplyload = [list(map(int, input())) for _ in range(n)]
    visit = [[100000] * n for _ in range(n)]
    visit[0][0] = 0
    start = (0, 0)
    q = deque()
    q.append(start)
    bfs(q)
    print('#{} {}'.format(t, visit[n - 1][n - 1]))