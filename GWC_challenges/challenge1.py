############################################
# Programming Challenge 1
# Python: Variables, Conditionals, & Loops
############################################

# 1
# print "Welcome to my world!"

print ("Welcome to my world!")

# 2
# print "hey!" 7 times using a for loop
for counter in range (7):
  print ("hey")
  counter+=1

# 3
# print the numbers 1-10 using a for loop

counter=1
while counter<11:
  print(counter)
  counter+=1


# 4
# print the odd numbers between 20 and 30 using a while loop
for counter in range (20,30):
    if counter%2==0:
      print
    else:
      print (counter)
      counter+=1

# 5
# write a function that subtracts two numbers (and call the function to test it)

def subtract(number1,number2):
	print (number1-number2)
subtract(5,3)

# 6
# print all the multiples of 3 between 2 and 34 using a loop

for counter in range (2,34):
	if counter%3==0:
		print(counter
		counter+=1

# 7
# print the numbers 2-8 in order, ten times using two for loops
for counter in range (10):
	for counter in range (2,8):
		print (counter)
		counter +=1
	counter +=1

# 8
# write a function that takes in parameters

def making_soup(adj,food):
  print (("This is")+(" ")+adj+(" ") + food+(" ") +(" soup"))
making_soup ("good","chicken")


# 9
# print a list of all the numbers that are divisible by 7 that are between 22 and 62

for counter in range (22,62):
	if counter%7==0:
		print (counter)
		counter+=1

# 10
# print "yo" 14 times, each time adding one more "o" to "yo" (ex. "yo", "yoo", "yooo"...)

for counter in range (1,14):
	print ("yo")
	counter+=("o")