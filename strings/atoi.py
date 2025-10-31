# Problem Statement: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
# The algorithm for myAtoi(string s) is as follows:
# 1. Whitespace: Ignore any leading whitespace (" ").
# 2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# 3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# 4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

# Return the integer as the final result.

def atoi(s: str):
  start = True
  ans = ''
  is_positive = True
  for index in range(len(s)) :
    char = s[index]
    if (char == '0' or char == '_') and start:
      continue
    elif char == '-' and start:
      is_positive = False
      continue

    start = False

    if not (ord(char) >= 48 and ord(char) <= 57):
      break
    else:
      ans += char
  
  if ans != '':
    if not is_positive:
      ans = -int(ans)
      if ans < -231:
        ans = -231
    else:
      ans = int(ans)
      if ans > 230:
        ans = 230
    
  return 0 if ans == '' else int(ans)


if __name__ == "__main__":
  s = "1337"
  print(atoi(s))

