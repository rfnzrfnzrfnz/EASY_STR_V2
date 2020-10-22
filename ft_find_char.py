def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_find_char(char, str):
    count = 0
    x = 0
    r = 0
    if char in str:
        for i in range(ft_len(str)):
            if str[i] == char:
                x = i

                break

        for i in str:
            if i == char:
                count += 1
        if count == 1:
            return x
        else:
            for i in range(ft_len(str)):
                if str[i] == char:
                    r = i
            return x, r


    else:
        return False
