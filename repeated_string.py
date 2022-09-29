def repeatedString(s, n):
    new_str = s
    str_length = len(s)
    if str_length == 1 and s == "a":
        return n
    count_a = 0
    for i in s:
        if i == "a":
            count_a += 1
    if count_a == 1:
        return n//str_length
    elif count_a == 0:
        return 0
    else:
        count_a = 0
    while str_length < n:
        remaining = n - str_length
        if remaining == 1:
            new_str += s[0]
            str_length += remaining
        elif remaining < len(s):
            new_str += s[remaining]
            str_length += remaining
        else:
            new_str += s
            str_length += len(s)

    for i in new_str:
        if i == 'a':
            count_a += 1

    return count_a


if __name__ == '__main__':
    s = "jdiacikk"
    n = 899491

    result = repeatedString(s, n)
    print(result)
