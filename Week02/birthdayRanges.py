def birthday_ranges(birthdays, ranges):
    m = {}

    for r in ranges:
        m[r] = 0

    for day in birthdays:
        for r in ranges:
            if(day >= r[0] and day <=r[1]):
                m[r]+=1

    lst = list(m.values())
    print(lst)

birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])
birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)])
