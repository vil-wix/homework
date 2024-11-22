for num in range(3, 21):
    result = f'{num} - '
    for i in range(1, num):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                result += f'{i}{j}'
    print(result)
