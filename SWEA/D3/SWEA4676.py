for t in range(1, int(input()) + 1):
    st = list(input())
    l = len(st)
    h = int(input())
    data = list(map(int, input().split()))
    visit = [0] * (max(data) + 1)
    data.sort()
    cnt = 0
    for i in range(h):
        st.insert(data[i] + cnt, '-')
        cnt += 1
    print('#{} {}'.format(t, ''.join(st)))