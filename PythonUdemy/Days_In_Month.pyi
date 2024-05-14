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


# TODO: Add more code here 👇
def days_in_month(year, month):
    if is_leap(year) == False:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_num = month_days[month]
    elif is_leap(year) == True:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_num = month_days[month]
    return days_num


#🚨 Do NOT change any of the code below
year = int(input("What year is it?: "))  # Enter a year
month = int(input("What month is it?: "))  # Enter a month
days = days_in_month(year, month)
print(days)
