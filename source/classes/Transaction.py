
# Transaction class object containing amount paid and by which member.
class Transaction:
  # Create a new Transaction object.
  def __init__(self, amount, paid_by):
    # self.item = item
    self.amount = amount
    self.paid_by = paid_by
  

  # Return Transaction object information as a string.
  def as_string(self):
    return 'Paid By: ' + self.paid_by.name + ', Amount: ' + str(self.amount)
  
  
