from stack import Stack


# Problem Statement: Check Balanced Parentheses. Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false.
def check_for_balanced_parenthesis(s: str):
    stack = Stack()
    open_paranthesis = ["(", "{", "["]
    for parenthesis in s:
        if parenthesis in open_paranthesis:
            stack.push(parenthesis)
        elif parenthesis == ")" and stack.top_value() == "(":
            stack.pop()
        elif parenthesis == "}" and stack.top_value() == "{":
            stack.pop()
        elif parenthesis == "]" and stack.top_value() == "[":
            stack.pop()

    return stack.size() == 0


if __name__ == "__main__":
    print(check_for_balanced_parenthesis("()[{}()]"))
