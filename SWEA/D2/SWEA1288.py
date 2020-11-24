tc = int(input())
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, tc + 1):
    n = int(input())
    num_list = []
    for j in range(1, 1000000 + 1):
        nj = n * j
        if 0 < nj < 10:
            num_list.append(nj)
        elif 10 <= nj < 100:
            num_list.append(nj // 10)
            num_list.append(nj % 10)
        elif 100 <= nj < 1000:
            num_list.append(nj // 100)
            num_list.append((nj % 100) // 10)
            num_list.append((nj % 100) % 10)

        elif 1000 <= nj < 10000:
            num_list.append(nj // 1000)
            num_list.append((nj % 1000) // 100)
            num_list.append(((nj % 1000) % 100) // 10)
            num_list.append(((nj % 1000) % 100) % 10)

        elif 10000 <= nj < 100000:
            num_list.append(nj // 10000)
            num_list.append((nj % 10000) // 1000)
            num_list.append(((nj % 10000) % 1000) // 100)
            num_list.append((((nj % 10000) % 1000) % 100) // 10)
            num_list.append((((nj % 10000) % 1000) % 100) % 10)

        elif 100000 <= nj < 1000000:
            num_list.append(nj // 100000)
            num_list.append((nj % 100000) // 10000)
            num_list.append(((nj % 100000) % 10000) // 1000)
            num_list.append((((nj % 100000) % 10000) % 1000) // 100)
            num_list.append(((((nj % 100000) % 10000) % 1000) % 100) // 10)
            num_list.append(((((nj % 100000) % 10000) % 1000) % 100) % 10)

        elif 1000000 <= nj < 10000000:
            num_list.append(nj // 1000000)
            num_list.append((nj % 1000000) // 100000)
            num_list.append(((nj % 1000000) % 100000) // 10000)
            num_list.append((((nj % 1000000) % 100000) % 10000) // 1000)
            num_list.append(((((nj % 1000000) % 100000) % 10000) % 1000) // 100)
            num_list.append((((((nj % 1000000) % 100000) % 10000) % 1000) % 100) // 10)
            num_list.append((((((nj % 1000000) % 100000) % 10000) % 1000) % 100) % 10)

        if sorted(set(num_list)) == lst:
            break
    print('#{} {}'.format(i, nj))