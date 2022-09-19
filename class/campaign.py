from datetime import date, datetime

class campaign:
  def __init__(self, name, description, category, startDate, endDate, fundingGoal, currentFunds):
    self.name= name
    self.description = description
    self.category = category
    self.startDate = datetime.strptime(startDate, '%Y-%d-%m').date()
    self.endDate = datetime.strptime(endDate, '%Y-%d-%m').date()
    self.fundingGoal = fundingGoal
    self.currentFunds = calcFunds
  
  def age(self):
    today = date.today()
    age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    return age