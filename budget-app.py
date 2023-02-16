def truncate(n):
  multiplier = 10
  return int(n * multiplier) / multiplier

def gettotals(categories):
  total = 0
  breakdown = []
  for category in categories:
    total += category.getwithdrawals()
    breakdown.append(category.getwithdrawals())
  exact = list(map(lambda x: truncate(x/total), breakdown))
  return exact

def create_spend_chart(categories):
  res = "Percentage spent by category\n"
  i = 100
  totals = gettotals(categories)
  while i >= 0:
    cat_spaces = " "
    for total in totals:
      if total * 100 >= i:
        cat_spaces += "o  "
      cat_spaces += "  "
    res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
    i = 10

  dashes = "-" + "---"*len(categories)
  names = []
  x_axis = ""
  for category in categories:
    names.append(category.name)

  maxi = max(names,key=len)

  for x in range(len(maxi)):
    namestr = '     '
    for name in names:
      if x >= len(name):
        namestr += "   "
      namestr += name[x] + "  "

    if (x != len(maxi) -1 ):
      namestr += '\n'

    x_axis += namestr

  res += dashes.rjust(len(dashes)+4) + "\n" + x_axis
  return res

class Category:
    def __init__(self, c_name):
        self.c_name = c_name
        self.ledger = []
      
    def __str__(self):
        topline = f"{self.c_name:*^30}\n"
        entries = ""
        total = 0
        for entry in self.ledger:
          entries += f"{entry['description'][0:23]:23}" + f"{entry['amount']:>7.2f}" + '\n'
          
          total += entry['amount']

        printout = topline + entries + "Total:" + str(total)
        return printout

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description}) 

    def withdraw(self, amount, description=""):
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
      balance = 0
      for entry in self.ledger:
        balance += entry["amount"]
      return balance

    def transfer(self, amount, category):
        if(self.check_funds(amount)):
            self.withdraw(amount, "Transfer to " + category.c_name)
            category.deposit(amount, "Transfer from " + self.c_name)
            return True
        return False

    def check_funds(self, amount):
        if(self.get_balance() >= amount):
            return True
        return False

    def getwithdrawals(self):
      total = 0
      for entry in self.ledger:
        if entry["amount"] < 0:
          total += entry["amount"]
      return total
