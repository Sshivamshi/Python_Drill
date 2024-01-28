'''
- Numeric Types
  - int
  - float
  - complex

- Sequence Types
  - str
  - list
  - tuple
    - NamedTuple

- Text Type
  - str

- Set Types
  - set
    - frozenset

- Mapping Types
  - dict

- Boolean Type
  - bool

- NoneType
  - None

- Binary Types
  - bytes
  - bytearray
  - memoryview

- Collection Types
  - list
  - tuple
  - dict
  - set

- Other Built-in Types
  - range
  - slice
  - Ellipsis
  - NotImplemented

- Iterator Types
  - iter

- Generator Types
  - generator
  - coroutine

- Callable Types
  - function
  - method
  - classmethod
  - staticmethod

- Module Type
  - module

- Class Types
  - class
  - type

- Type Type
  - type

- File Types
  - file


'''




'''

- Integer Methods:
  - `bit_length()`
    - Returns the number of bits required to represent the integer.

  - `to_bytes(length, byteorder, signed=False)`
    - Returns an array of bytes representing the integer.


- Built-in Functions (Taking Int as Argument):
  - `abs(x)`
    - Returns the absolute value of x.

  - `divmod(a, b)`
    - Returns a tuple of the quotient and remainder of the division.

  - `max(iterable, *[, key, default])`
    - Returns the largest item in an iterable or the largest of two or more arguments.

  - `min(iterable, *[, key, default])`
    - Returns the smallest item in an iterable or the smallest of two or more arguments.

  - `pow(base, exp[, mod])`
    - Returns base to the power of exp, optionally reduced by mod.

  - `round(number[, ndigits])`
    - Returns a number rounded to the nearest integer.



- Arithmetic Operations:
  - Addition: `a + b`
  - Subtraction: `a - b`
  - Multiplication: `a * b`
  - Division: `a / b` (returns a float in Python 3.x)
  - Floor Division: `a // b` (returns the floor of the division)
  - Modulus: `a % b` (returns the remainder)
  - Exponentiation: `a ** b`


- Type Conversions (From Int):
  - `float(x)`
    - Converts an integer to a floating-point number.

  - `complex(real, [imag])`
    - Converts an integer to a complex number.


- Type Conversions (To Int):
  - `int(x)`
    - Converts x to an integer.

  - `bool(x)`
    - Converts x to a Boolean value (0 becomes False, non-zero becomes True).


'''
'''

- **Float Methods:**

  - `is_integer()`: Check if a float is an integer.

  - `as_integer_ratio()`: Return a pair of integers representing the numerator and denominator of the float.

  - `hex()`: Convert a float to a hexadecimal string.

  - `fromhex()`: Convert a hexadecimal string to a float.



- **Built-in Functions (Float-specific):**
  - `abs()`: Absolute value of a float.
  - `round()`: Round a float to the nearest integer.
  - `divmod()`: Quotient and remainder of the division.
  - `float()`: Convert an integer or string to a float.

-

 **Arithmetic Operations on Floats:**
  - Addition: `a + b`
  - Subtraction: `a - b`
  - Multiplication: `a * b`
  - Division: `a / b`
  - Floor Division: `a // b`
  - Modulus: `a % b`
  - Exponentiation: `a ** b`



- **Type Conversions (To Float):**
  - `int()`: Convert an integer to a float.
  - `str()`: Convert a string containing a number to a float.
  - `complex()`: Convert a complex number to a float.
  


- **Type Conversions (From Float):**
  - `int()`: Convert a float to an integer (truncating the decimal part).
  - `str()`: Convert a float to a string.
  - `bool()`: Convert a float to a boolean (False if the float is 0.0, True otherwise).

'''
