from datetime import datetime

class CalculateAge:
    def __init__(self, birth_date):
        self.birth_date = birth_date

    def calculate_age(self):
        today = datetime.today()
        years = today.year - self.birth_date.year
        months = today.month - self.birth_date.month
        days = today.day - self.birth_date.day

        if days < 0:
            months -= 1
            days += (self.birth_date.replace(month=self.birth_date.month+1, day=1) - self.birth_date.replace(day=1)).days

        if months < 0:
            years -= 1
            months += 12

        return years, months, days


class Personal:
    def __init__(self, name, gender, birth_date):
        self.name = name
        self.gender = gender
        self.age_calculator = CalculateAge(birth_date)

    def showInfo(self):
        years, months, days = self.age_calculator.calculate_age()
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {years} years, {months} months, and {days} days old.")


# Input
name = input("Enter your name: ")
gender = input("What is your gender?: ")
dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")
birth_date = datetime.strptime(dob_input, "%Y-%m-%d")

# Create object and show info
person = Personal(name, gender, birth_date)
person.showInfo()
