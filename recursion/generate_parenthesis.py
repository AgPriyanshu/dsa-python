def paren(n,string,count,result):
  if n == 0 and count == 0:
    return result.append(string)
  elif n == 0 and count != 0:
    return None
  elif count < 0:
    return None

  paren(n-1,string + '(', count + 1,result)
  paren(n-1,string + ')', count - 1,result)

  return result



if __name__ == "__main__":
  n = 3
  print(paren(2*n,"",0,[]))
