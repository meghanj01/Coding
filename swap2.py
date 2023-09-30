import re


def transform_string(input_str):
    # Use regular expression to find words with digits in them
    words = re.findall(r"\b\w\d\w\b", input_str)
    print(words)
    # Loop through the words and replace digits with empty string
    for word in words:
        modified_word = re.sub(r"\d", "", word)
        input_str = input_str.replace(word, modified_word.capitalize())

    return input_str


input_str = "2s 6 du5d4e"
result_str = transform_string(input_str)
print(result_str)
