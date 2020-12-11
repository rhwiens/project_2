from functions import *
from random import randint
import datetime

# Red_Knight
print(red_knight(0,8))
print("Solution: White, 16")

print(red_knight(0,7))
print("Solution: Black, 14")

print(red_knight(1, 6))
print("Solution: Black, 12")

print(red_knight(1,5))
print("Solution: White, 10")

# Array
print(array(''))
print("Solution: None")

print(array('1'))
print("Solution: None")

print(array('1, 3'))
print("Solution: None")

print(array('1,2,3'))
print("Solution: '2'")

print(array('1,2,3,4'))
print("Solution: 2 3")

# What_Century
print(what_century("2011"))
print("Solution: 21st")

print(what_century("2154"))
print("Solution: 22nd")

print(what_century("2259"))
print("Solution: 23rd")

print(what_century("1234"))
print("Solution: 13th")

print(what_century("1023"))
print("Solution: 11th")

# Solution
print(solution('world'))
print("Solution: dlrow")

print(solution('hello'))
print("Solution: olleh")

print(solution(''))
print("Solution: ")

print(solution('h'))
print("Solution: h")

# Gimme
print(gimme([2,3,1]))
print("Solution: 0")

print(gimme([5,10,14]))
print("Solution: 1")

# Sum_even_numbers
print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Solution: 30")

print(sum_even_numbers([]))
print("Solution: 0")

# Testit
print(testit([0], [1]))
print("Solution: [0,1]")

print(testit([1,2], [3,4]))
print("Solution: [1,2,3,4]")

print(testit([1], [2,3,4]))
print("Solution: [1,2,3,4]")

print(testit([1,2,3], [4]))
print("Solution: [1,2,3,4]")

print(testit([1,2], [1,2]))
print("Solution: [1,1,2,2]")

# Find_it
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print("Solution: 5")

print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print("Solution: -1")

print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))
print("Solution: 5")

print(find_it([10]))
print("Solution: 10")

print(find_it([1,1,1,1,1,1,10,1,1,1,1]))
print("Solution: 10")

print(find_it([5,4,3,2,1,5,4,3,2,10,10]))
print("Solution: 1")

# Get Villain Name
format_str = '%d/%m/%Y'

print(get_villain_name(datetime.datetime.strptime("1/1/2000", format_str)))
print("Solution: The Evil Pickle")

print(get_villain_name(datetime.datetime.strptime("2/2/2000", format_str)))
print("Solution: The Vile Hood Ornament")

print(get_villain_name(datetime.datetime.strptime("2/12/2000", format_str)))
print("Solution: The Awkward Hood Ornament")

# Index
print(index([1, 2, 3, 4],2))
print("Solution: 9")

print(index([1, 3, 10, 100],3))
print("Solution: 1000000")

# Quarter of
print(quarter_of(3))
print("Solution: 1")

print(quarter_of(8))
print("Solution: 3")

print(quarter_of(11))
print("Solution: 4")

# Sum square even root odd
print(sum_square_even_root_odd([4,5,7,8,1,2,3,0]))
print("Solution: 91.61")

print(sum_square_even_root_odd([1,14,9,8,17,21]))
print("Solution: 272.71")

# Multi Table
print(multi_table(5))
print("Solution: 1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45\n10 * 5 = 50")

print(multi_table(1))
print("Solution: 1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10")


