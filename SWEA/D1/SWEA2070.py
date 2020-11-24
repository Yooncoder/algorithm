a = int(input())

for i in range(a):
    j = list(map(int, input().split()))
    if j[0] > j[1]:
        print('#{} >'.format(i + 1))
    elif j[0] == j[1]:
        print('#{} ='.format(i + 1))
    elif j[0] < j[1]:
        print('#{} <'.format(i + 1))