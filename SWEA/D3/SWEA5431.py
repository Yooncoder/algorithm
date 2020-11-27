for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    ks = list(map(int, input().split()))
    student = [0] * n
    for i in range(n):
        student[i] += 1 + i
    for i in ks:
        student.remove(i)
    print('#{}'.format(t), *student)