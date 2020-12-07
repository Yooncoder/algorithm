for t in range(1, int(input()) + 1):
    n = int(input())
    sol = []
    for i in range(n):
        sol.append(input())
    start = 0
    end = n - 1
    res = []
    if start == end:
        res.append(sol[start])
    while start != end:
        s, e = start, end
        if ord(sol[start]) < ord(sol[end]):
            res.append(sol[start])
            s += 1
        elif ord(sol[start]) > ord(sol[end]):
            res.append(sol[end])
            e -= 1
        else:
            checks = start + 1
            checke = end - 1
            same = False
            diff = False
            while True:
                if sol[checks] != sol[checke]:
                    diff = True
                    break
                else:
                    if checks + 1 <= checke - 1:
                        checks += 1
                        checke -= 1
                    else:
                        same = True
                        break

            if same == False:
                if ord(sol[checks]) < ord(sol[checke]):
                    res.append(sol[start])
                    s += 1
                else:
                    res.append(sol[end])
                    e -= 1
            if same == True:
                res.append(sol[start])
                s += 1
        start = s
        end = e
        if start == end:
            res.append(sol[start])

    print('#{} {}'.format(t, ''.join(res)))