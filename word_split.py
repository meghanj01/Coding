def word_split(word, dictinory):
    for i in range(len(word)):
        if word[:i] in dictinory and word[i:] in dictinory:
            return word[:i] + "," + word[i:]
    return False


print(word_split("baseball", ["a", "all", "b", "ball", "bas", "base", "cat", "d", "e"]))
print(
    word_split(
        "abcgefd", ["a", "ab", "abc", "abcg", "b", "c", "e", "dog", "efd", "zzzz"]
    )
)
