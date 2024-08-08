#how many days aliv


 
from datetime import datetime as da




date1 = da.strptime("18-08-2024" , "%d-%m-%Y")
date2 = da.strptime("08-08-1987" , "%d-%m-%Y")

diff = date2 - date1
print(diff)

day_diff = diff.days

print(day_diff)