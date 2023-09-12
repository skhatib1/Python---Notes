#########################
# Boolean Operators
#########################

# - True, if string "Dan" IS A SUBSTRING of "Daniel"
myBool = "Dan" in "Daniel"

# - True, if string "Dan" is NOT a substring of "Arapi"
myBool = "Dan" not in "Arapi"

a = 1
b = 2

# - True, if value of "a" is LESS THAN value of "b"
myBool = a < b

# - True, if "a" is GREATER THAN "b"
myBool = a > b

# - True, if value of "a" is LESS THAN OR EQUAL TO value of "b"
myBool = a <= b

# - True, if value of "a" is GREATER THAN OR EQUAL TO value of "b"
myBool = a >= b

# True, if value of "a" is NOT EQUAL TO vlaue of "b"
myBool = a != b

# - True, if value of "a" is EQUAL TO THE VALUE of "b"
myBool = a == b

# - True, if value of "a" points to the SAME OBJECT as value of "b"
myBool = a is b

# - True, if "a" is lesser than "b" AND "b" is greater than "a"
myBool = a < b and b > a

# - True, if "a" is lesser than "b" OR "b" is lesser than "a"
myBool = a < b or b < a

#########################
# Boolean Methods
#########################

myVariable = "This is a test."
# - True, if ALL characeters in "myVariable" are type str()
myBool = myVariable.isalpha()

# - True, if ALL characters in "myVriable" are type int()
myBool = myVariable.isdigit()

# - True, if all characters in the string are alphanumeric and there is at least one character
myBool = myVariable.isalnum()

myBool = myVariable.isspace()

# - True, is variable is an instance of a class type
myBool = isinstance(myVariable, str)
myBool = isinstance(myVariable, int)
myBool = isinstance(myVariable, float)
myBool = isinstance(myVariable, list)
myBool = isinstance(myVariable, set)
myBool = isinstance(myVariable, dict)



