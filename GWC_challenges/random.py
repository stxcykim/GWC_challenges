import random

input_name=input("What is your name?:")

verb=["is running","is sleeping","is dying"]
random_index=random.randint(0,2)

place=["in the movies","in the gym","at the beach"]
random_index1=random.int(0,2)


print("\r")
print (input_name, end='')
print(verb[random_index])
