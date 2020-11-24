tc = 10
for t in range(1, tc + 1):
    n = int(input())
    password = list(map(str, input().split()))
    m = int(input())
    od = list(map(str, input().split()))

    for i in range(len(od)):
        if od[i] == 'I':
            for j in range(int(od[i + 2])):
                password.insert(int(od[i + 1]) + j, od[j + i + 3])
        if od[i] == 'D':
            del password[int(od[i + 1]) : int(od[i + 1]) + int(od[i + 2])]
        if od[i] == 'A':
            for j in range(int(od[i + 1])):
                password.append(od[i + 2 + j])
    print('#{} '.format(t), end = '')
    print(*password[0 : 10])