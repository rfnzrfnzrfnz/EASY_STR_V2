def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_analysis(str):
    print(str[2])
    print(str[ft_len(str) - 2])
    print(str[0], str[1], str[2], str[3], str[4], sep="")
    i = 0
    while i != ft_len(str) - 2:
        print(str[i], end="")
        i += 1
    i = 0
    print(end="\n")
    while i != ft_len(str):
        if i % 2 == 0:
            print(str[i], end="")
        i += 1
    print(end="\n")
    i = 0
    while i != ft_len(str):
        if i % 2 != 0:
            print(str[i], end="")
        i += 1
    print(end="\n")
    i = 0
    while i != ft_len(str):
        print(str[ft_len(str) - i - 1], end="")
        i += 1
    print(end='\n')
    i = 0
    while i != ft_len(str):
        if i % 2 == 0:
            print(str[ft_len(str) - i - 1], end="")
        i += 1
    print(end='\n')
    print(ft_len(str))
