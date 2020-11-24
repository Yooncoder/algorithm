tc = 10
for t in range(1, tc + 1):
    n, s = map(str, input().split())
    n = int(n)
    st = []
    result = 1
    for i in range(n):
        st.append(s[i])
    while result == 1:
        for i in range(1, n):
            if st[i - 1] == st[i]:
                del st[i - 1 : i + 1]
                n -= 2
                break
            if i == n - 1:
                result = 0
    print('#{} {}'.format(t, ''.join(st)))