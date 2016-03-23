class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name=name
  def __repr__(self):
    return "The account belongs to %s. Balance: %s" %(self.name, str("%.2f" % self.balance))
  def show_balance(self):
    print "%.2f" % self.balance
  def deposit(self, amount):
    if amount<= 0:
      print "error! deposit is less than/equal to zero."
      return
    else:
      print "Deposit amount: %.2f" %amount
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount> self.balance:
      print "Error! Withdrawed amount exceeds balance."
    else:
      print "Withdraw amont %.2f" % amount
      self.balance -=amount
      self.show_balance()

my_account = BankAccount("Claire")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account


      
    
      
    
