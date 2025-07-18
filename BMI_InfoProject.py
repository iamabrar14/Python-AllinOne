import win32com.client
from datetime import datetime


# Age Calculation Class
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


# BMI Calculator Class
class BMICalculator:
    def __init__(self, height_ft, weight_kg):
        self.height_ft = height_ft
        self.weight_kg = weight_kg

    def calculate_bmi(self):
        height_m = self.height_ft * 0.3048  # Convert ft to meters
        bmi = self.weight_kg / (height_m ** 2)
        return round(bmi, 2)


# Personal Information Class
class Personal:
    def __init__(self, name, gender, birth_date):
        self.name = name
        self.gender = gender
        self.age_calculator = CalculateAge(birth_date)

    def showInfo(self):
        s1 = win32com.client.Dispatch("SAPI.SpVoice")
        s2 = win32com.client.Dispatch("SAPI.SpVoice")
        s3 = win32com.client.Dispatch("SAPI.SpVoice")
        years, months, days = self.age_calculator.calculate_age()
        a = (f"The  name of the user is :  {self.name}")
        b = (f"He is  a    {self.gender}")
        c = (f"his age: {years} years,   {months} months, and   {days} days old.")

        print(a)
        print(b)
        print(c)

        s1.Speak(a)
        s2.Speak(b)
        s3.Speak(c)


# Input Section
n = win32com.client.Dispatch("SAPI.SpVoice")

n.Speak("Enter your name :")
name = input("Enter your name: ")

n.Speak("Enter your gender :")
gender = input("What is your gender?: ")

n.Speak("Enter your date of birth by following the pattern")
dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")
birth_date = datetime.strptime(dob_input, "%Y-%m-%d")

# Height and Weight for BMI
n.Speak("Enter your height in feet")
height_ft = float(input("Enter your height in feet: "))

n.Speak("Enter your weight in kilograms")
weight_kg = float(input("Enter your weight in kg: "))

# Create object and show info
person = Personal(name, gender, birth_date)
person.showInfo()

# Calculate BMI
bmi_calculator = BMICalculator(height_ft, weight_kg)
bmi_value = bmi_calculator.calculate_bmi()

# Speak and print BMI
bmi_message = f"Your Body Mass Index is {bmi_value}"
print(bmi_message)
n.Speak(bmi_message)

n.Speak("Thanks for using me")
