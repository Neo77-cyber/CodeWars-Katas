# user_name = input("Username")
# age = input("Age")
# # current year - age + 100

# age_program = int(age) + 100 + 2022



# value of n + nn + nnn 
# valid triangle 

def find_needle(haystack):
    for i in haystack:
        if i[0] == "n":
            return f'found the needle at position {haystack.index("needle")}'
        else:
            pass

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

def past(h, m, s):
    return (h *3600000 + m*60000 + 1 * 1000)
print(past(0,1,1))

def make_upper_case(s):
    return s.upper()
print(make_upper_case("learn"))

def cockroach_speed(s):
    return int(s*27.778)
print(cockroach_speed(1.08))

def repeat_str(repeat, string):
    # duplicate the string for a number of times
    return string * repeat
print(repeat_str(6,"hello"))

def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product
print(grow([1,2,3,4,5]))

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum = sum + i
    return sum
        
print(positive_sum([1,-4,7,12]))

def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
print(simple_multiplication(13))

def reverse_seq(n):
    output = []
    for i in range(n):
        output.append(n)
        n -= 1
    return output
print(reverse_seq(7))

def reverseseq(n):
    return range(n, 0, -1)

print(reverse_seq(7))

def summation(num):
    output = []
    for i in range(num):
        output.append(num)
        num -= 1
    return sum(output)
print(summation(2))

def summation(num):
    total = 0
    for i in range(0, num+1):
                                                        
        total = total + i
    return total
    
def remove_exclamation_marks(s):
                                                        # replacing/removing a letter in a string
    return s.replace('!', '')

def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."

print(update_light("green"))
        
def maskify(cc):
    return len(cc[:-4])*"#" + cc[-4:] 
                                                        # using len
print(maskify("Newstataus@12"))

def find_smallest_int(arr):
    
                                                        # minimum i
        return min(arr)

print(find_smallest_int([34, -345, -1, 100]))

from math import sqrt
from this import s


def find_next_square(sq):

    if int(sqrt(sq)) == sqrt(sq):
        return (sqrt(sq) + 1) ** 2
    else:
        return -1
print(find_next_square(144))

def greet(name):

    return f"Hello, {name} how are you doing today?"

print(greet("Neo"))

def get_age(age):
   # returns the first number as an integer

    x= age.split()
    return int(x[0])

print(get_age("1 years old"))

import string

def to_jaden_case(my_text):
    
    return string.capwords(my_text)

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list

print(filter_list([1,2,'a','b']))

def is_uppercase(letter):
    if letter.upper()==letter:
        return True
    else:
        return False

print(is_uppercase('$3$'))

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    empty_list = []
    
    if geese in birds:
            empty_list.pop(birds)
        
       

print(geese('pigeoon', 'bird', 'donkey'))






