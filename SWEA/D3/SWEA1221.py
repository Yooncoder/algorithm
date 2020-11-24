stand = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

tc = int(input())
for t in range(1, tc + 1):
    tt, n = map(str, input().split())
    n = int(n)
    data = list(map(str, input().split()))
    lst = []
    re_lst = []
    for i in range(n):
        if data[i] in stand:
            lst.append(stand.index(data[i]))
    lst.sort()
    for i in range(n):
        re_lst.append(stand[lst[i]])
    print('#{}'.format(t))
    print(*re_lst)