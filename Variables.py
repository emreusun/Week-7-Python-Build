# this is a comment
# this is a printh method. Print will echo out anything inside the
# () round brackets to the terminal, when we the file
print("This is my very first python script!!!")

# variables are placeholders, with dynamic values -> things that can change
# they get stored in memory and referenced later
name= "Emre"
age= 25
eyecolor= "blue"
haircolor= "brown"

# Arrays are variables on steriods. They let us store many values in one
# variable -> to help us group  data.
# This makes our scripting flies easier to understand and work it.
# car1= "Volvo"
# car2= "Toyota"
# car3= "Fiesta"
cars = ["Volvo", "Toyota", "Fiesta"]


print("My name is "+ name)
#input is anothet python "thing" - it waits with a flashing curson
#until you type somethin and hit enter
alternatename = input("What is YOUR name?")

print("My name is now" + alternatename)

print("My age is"+ str(age))