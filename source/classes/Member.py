
# Member class for tracking member name and balance.
class Member:
  # Create a new Member object.
  def __init__(self, name):
    self.name = name
    self.balance = 0
  

  # Return true if member is in debt, false otherwise.
  def in_debt(self):
    return self.balance < 0
  

  # Add amount to member's balance.
  def add(self, amount):
    self.balance += amount


  # Subtract amount from member's balance.
  def sub(self, amount):
    self.balance -= amount
  

  # Return Member object information as a string.
  def as_string(self):
    return 'Name: ' + self.name + ', Balance: ' + str(self.balance)
    
