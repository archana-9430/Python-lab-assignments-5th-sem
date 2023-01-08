'''9. Write a user defined function to check whether a year is leap year
or not. '''

def check_leap(year: int):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


