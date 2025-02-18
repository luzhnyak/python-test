def solution(number):
    if number <= 0:
        return 0

    sum = 0

    for i in range(number-1, 0, -1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


if __name__ == '__main__':
    print("Suma", solution(10))
