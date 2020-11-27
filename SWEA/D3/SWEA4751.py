tc = int(input())

for i in range(1, tc + 1):
    data = input()
    row = 4 + len(data) + (len(data) - 1) * 3
    col = 5
    mat = [[0] * row for j in range(col)]
    s15 = '..#'
    s24 = '.#'
    s3 = '#'
    for k in range(len(data) - 1):
        s15 += '...#'
    s15 += '..'
    for k in range(len(data) * 2 - 1):
        s24 += '.#'
    s24 += '.'
    for k in range(len(data)):
        s3 = s3 + '.' + data[k] + '.#'

    print(s15)
    print(s24)
    print(s3)
    print(s24)
    print(s15)