from datetime import date

today = date.today()
print("today is:",today)
print("day:",today.day)
print("month:",today.month)
print("year:",today.year)

print(today.strftime("%A, %dth of  %B %Y"))

