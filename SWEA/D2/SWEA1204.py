def sol(ans):
    max_count = 0
    max_val = 0
    for i in range(100, -1, -1):
        count = ans.count(i)
        if max_count < count:
            max_count = count
            max_val = i
    return max_val

a = int(input())
for j in range(a):
    b = int(input())
    k = list(map(int, input().split()))
    print('#{0} {1}'.format(b, sol(k)))