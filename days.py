# function to test leap year
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
     
# nested function
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_year=is_leap(year)
  month-=1
  if leap_year :
    print(month)
    if month==1:
      return 29
    else:
      return month_days[month]
  else:
    month_days[month]
  
  
# input and function call
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
