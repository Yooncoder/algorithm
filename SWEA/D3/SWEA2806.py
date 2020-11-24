def n_q(n):
    def q(i, n, qs):
        if i == n:
            return 1

        sol = 0
        for j in range(n):
            pre = 0
            while pre < i:
                if qs[pre] == j or abs(pre - i) == abs(qs[pre] - j):
                    break
                pre += 1
            if pre == i:
                qs[i] = j
                sol += q(i + 1, n, qs)
        return sol
    return q(0, n, [0 for i in range(n)])

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    print('#{} {}'.format(t, n_q(n)))