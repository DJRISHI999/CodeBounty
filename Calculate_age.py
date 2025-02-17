import time
from calendar import isleap

def calculate_age(name, birth_year, birth_month, birth_day):
    current_time = time.localtime(time.time())
    current_year = current_time.tm_year
    current_month = current_time.tm_mon
    current_day = current_time.tm_mday

    leap_year = isleap(current_year)


    if birth_year > current_year:
        print("Invalid birth year. It's in the future.")
        return


    if birth_month < 1 or birth_month > 12:
        print("Invalid birth month. It should be between 1 and 12.")
        return

    if birth_day < 1 or birth_day > 31:
        print("Invalid birth day. It should be between 1 and 31.")
        return


    if birth_month == 2 and birth_day > 29:
        print("Invalid birth day. It should be between 1 and 29.")
        return
    
    if birth_month in [4, 6, 9, 11] and birth_day > 30:
        print("Invalid birth day. It should be between 1 and 30.")
        return
    
    if birth_year == current_year and birth_month > current_month:
        print("Invalid birth month. It's in the future.")
        return
    
    if birth_year == current_year and birth_month == current_month and birth_day > current_day:

        print("Invalid birth day. It's in the future.")
        return
    

    if birth_year == current_year and birth_month == current_month and birth_day == current_day:
        print(f"Happy birthday, {name}!")
        return

# coverting days to months and years

    age_year = current_year - birth_year
    age_month = current_month - birth_month
    age_days = current_day - birth_day


    for year in range(birth_year, current_year):
        if not isleap(year):

            age_days += 366
        else:
            age_days += 365



    for month in range(birth_month, current_month):
        age_days += month_days(month, leap_year)

    age_days += current_day - birth_day


    if age_month < 0:
        age_year -= 1
        age_month += 12

    age_days = str(age_days)
        
    print(f"{name} is {age_year} years, {age_month} months, or {age_days} days old.")



           
    



def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year else 28

if __name__ == "__main__":
    name = input("Input your name: ")
    birth_year = int(input("Input your birth year: "))
    birth_month = int(input("Input your birth month: "))
    birth_day = int(input("Input your birth day: "))

    calculate_age(name, birth_year, birth_month, birth_day)
