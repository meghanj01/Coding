from collections import Counter


def run_length(strings):
    values = Counter(strings)
    res = ""
    for val in values.items():
        res += str(val[1]) + val[0]
    return res


print(run_length("eeeeaaabbbcc"))
