num = 34


def fibonacci_checker(num):
    if num == 2 or num == 3:
        return "yes"
    first = 1
    second = 1
    for i in range(0, num):
        if first == num:
            return "yes"
        if first > num:
            break
        next_val = first
        first = second
        second = next_val + second
    return "no"


print(fibonacci_checker(num))
