grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
tc = int(input())
for t in range(1, tc + 1):
    n, k = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(n)]
    sums = []
    cnt = 0
    score = 0
    for i in range(n):
        score = (scores[i][0] * 0.35) + (scores[i][1] * 0.45) + (scores[i][2] * 0.2)
        sums.append(score)
        score = 0
    for i in range(n):
        if sums[k - 1] < sums[i]:
            cnt += 1
    ratio = (cnt) // (n // 10)
    print('#{} {}'.format(t, grade[ratio]))