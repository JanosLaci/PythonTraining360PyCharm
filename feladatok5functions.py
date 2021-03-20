# https://e-learning.training360.com/courses/take/python-alapismeretek/lessons/10509701-feladatok-funkciok

def is_it_leap_year(param_year):
    if param_year % 400 == 0:
        return True
    elif param_year % 100 == 0:
        return False
    elif param_year % 4 == 0:
        return True
    else:
        return False


entered_year = int(input("Enter the year. Is it a leap year?"))

print(str(is_it_leap_year(entered_year)))

is_it_a_tuple = 3, 14
print(is_it_a_tuple)
print(f'A típusa {type(is_it_a_tuple)}')
