#String is set of characters written in  the 
  #..Double our single quotes ,Even we can use the triple
  # ...Quotes but used for multiple line systems
  # python String indexing started from -->0
  #In python We can access the indexing from End also 
  #   A  M  A  N
  #   0  1  2  3
  #  -4,-3,-2,-1      
fruit="Apple"
veg="potato"

print(fruit[-2])

br=fruit+veg
print(br)

#slicing of string
#python Fuctions for strings
#1)isalpha()
#2)isdigit()
#3)islower()
#4)isupper()
#5)lower()
#6)upper()
#7)lstrip()
#8)rstrip()

s="  abcde   "
print('s.isalpha',s.isalpha())
print('s.isdigit',s.isdigit())
print('s.islower',s.islower())
print('s.isupper',s.isupper())

print('s.upper:',s.upper())
print('s.lstrip:',s.lstrip())
print('s.rstrip:',s.rstrip())


