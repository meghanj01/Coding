input_string = "hello MEGHA Z"
num = 4

l = list()
for i in input_string:
    if i.isalnum():
        originalvalue = ord(i)
        value = ord(i) + 4
        if originalvalue in range(97, 123) and value not in range(97, 123):
            value = value // 26 + 97 - 1
        elif originalvalue in range(65, 91) and value not in range(65, 91):
            value = value // 26 + 65 - 1
        l.append(chr(value))
    else:
        l.append(i)

print("".join(l))
