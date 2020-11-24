tc = 10
for t in range(1, tc + 1):
    n = int(input())
    secret = list(map(int, input().split()))
    while secret[len(secret) - 1] > 0:
        for i in range(1, 6):
            p = secret.pop(0) - i
            if p <= 0:
                p = 0
                secret.append(p)
                break
            secret.append(p)
    print('#{}'.format(t), *secret)