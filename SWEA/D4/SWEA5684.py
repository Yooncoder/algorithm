from collections import deque

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    data = [[0] * n for _ in range(n)]
    for i in range(m):
        s, e, c = map(int, input().split())
        data[s - 1][e - 1] = c
    min_sol = float('inf')
    for i in range(n):
        visit = [0] * n
        q = deque()
        q.append([i, 0])
        while q:
            point = q.popleft()
            for j in range(n):
                if data[point[0]][j] != 0 and visit[j] == 0:
                    visit[j] = 1
                    q.append([j, point[1] + data[point[0]][j]])
                if data[point[0]][j] != 0 and j == i:
                    min_sol = min(min_sol, point[1] + data[point[0]][j])
    if min_sol == float('inf'):
        print('#{} {}'.format(t, -1))
    else:
        print('#{} {}'.format(t, min_sol))