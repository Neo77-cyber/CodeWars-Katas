# Find letter 'n' in a List

def find_needle(haystack):
    for i in haystack:
        if i[0] == "n":
            return f'found the needle at position {haystack.index("needle")}'
        else:
            pass

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))





# Operations 

def past(h, m, s):
    return (h *3600000 + m*60000 + 1 * 1000)
print(past(0,1,1))





# Make a string uppercase

def make_upper_case(s):
    return s.upper()
print(make_upper_case("learn"))





# Repeat strings

def repeat_str(repeat, string):
    # duplicate the string for a number of times
    return string * repeat
print(repeat_str(6,"hello"))





# Product of all the numbers in a list

def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product
print(grow([1,2,3,4,5]))





# Positive sum of numbers in a list

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum = sum + i
    return sum
        
print(positive_sum([1,-4,7,12]))





# Reverse squnece of a list

def reverse_seq(n):
    output = []
    for i in range(n):
        output.append(n)
        n -= 1
    return output
print(reverse_seq(7))





# sSummation of numbers

def summation(num):
    output = []
    for i in range(num):
        output.append(num)
        num -= 1
    return sum(output)
print(summation(2))




# replacing/removing a letter in a string

def remove_exclamation_marks(s):
                                                        
    return s.replace('!', '')




        
# Mask letters in a string 

def maskify(cc):
    return len(cc[:-4])*"#" + cc[-4:] 
                                                       
print(maskify("Newstataus@12"))





# Get the minimum

def find_smallest_int(arr):                                             
        return min(arr)

print(find_smallest_int([34, -345, -1, 100]))





# Find the next square

from math import sqrt
from this import s


def find_next_square(sq):

    if int(sqrt(sq)) == sqrt(sq):
        return (sqrt(sq) + 1) ** 2
    else:
        return -1
print(find_next_square(144))





# returns the first number as an integer

def get_age(age):
   
    x= age.split()
    return int(x[0])

print(get_age("1 years old"))





# Make a sentence upper case

import string

def to_jaden_case(my_text):
    
    return string.capwords(my_text)

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))






# Filter list for integers 

def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list

print(filter_list([1,2,'a','b']))






# Sorting strings 

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))


   
    

def nb_year(p0, percent, aug, p):
    # how many years will it take to be 1200
    x = p0 + percent/100 + aug
    while x >= p:
        print(x)
print(nb_year(1000, 2, 50, 1200))





    
    
    


    
        
            




             
    


    

    
    



    

    







