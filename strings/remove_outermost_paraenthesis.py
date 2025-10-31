# Problem Statement: A valid parentheses string is defined by the following rules:
# It is the empty string "".
# If A is a valid parentheses string, then so is "(" + A + ")".
# If A and B are valid parentheses strings, then A + B is also valid.

# A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.

# Given a valid parentheses string s, your task is to remove the outermost parentheses from every primitive component of s and return the resulting string. 

def remove_outermost_parenthesis(s: str):
  level = 0
  result = ''

  for substr in s:
    if substr == '(':
      if level > 0:
        result += '('
      level += 1

    else:
      if level > 1:
        result += ')'
      level -= 1

  return result

if __name__ == "__main__":
  s = '(()())(())'
  print(remove_outermost_parenthesis(s))

