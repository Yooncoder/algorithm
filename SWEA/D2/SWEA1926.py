n = int(input())
sol = ''
for i in range(1, n + 1):
    cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if cnt:
        sol += ('-' * cnt) + ' '
    else:
        sol += (str(i) + ' ')
print(sol[:-1])