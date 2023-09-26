'''string transform functions
captlize'''
comment = "good morning every one"
print(comment.capitalize())

# title
statement = "this is rajeev"
print(statement.title())

#upper
statement = "completed"
print(statement.upper())

# lower
statement = "B.tECh"
print(statement.lower())

#case fold
statement = "In two"
print(statement.lower())

#the difference between lower and case fold is in lower every char will not convert but in case fold every char will change

#swap case
a = "ThousAnd Twenty ThRee"
print(a.swapcase())

#string check functions
#isnumeric
b = "123"
print(b.isnumeric())

c = "abc"
print(c.isnumeric())

#isalnum
d = "rajEev17"
print(d.isalnum())

e = "12 3"
print((e.isalnum()))

#isdecimal
f = "10.2"
print(f.isdecimal())

g = "ac"
print(g.isdecimal())

#isdigit

h = "10"
print(h.isdecimal())

i = "ax"
print(i.isdecimal())

#is asscii
j = "AZ"
print(i.isascii())

k = "nbvjun"
print(k.isascii())

#is upper
l = "RAJEEV"
print(l.isupper())

m = "rajeev"
print(m.isupper())

# is lower
n = "sai"
print(n.islower())

o = "HYFCYD"
print(o.islower())

#isspace

p = " "
print(p.isspace())

q = "raj"
print(q.isspace())

#isidentifiers

r = "axdS"
print(r.isidentifier())

s = "%"
print(s.isidentifier())

#isprintable

o = "cadscx"
print(o.isprintable())

# istitle

p = "Rajeev Easxsa Fsxdas"
print(p.istitle())

q = "adxasc ascsdc "
print(q.istitle())
