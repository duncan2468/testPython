import requests
import json

wage = 20
hours = 40
weeks = 52
salary = wage * hours * weeks
print('Salary is ', salary)
if hours > 38:
    print("You are working too hard")