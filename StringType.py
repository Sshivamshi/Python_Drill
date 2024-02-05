# In Python, Strings are arrays of bytes representing Unicode characters.
z = 'a'  # string of len 1 not a char
# Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.
a = 'Hello'
b = " 'Hello' "
# c = " ''' "Hello" ''' " # invalid syntax 
c = ''' "Hello" ''' # ''' triple quotes are used to print double quoted string and multiline string
d = ''' This is a 
multiline            text.'''
print(a,b,c)
print(d)
''' OUTPUT: 
Hello  'Hello'   "Hello" 
 This is a 
multiline            text. '''  # This is Docstring format , can be used a multiline Python Comments 

s = 'Hello Himmi'
print(s[-1]) # i    s[-1] returns the last char in string and -2 represents the second last and so on 
print(s[-2]) # m     if indexing from left to right is  0-12  then in reverse it's (-1)-(-13)
# While accessing an index out of the range will cause an IndexError. Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError

# Reversing a String : 
# print(s.reverse())  # AttributeError: 'str' object has no attribute 'reverse'
print(s[::-1])   # immiH olleH


# Code to check if string is palindrome 
s = ['MOM' ,'DAD','GOD' ]
for word in s :
    if word == word[::-1]:   # If  String == Reversed string 
        print('Palindrome')
    else:
        print('Not Palindrome')
''' OUTPUT: 
Palindrome
Palindrome
Not Palindrome
'''

string = "Geeks for Geeks"
print(reversed(string))   # <reversed object at 0x7f4b1ea148b0>   # The reversed() function in Python returns a reversed iterator, not a reversed string. The reversed iterator can be used in a loop or converted to other iterable types, but it is not automatically converted to a string.

print(str(reversed(string))) # <reversed object at 0x7f4b1ea148b0>  :    # The reversed() function in Python returns a reversed iterator, not a reversed string. The reversed iterator can be used in a loop or converted to other iterable types, but it is not automatically converted to a string.

reversedString = list(reversed(string))    # Reversed object (iterable) coverted to list , similar to map objects are coverted to list using list() 

s = ''.join(reversed(string))
print(s)   
print(reversedString)  #  ['s', 'k', 'e', 'e', 'G', ' ', 'r', 'o', 'f', ' ', 's', 'k', 'e', 'e', 'G']

string = "hello"
listOfReversed = []

listOfReversed.extend(map(str.upper, reversed(string)))
print(listOfReversed)   # ['O', 'L', 'L', 'E', 'H']


listOfReversed2 = list(map(input, reversed(string)))  
 # OUTPUT : s  :  input() function might not behave as expected input() requires user interaction and is designed to be used interactively in the console, which might not align well with the expectations of map().    output.extend(map(square, numbers))square() is a regular function that takes a value and returns its square. It works seamlessly with map() because it's designed to work as a regular function, not expecting user interaction.
print(listOfReversed2)

s = "hello"
s_reversed = reversed(s)  # but note that reversed() return a reversed type object which is an iterable 
print(s_reversed)    # OUTPUT : <reversed object at 0x7ffba299f8b0>
s_reversed2 = s[::-1]  # Reversed
print(s_reversed2)     # OUTPUT: olleh 
# converting the reversed type object to list type object , using list() as it creates a new list object and puts values into it . Similar to converting  
print(list(reversed(s))) #  ['o', 'l', 'l', 'e', 'h'] 
rever = ''.join(reversed(s))
print(rever)      # OUTPUT: olleh 

string = "hello"
listOfReversed = []
listOfReversed.extend(map(str.upper, reversed(string)))
print(listOfReversed)   # ['O', 'L', 'L', 'E', 'H']

'''
String Methods:

- `capitalize()`
  - Returns a copy of the string with its first character capitalized.

- `lower()`
  - Returns a copy of the string converted to lowercase.

- `upper()`
  - Returns a copy of the string converted to uppercase.

- `title()`
  - Returns a titlecased version of the string where words start with an uppercase character.

-  string.count(Substr, start, end)
  - Returns the number of occurrences of a substring in the string.

- `find(sub[, start[, end]])`
  - Returns the lowest index in the string where a substring is found. Returns -1 if not found.

- `replace(old, new[, count])`
  - Returns a copy of the string with occurrences of the old substring replaced by the new substring.

- `startswith(prefix[, start[, end]])`
  - Returns `True` if the string starts with the specified prefix; otherwise, returns `False`.

- `endswith(suffix[, start[, end]])`
  - Returns `True` if the string ends with the specified suffix; otherwise, returns `False`.

'''
s = "hello"
print(s.capitalize())    # Hello
z = s.capitalize()      # Even if we don't assign to z, the original string will not be affected. In Python, strings are immutable, meaning their content cannot be changed after they are created. When you perform operations that modify a string, such as s.upper() or s.capitalize(), a new string with the modified content is created, and the original string remains unchanged. And here the concept of garbage collection comes in , to handle the old (original string )

print(type(z))      # <class 'str'>   Return type is string
y = s.capitalize   # missing bracket When you assign y = s.capitalize without parentheses, you are actually assigning the method itself to the variable y, not calling the method. Therefore, type(y) returns <class 'builtin_function_or_method'> because it's a reference to the method itself, not the result of calling the method. 
print(type(y))  # <class 'builtin_function_or_method'>

# Note : If the method returns nothing then print function will print None ( of None datatype) else the results

# Note: If the method returns nothing, then the print function will print None (of None datatype).
# Otherwise, it prints the result.
print(s.upper())     # Output: HELLO
print(s.lower())     # Output: hello
print(s.upper())     # Output: HELLO
print(s)             # Output: hello (original string s)

s = 'he is a good boy,he is a emperor , he walks his path '
print(s.count('he'))   # 3
print(s.count('he', 17 ,20 ))    # 1 
print(s.count('he', 17 ))    # 2
# string.count(value, start, end)  
#  start:  An Integer. The position to start the search. Default is 0   End : An Integer. The position to end the search. Default is the end of the string



'''

### Built-in Functions (Taking String as Argument):

- `len(s)`
  - Returns the length (number of characters) of the string.

- `max(iterable, *[, key, default])`
  - Returns the largest item in an iterable or the largest of two or more arguments.

- `min(iterable, *[, key, default])`
  - Returns the smallest item in an iterable or the smallest of two or more arguments.

- `ord(c)`
  - Returns an integer representing the Unicode character.

- `chr(i)`
  - Returns a string representing a character whose Unicode code point is the integer.


'''




'''

### Operations on Strings:

- Concatenation: `s1 + s2`

- Repetition: `s * n` (repeats the string s n times)

'''







'''


### Type Conversions (From String):

- `int(s[, base])`
  - Converts a string to an integer with an optional base for interpreting the string.

- `float(s)`
  - Converts a string to a floating-point number.

- `bool(s)`
  - Converts a string to a Boolean value.

'''

'''

### Type Conversions (To String):

- `str(x)`
  - Converts x to a string.

- `repr(x)`
  - Returns a string containing a printable representation of an object.

- `format(value[, format_spec])`
  - Formats a specified value using a format specification.

- `join(iterable)`
  - Concatenates the strings in an iterable using the original string as a separator.
'''
