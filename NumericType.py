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


# The "signed" part is like deciding if the number is positive or negative. If it's signed, we use a special way to write down negative numbers.
num = -16 
print(num.bit_length())   # 5 ( as it excludes sign)
print(num.to_bytes( 5 , byteorder = 'big' , signed = True)) # By default value of signed is false 
print(num.from_bytes( b'\xff\xff\xff\xff\xf0' , byteorder = 'big' , signed = True))   # -16

#So, in simple terms, it's like deciding how to write a secret code made of numbers, and whether the code is for a positive or negative number.



'''

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
'''




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
# 8 is the output as closest int multiple (towards -ve infinity) is 18 And  9*-2 = - 18;    -10 -(-18 ) = 8  ( exactly like division)


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

  - `complex(real, [imag])`
    - Converts an integer to a complex number.


- Type Conversions (To Int):
  - `int(x)`
    - Converts x to an integer.

  - `bool(x)`
    - Converts x to a Boolean value (0 becomes False, non-zero becomes True).


'''