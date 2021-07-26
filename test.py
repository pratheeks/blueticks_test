def alternatingRanges(s, up):
    count = 0
    str_list = []
    for i in range(len(s)):
        try:
            if s[i] == s[i+1] - 1:
                continue
            else:
                if (s[i] + 1) == (s[i+1] - 1):
                    str_list.append(str(s[i] + 1))
                else:
                    if s[i + 1] == upper:
                        s[i + 1] = upper + 1
                    str_list.append(str(s[i] + 1) + '->' + str(s[i+1] - 1))
        except IndexError:
            pass
    return str_list


if __name__ == '__main__':
    lower = 0
    upper = 99
    q = [0, 1, 3, 50, 75]
    if lower not in q:
        q.insert(0, lower)
    if upper not in q:
        q.append(99)
    q = sorted(q)
    result = alternatingRanges(q, upper)
    print(result)
