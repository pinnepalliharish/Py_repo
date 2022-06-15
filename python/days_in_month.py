def is_leap(year):
  if (year%4==0 and year%100!=0)  or year%400==0:
    return True
  else:
    return False

def days_in_month(y,m): 
  month_days = ["",31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month>12 or month<1:
    return "there are only 12 months LOL !!"
  if is_leap(y)==True:
    month_days[2]=29
  return f"the number of days are {month_days[m]}"





  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#         return True
#   else:
#     return False
    
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month > 12 or month < 1:
#     return "Invalid month entered."
#   if month == 2 and is_leap(year):
#     return 29
#   return month_days[month - 1]



# #Do NOT change any of the code below 👇
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
