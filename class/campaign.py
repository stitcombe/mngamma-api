from datetime import datetime


class campaign:
    def __init__(
        self, name, description, category, startDate, endDate, fundingGoal, currentFunds
    ):
        self.name = name
        self.description = description
        self.category = category
        self.startDate = datetime.strptime(startDate, "%Y-%d-%m").date()
        self.endDate = datetime.strptime(endDate, "%Y-%d-%m").date()
        self.fundingGoal = fundingGoal
        self.currentFunds = 500
