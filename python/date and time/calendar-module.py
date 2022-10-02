# input: 08 05 2015
# output: WEDNESDAY

# Enter your code here. Read input from STDIN. Print output to STDOUT
from calendar import weekday, weekheader

[month, day, year] = map(int, input().split())
dayName = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
name_day = dayName[weekday(year,month, day)]
print(name_day)