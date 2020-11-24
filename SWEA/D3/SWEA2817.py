def subsum(idx, sum):
    global cnt
    if idx >= n:
        return
    sol = sum + total_set[idx]
    if sol == k:
        cnt += 1
    subsum(idx + 1, sum)
    subsum(idx + 1, sol)

tc = int(input())
for t in range(1, tc + 1):
    n, k = map(int, input().split())
    total_set = list(map(int, input().split()))
    cnt = 0
    subsum(0, 0)
    print('#{} {}'.format(t, cnt))