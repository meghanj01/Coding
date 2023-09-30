def gcd(num1, num2):
    iterate = num2
    if num1 < num2:
        iterate = num1
    for i in range(iterate, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


print(gcd(7, 3))
print(gcd(36, 54))
