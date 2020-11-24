tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    n_set = set(list(map(str, input().split())))
    m_set = set(list(map(str, input().split())))
    sol = len(n_set & m_set)
    print('#{} {}'.format(t, sol))