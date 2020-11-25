for t in range(1, int(input()) + 1):
    n = int(input())
    card = list(input().split())
    suffle = []
    if n % 2 == 0:
        first = [*card[ : n // 2]]
        second = [*card[n // 2:]]
        for i in range(n // 2):
            suffle.append(first[i])
            suffle.append(second[i])
    else:
        first = [*card[ : n // 2 + 1]]
        second = [*card[n // 2 + 1 : ]]
        for i in range(n // 2 + 1):
            suffle.append(first[i])
            if len(second) <= i:
                continue
            suffle.append(second[i])
    print('#{}'.format(t), *suffle)