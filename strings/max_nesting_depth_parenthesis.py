# Problem Statement: Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses. 
def max_nesting_depth_parenthesis(s: str):  
  depth = 0
  max_depth = 0
  for letter in s:
    if letter == '(':      
      depth += 1
      if max_depth < depth:
        max_depth = depth
    elif letter == ')':
      depth -=1 
  
  return max_depth

if __name__ == "__main__":
  s = ""
  print(max_nesting_depth_parenthesis(s))

