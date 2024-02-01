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

- `count(sub[, start[, end]])`
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

### Operations on Strings:

- Concatenation: `s1 + s2`

- Repetition: `s * n` (repeats the string s n times)

### Type Conversions (From String):

- `int(s[, base])`
  - Converts a string to an integer with an optional base for interpreting the string.

- `float(s)`
  - Converts a string to a floating-point number.

- `bool(s)`
  - Converts a string to a Boolean value.

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
