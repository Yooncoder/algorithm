for t in range(1, int(input()) + 1):
    student = list(map(int, input().split()))
    for i in range(len(student)):
        if student[i] < 40:
            student[i] = 40
    print('#{} {}'.format(t, sum(student) // len(student)))