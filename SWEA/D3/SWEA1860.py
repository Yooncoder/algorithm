tc = int(input())
for i in range(1, tc + 1):
    n, m, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    nn = max(p)
    bread = [0] * (nn + 1)
    people = [0] * (nn + 1)
    for j in range(m, nn + 1, m):
        bread[j] += k
    for j in range(1, len(bread)):
        bread[j] = bread[j - 1] + bread[j]
    for j in p:
        people[j] += 1
    for j in range(1, len(people)):
        people[j] = people[j - 1] + people[j]
    result = True
    for j in p:
        if bread[j] < people[j]:
            result = False

    if result == False:
        print('#{} {}'.format(i, 'Impossible'))
    else:
        print('#{} {}'.format(i, 'Possible'))