import re

for t in range(1, int(input()) + 1):
    n = int(input())
    sentence = re.split('[.?!]',input())[0:n]
    print("#{}".format(t), end=' ')

    for i in sentence:
        cnt = 0
        for j in i.split():
            if j[0].isupper() and j.isalpha():
                if len(j) == 1:
                    cnt += 1
                if j[1:].islower():
                    cnt += 1
        print(cnt, end=' ')
    print('')