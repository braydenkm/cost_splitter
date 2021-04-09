
# Transaction class object containing amount paid and by which member.
class Transaction:
  # Create a new Transaction object.
  def __init__(self, amount, paid_by, label):
    self.label = label
    self.amount = amount
    self.paid_by = paid_by
  

  # Return Transaction object information as a string.
  def as_string(self):
    label = self.label.ljust(12)
    cost = '$' + str(self.amount).ljust(8)
    payer = self.paid_by.name
    return 'Label: {} Cost: {} Paid By: {}'.format(label, cost, payer)
  
  
