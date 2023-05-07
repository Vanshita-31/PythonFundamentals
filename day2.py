import keyword
print(True+True)
# print(True/False)
print(False/True)
# Reserved keywords in python
keyword.kwlist
print(keyword.kwlist)
x = 10
y = 10
print(type(x))
print(id(x))
print(id(y))
x = 12345
# Converting binary to decimal
x = 0B1111
print(x)
print(type(x))
# Converting octal to decimal
x = 0o123
print(x)
print(type(x))
# Converting hexadecimal to decimal
x = 0x123face
print(x)
print(type(x))
# Converting decimal to binary
x = bin(15)
print(x)
print(type(x))
# Converting decimal to octal
x = oct(83)
print(x)
print(type(x))
# Converting decimal to hexadecimal
x = hex(19135182)
print(x)
print(type(x))
# float datatype
# exponential form / scientific notation
f = 1.2e4
print(f)
print(type(f))

# complex number
a = 3+5j
print(type(a))
b = 3.7+5.9j
print(b)
# we can perform arithmetic operations on complex numbers
print(a+b)
print(b.real)  # extracting real from complex number
print(b.imag)   # extracting img from complex number
