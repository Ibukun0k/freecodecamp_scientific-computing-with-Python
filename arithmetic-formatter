import regex


def arithmetic_arranger (problems, solve = False):
    if (len(problems) > 5):
      return "Error: Too many problems."

    firstnum = ""
    secondnum = ""
    lines = ""
    sumx = ""
    string = ""
    
    for problem in problems:
      if (regex.search("[^\s0-9.+-]", problem)):
        if (regex.search("[/]", problem) or regex.search("[*]", problem)):
         return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."

      first = problem.split(" ") [0]
      operator = problem.split(" ") [1]
      second = problem.split(" ") [2]

      if (len(first)>= 5 or len(second) >=5):
        return "Error: Numbers cannot be more than four digits."

      sum = ""
      if operator == "+":
        sum = str(int(first) + int(second))
      elif operator == "-":
        sum = str(int(first) - int(second))

      length = max(len(first), len(second)) + 2
      top = str(first).rjust(length)
      bottom = operator + str(second).rjust(length - 1)
      line = ""
      res = str(sum).rjust(length)
      for s in range (length):
        line += "-"

      if problem != problems[-1]:
        firstnum += top + '    '
        secondnum += bottom + '    '
        lines += line + '    '
        sumx += res + '    '
      else:
        firstnum += top
        secondnum += bottom
        lines += line
        sumx += res

    if solve:
      string = firstnum + "\n" + secondnum + "\n" + lines + "\n" + sumx
    else:
      string = firstnum + "\n" + secondnum + "\n" + lines
    return string
