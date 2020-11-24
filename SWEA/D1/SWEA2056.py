k = int(input())
month_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(k):
    cal = input()
    year = int(cal[0:4])
    month = int(cal[4:6])
    day = int(cal[6:8])

    print('#%d ' % (i + 1), end='')

    if month > 12 or month < 1:
        print(-1)
    else:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day > 31 or day < 1:
                print(-1)
            else:
                print('%.4d/%.2d/%.2d' % (year, month, day))
        elif month == 2:
            if day > 28 or day < 1:
                print(-1)
            else:
                print('%.4d/%.2d/%.2d' % (year, month, day))
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30 or day < 1:
                print(-1)
            else:
                print('%.4d/%.2d/%.2d' % (year, month, day))