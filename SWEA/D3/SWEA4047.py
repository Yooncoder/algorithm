for t in range(1, int(input()) + 1):
    data = input()
    card = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    check = set()
    for i in range(0, len(data), 3):
        check.add(data[i : i + 3])
    if len(check) != len(data) // 3:
        print('#{} {}'.format(t, 'ERROR'))
    else:
        for i in check:
            if i[0] in card.keys():
                card[i[0]] -= 1
        print('#{}'.format(t), *list(card.values()))