from Transaction import Transaction
from Member import Member


# Group class containing members, transaction, and total group debt.
class Group:
  # Create a new Group object.
  def __init__(self, name):
    self.name = name
    self.members = {}
    self.total_debt = 0
    self.transactions = []


  # Add a new purchase to balance through the group.
  def add_purchase(self, payer, amount):
    self.transactions.append(Transaction(amount, payer))
    amount_each = amount / self.number_of_members()
    amount_to_payer = amount - amount_each
    
    # Update each member's balance.
    for member in self.members:
      if payer == self.members[member]:
        payer.add(amount_to_payer)
        continue
      self.members[member].sub(amount_each)
    
    # Find total debt.
    # TODO Look into better way of updating this value.
    self.total_debt = 0
    for member in self.members:
      if self.members[member].in_debt():
        self.total_debt += self.members[member].balance
      
  
  # Add amount to total group debt.
  def add_debt(self, amount):
    self.total_debt += amount


  # Subtract amoount from total group debt.
  def sub_debt(self, amount):
    self.total_debt -= amount

  
  # Return number of members in group.
  def number_of_members(self):
    return len(self.members)


  # Add a member to a group.
  def add_member(self, member_name):
    self.members[member_name] = Member(member_name)
  

  # Remove a member to a group.
  def remove_member(self, member_name):
    if self.members[member_name].balance != 0:
      print('Member cannot be removed until balance equals $0')
      return
    self.members.pop(member_name)


  # Print out information on Group object.
  def print_group(self):
    string = '  Name: ' + self.name + '\n'
    string += '  Total Debt: ' + str(self.total_debt) + '\n  Members:\n'
    for person in self.members:
      string += '    ' + self.members[person].as_string() + '\n'
    print(string)