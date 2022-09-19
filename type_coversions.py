# " integer can convert  into both float and string"
a=2
print(float(a))        #adding point values
print(str(a))          #same as input
#" float can convert  into both int and string"
b=2.8
print(float(b))        #ignore point values
print(str(b))          #same as input
#" string can convert  into both int and float when string contain int values"
c="5"
print(int(c))
print(float(c))
#"when str contain float value we cannot convert directly in int first we have to convert into float"
d="5.8"
e=float(d)
print(e)
print(int(e))
