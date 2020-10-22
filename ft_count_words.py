def ft_count_words(str):
    count = 1
    for i in str:
        if i == ' ':
            count += 1
    return count
