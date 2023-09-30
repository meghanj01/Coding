# def missing_digit(str):
#     x = str.index("x")
#     first, second = str.split("=")
#     if x not in first:
#         eval(first)
#     for i in range(0, 9):
#         first[x] == i
#         num = 0
#         sign = None
#         numbers = []
#         for j in range(len(first)):
#             if j.isdigit():
#                 num = num * 10 + first[j]
#             else:
#                 numbers.append(num)
#                 numbers.append(j)
#             if numbers and len(numbers) == 3:
#                 second = numbers.pop()
#                 sign = numbers.pop()
#                 first = numbers.pop()
#                 numbers.append(calculate(second, first, sign))
#         if numbers.pop() == second:
#             return i


# def calculate(second, first, sign):
#     if sign == "+":
#         return first + second
#     elif sign == "-":
#         return first - second
#     elif sign == "*":
#         return first * second
#     elif sign == "/":
#         return float(first / second)


# missing_digit("4-2=x")


def missing_digits(nums):
    x = 0
    temp = nums.replace("x", str(x))
    arr = temp.split("=")
    while eval(arr[0]) != eval(arr[1]):
        x += 1
        temp = nums.replace("x", str(x))
        arr = temp.split("=")
    return x


print(missing_digits("4-2=x"))
print(missing_digits("10x0*12=12000"))
