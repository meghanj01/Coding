l = ["a", "b", "c"]


# def string_reduction(string):
#     if set(string) == 1:
#         return len(string)
#     newstring = []
#     for i in range(0, len(string), 2):
#         breakpoint()
#         if len(string) - 1 > i + 1:
#             if string[i] and string[i + 1] and string[i] != string[i + 1]:
#                 for j in l:
#                     # breakpoint()
#                     if j != string[i] and j != string[i + 1]:
#                         val = i
#                         newstring.append(val)
#     string_reduction(newstring)


def string_reduction(str):
    res = len(str) + 1
    while res > len(str):
        res = len(str)
        str = str.replace(/ab|ba/, "c")
        str = str.replace("ba", "c")
        str = str.replace("cb", "a")
        str = str.replace("bc", "a")
        str = str.replace("ac", "b")
        str = str.replace("ca", "b")
        print(str)
    return len(str)


i = "abcabc"
# i = list(i)
print(string_reduction(i))


def StringReduction(str): 
    str = list(str)
    cSet = set(['a','b','c'])
    repeat = True
    while repeat:
      i = 0
      repeat = False
      while i < len(str)-1:
        if str[i] != str[i+1]:
          str[i:i+2] = list(cSet-set([str[i],str[i+1]]))
          repeat = True
        else:
          i += 1
    return len(str)
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print StringReduction(raw_input())  