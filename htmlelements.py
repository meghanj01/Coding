import re

# Examples

# Input: "<div><div><b></b></div></p>"
# Output: div

# Input: "<div>abc</div><p><em><i>test test test</b></em></p>" '''


def html_elements(strParams):
    open_tags = ["<b>", "<i>", "<em>", "<div>", "<p>"]
    close_tags = ["</b>", "</i>", "</em>", "</div>", "</p>"]

    stack = []
    tags = re.split("(<[^>]*>)", strParams)
    # print(tags)
    # breakpoint()
    for tag in tags:
        if tag in open_tags:
            stack.append(tag)
        elif tag in close_tags:
            check = close_tags.index(tag)
            if len(stack) > 0 and open_tags[check] == stack[-1]:
                stack.pop()
    if stack:
        return stack[-1].replace("<", "").replace(">", "")
    return True


print(html_elements("<div><div><b></b></div></p>"))
