def genValidParen(n):
  helper(n, 0, "")


def helper(open, close, output):
  if(open == 0 and close == 0):
    print(output)
    return
  if open > 0:
    helper(open - 1, close + 1, output + "(")
  if close > 0:
    helper(open, close - 1, output + ")")

n = 5
print("All possible of " + str(n) + " pairs valid parentheses: ")
genValidParen(n)