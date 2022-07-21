#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".

var_int = 1234
print(4-(var_int % 10 % 2 + var_int // 10 % 10 % 2 + var_int // 100 % 10 % 2 + var_int // 1000 % 10 % 2))