from queue import PriorityQueue

def edge():
    for i in range(n):
        for j in range(i + 1, n):
            d = ((x_list[i] - x_list[j]) ** 2 + (y_list[i] - y_list[j]) ** 2) ** 0.5
            q_distance.put((d, i, j))

def find_root(x):
    if roots[x] != x:
        roots[x] = find_root(roots[x])
    return roots[x]

def check(a, b):
    x = find_root(a)
    y = find_root(b)
    return x != y

def union_root(a, b):
    x = find_root(a)
    y = find_root(b)
    if x > y:
        roots[x] = y
    else:
        roots[y] = x

for t in range(1, int(input()) + 1):
    n = int(input())
    sol = 0
    cnt = 0
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    q_distance = PriorityQueue()
    ratio = float(input())
    roots = [i for i in range(n)]
    edge()

    while q_distance and cnt != n - 1:
        d, a, b = q_distance.get()
        if check(a, b):
            sol += (d ** 2) * ratio
            cnt += 1
            union_root(a, b)
    sol = round(sol)
    print('#{} {}'.format(t, sol))