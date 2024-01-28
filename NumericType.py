'''

- Integer Methods:
  -  int.bit_length()
     - Returns the number of bits required to represent the integer in binary,excluding sign and leading 0s .

  -  int.to_bytes(length, byteorder, *, signed=False)
     - Returns an array of bytes representing the integer.

  -  int.from_bytes(bytes, byteorder, *, signed=False)
     - 

'''
num = 16
print(num.bit_length())   # 5 (length of num in bytes)
print(num.to_bytes( 5 ,byteorder = 'big'))  # b'\x00\x00\x00\x00\x10'      (num variable's value represented by array of bytes )
print(num.from_bytes( b'\x00\x00\x00\x00\x10' , byteorder = "big"))  # 16  (num var value)

# Byteorder : The "byteorder" is like deciding if we want to start writing the code from the biggest number or the smallest number. If we use "big" byteorder, we start with the biggest number first, and if we use "little" byteorder, we start with the smallest number first.

num = 12
print(num.bit_length())   # Output: 4
# 2. Convert the integer to bytes using little-endian byte order
print(num.to_bytes(4, byteorder='little', signed=True)) # Output: b'\x0c\x00\x00\x00'
# 3. Convert the integer to bytes using big-endian byte order
print(num.to_bytes(4, byteorder='big', signed=True)) # Output: b'\x00\x00\x00\x0c'
# 4. Convert bytes back to integer using little-endian byte order
print(num.from_bytes(b'\x0c\x00\x00\x00', byteorder='little', signed=True))    # Output: 12
# 5. Convert bytes back to integer using big-endian byte order
print(num.from_bytes(b'\x0c\x00\x00\x00', byteorder='big', signed=True)) # Output: 201326592 The difference in output is due to the different byte order, which changes the interpretation of the bytes.


# The "signed" part is like deciding if the number is positive or negative.
num = -16 
print(num.bit_length())   # 5 ( as it excludes sign)
print(num.to_bytes( 5 , byteorder = 'big' , signed = True)) # By default value of signed is false 
print(num.from_bytes( b'\xff\xff\xff\xff\xf0' , byteorder = 'big' , signed = True))   # -16

#So, in simple terms, it's like deciding how to write a binary, and whether the code is for a positive or negative number.



'''

- Built-in Functions (Taking Int as Argument):
  - `abs(x)`
    - Returns the absolute value of x.( Turns -ve to +ve)

  - `divmod(dividend, divisor)`
    - Returns a tuple ( quotient , remainder) of the quotient and remainder of the division.

  -  max(n1, n2, n3, ...)        # where n1 , n2 , n3 are integers or floating values
    - Returns the largest item in an iterable or the largest of two or more arguments.

  -  min(n1, n2, n3, ...)      # where n1 , n2 , n3 are integers or floating values
    - Returns the smallest item in an iterable or the smallest of two or more arguments.

  - `pow(base, exp[, mod])`
    - Returns base to the power of exp, 
      optionally reduced by mod : Taking the remainder when divided by the modulus. This can be useful in various mathematical and programming scenarios, such as cryptography, hashing, and number theory.

  - `round(number[, ndigits])`
    -  Returns a number rounded to the nearest integer.Second   argument here, is the place after decimal upto which round off is required
'''

x = -5
print(abs(x))  # 5  coverts to +ve int if a -ve int 

print(divmod(-10 , 9))
print(-10//9 , -10 % 9)
# divmod does floor division or integer division to give quotient and remainder 
 #8 is the output as closest int multiple (towards -ve infinity) is 18 And  9*-2 = - 18;    -10 -(-18 ) = 8  ( floor division / traditional division)
 
print(-10/9) # '/' operator does floating point division to find decimal point equivalent of fraction (with remainder close to 0)
# -10/9 = -(Decimal equivalent of 10/9) = -1.1111111111111112

#The difference in quotients between divmod(-10, 9) and -10 / 9 is due to the way integer division and floating-point division handle negative numbers in Python.

print(max(22,23 , 24.5 , 23 ))   # 24.5
print(min(22.5 ,23 , 24.5 , 23 )) # 22.5


print(pow(2,3))  # 8  (same as 2*2*2)
print(pow(4,3,5))  # 4 (same as (4 * 4 * 4) % 5)

a = -32.75
print(round(a))  # -33             Round off to int
print(round(a,1))   # -32.8        Round of upto 2 decimal places
# Second argument here, is the place after decimal upto which round off is required
b = -29.846
print(abs(round(b,2)))  # 29.85
print(abs(round(b,1)))   #29.8
print(abs(round(b)))      # 30



'''
- Arithmetic Operations:
  - Addition: `a + b`
  - Subtraction: `a - b`
  - Multiplication: `a * b`
  - Division: `a / b` (returns a float in Python 3.x)
  - Floor Division: `a // b` (returns the floor of the division)
  - Modulus: `a % b` (returns the remainder)
  - Exponentiation: `a ** b`
'''

a = -10
b = 9

print(a+b) #-1
print(a*b)  # -90
print(a-b)   # -19
print(a/b)   # -1.1111111111111112( This operation gives Quotient , can be -ve)
print(a%b)   # 8 (This gives remainder , always positive )
# 8 is the output as closest int multiple (towards -ve infinity) is 18 And  9*-2 = - 18;    -10 -(-18 ) = 8  (floor division / traditional division)
print(a//b)     # -2

e , f = 4 , 1/2   
print(e**f) 
#  e , f = 4 , 1/2     shortway of calculating square root 
#  (a)^1/2 mean sqaure root 
#  (a)^-1 means reciprocal 
#  (a)^-1/2 means square root of reciprocal 
#  (a)^-2  means square of reciprocal   (in decimal)  ex- (2/5)^2 = 0.4)^2 = 0.16 )

powers = [1/2,-1/2,2,-2]
output =[]
for nums in powers :
    #output[nums]    nums is values inside power not index
    output.append(4**nums)
print(output) #[2.0, 0.5, 16, 0.0625]  





'''

- Type Conversions (From Int):
  - `float(x)`
    - Converts an integer to a floating-point number.

  - `bool(x)`
    - Converts x to a Boolean value (0 becomes False, non-zero becomes True).

  
- Type Conversions (To Int):
  - `int(x)`
    - Converts a floating point number or string of numbers(without space) to an integer.

'''

f = 0
t = 1
print(bool(f),bool(t))    # False True    integer to bool

d = -10
print(float(d))      # -10.0      int to float 
 
z = 29.0
print(int(z))    # 29 float to integer  
a = "123"
print(int(a))     # 123 string to integer
# int() can convert integer in string format ("123") and floating point ("29.0") to integer

b = False 
c = True 
print(int(b), int(c))   #0 1  bool to integer 

x = 'a'
# print(int(x))  # Error doesn't print ASCII when type converted
print(ord(x))   # ord() to find ASCII value of a alphabet



'''

 **Float Methods:**

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
  
  


- **Type Conversions (From Float):**
  - `int()`: Convert a float to an integer (truncating the decimal part).
  - `str()`: Convert a float to a string.
  - `bool()`: Convert a float to a boolean (False if the float is 0.0, True otherwise).

'''
