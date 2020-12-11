import collections
from datetime import date

def multi_table(number):
    answer = str()
    for x in range(1,11):
        mult = number * x
        answer += '{} * {} = {}\n'.format(x, number, mult)
        
    return answer.strip('\n')

def sum_square_even_root_odd(nums):
    sum = 0
    for _num in nums:
        if _num%2 == 0:
            sum = sum + _num**2
        else:
            sum = sum + _num**0.5
    sum = round(sum, 2)    
    return sum

def quarter_of(month):
    if month <= 3:
        return 1
    elif month > 3 and month <= 6:
        return 2
    elif month > 6 and month <= 9:
        return 3
    return 4

def index(array, n):
    if len(array) - 1 < n:
        return -1
    return array[n]**n

def get_villain_name(birthdate): 
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    # your code here
    name = first[birthdate.month-1] + ' ' + last[birthdate.day%10]
    return name

def find_it(seq):
    if len(seq) == 0:
        return None
    b = collections.Counter(seq)
    for position in b:
        if b[position] % 2 ==1:
            return position

def testit(a, b):
    a = list(set(a))
    b = list(set(b))
    answer = sorted(a+b)
    return answer

def sum_even_numbers(seq): 
    sum = 0
    for x in seq:
        if x%2 == 0:
            sum = sum + x
    return sum

def gimme(input_array):
    inputsorted = sorted(input_array)
    middle = inputsorted[1]
    return input_array.index(middle)

def solution(string):
    return string[::-1]

def what_century(year):
    year = int(year)
    century = (year-1)/100
    ending = "th"
    century = int(century)+1
    century = str(century)

    if century[len(century)-1] == '1':
        ending = "st"
    elif century[len(century)-1] == '2':
        ending = "nd"
    elif century[len(century)-1] == '3':
        ending = "rd"
    
    if century == '11':
        ending = "th"
    if century == '12':
        ending = "th"
    if century == '13':
        ending = "th"
    answer = century + ending
    return answer

def array(string):
    string2 = " ".join(string.split(',')[1:-1])
    return string2 or None

def red_knight(N, P):
    if P%2 == N:
        return ('White', P*2)
    return ('Black', P*2)