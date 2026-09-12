# Function for addition
def add(num1,num2):
  sum=num1+num2
  return sum

# Function for subtraction
def subtract(num1,num2):
  subtracted_value=num1-num2
  return subtracted_value

#Function for multiplication
def multiply(num1,num2):
  multiplied_value=num1*num2
  return multiplied_value

#Function for division
def divide(num1,num2):
  divided_value=num1/num2
  return divided_value

print("Welcome to the calculator!")
print()
# Storing the 2 numbers as variables using input()
num1=int(input("Choose a number:"))
num2=int(input("Choose another number:"))

#Showing calculator menu
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")
option = int(input("Select an option from above:"))

# while True keeps the loop running until 5 is entered and break stops it
while True:              
#Conditional statements for menu options
  if option==1:
    print(add(num1,num2))
  elif option==2:
    print(subtract(num1,num2))
  elif option==3:
    print(multiply(num1,num2))
  elif option==4:
    print(divide(num1,num2))
  elif option==5:
    print("Bye bye!")
    break
  #Considering other cases
  else:
    print("Choose a valid option number.")

  print()
  num1=int(input("Choose a number:"))
  num2=int(input("Choose another number:"))
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Exit")
  option = int(input("Select an option from above:"))

  
 


