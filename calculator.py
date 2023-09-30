def calculator(input_string):
    stack = []
    stack2 = []
    switch = stack
    for i in input_string:
        if i == "(" and switch == stack:
            switch = stack2
            continue
        elif i == ")" and switch == stack2:
            switch = stack
            switch.append(stack2.pop())
        else:
            switch.append(i)
        while switch and len(switch) >= 3:
            second = switch.pop()
            sign = switch.pop()
            first = switch.pop()
            switch.append(simple_calculator(int(first), int(second), sign))

    return stack.pop()


def simple_calculator(a, b, sign):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "/":
        return a / b
    elif sign == "*":
        return a * b
    elif sign == "(":
        return


print(calculator("6*(4/2)+3*1"))
print(calculator("6/3-1"))
