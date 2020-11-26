for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    sol = 0
    score.sort(reverse=True)
    for i in range(k):
        sol += score[i]
    print('#{} {}'.format(t, sol))