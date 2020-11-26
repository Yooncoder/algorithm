sol = []
for t in range(1, int(input()) + 1):
    a, b, c, d = map(int, input().split())
    al = a / b
    bob = c / d
    if al > bob:
        sol.append('ALICE')
    elif bob > al:
        sol.append('BOB')
    else:
        sol.append('DRAW')
j = 0
for i in sol:
    j += 1
    print('#{} {}'.format(j, i))