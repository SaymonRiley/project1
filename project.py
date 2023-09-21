# import math
#
# def calculate_circle_area(r, alpha):
# alpha = math.degrees(alpha)
# S = (math.pi * r ** 2) * alpha / 360
# print("The area of the circle is:", S)
#
#
# import datetime
#
# def calculate_day(year, month, day):
#     input_date = datetime.datetime(year, month, day)
#     day_of_week = input_date.strftime('%A')
#     return day_of_week
# print(calculate_day())
#
# def arabic_to_roman(number):
#     roman_numerals = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
#     roman_number = ''
#     while number > 0:
#         for value, symbol in sorted(roman_numerals.items(), reverse=True):
#             if number >= value:
#                 roman_number += symbol
#                 number -= value
#                 break
#     return roman_number
#
# number = 1452
# roman_number = arabic_to_roman(number)
# print(f"The Roman equivalent of {number} is: {roman_number}")
#
#
#
#
#
# 
