# The math to check if it's a leap year or not 
# Was taken from a Google search 
# This function returns True or False depending on the given year 
# Being a Leap year or not. 
def is_leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

leap = is_leap_year(2024)
print(leap)
