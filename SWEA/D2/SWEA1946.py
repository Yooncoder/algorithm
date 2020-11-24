tc = int(input())

for i in range(1, tc + 1):
    n = int(input())
    string = ''
    print('#{}'.format(i))
    for j in range(n):
        ci, ki = input().split()
        string += str(ci) * int(ki)
    unzip = []
    for k in range(0, len(string), 10):
        unzip.append(string[k : k + 10])
    for l in range(len(unzip)):
        print(unzip[l])