# import random
#
# food= ["cheese", "pasta","burger","pizza","sandwich"]
#
# random_index= random.randint(0, len(food)-1)
#
# print("Do you want to eat  ", food[random_index],"?")






# food= ["cheese", "pasta","burger","pizza","sandwich"]
# for counter in range (len(food)):
#     print("I want to eat ")
#     print(food[counter])




# places=["london","stockholm","brazil","mumbai","rome","japan","my bed"]
#
# def onList (item_list, list_name):
#     for item in list_name:
#         if item == item_name:
#             return True
#     return False
#
# print(onList("stockholm", places))

import random

#choices for good comments
compliment=[" wonderful!"," beautiful!"," gorgeous!"," intelligent!"," sexy!"]
random_index= random.randint(0, len(compliment)-1)

#chocies for bad comments
insult1=[" dumb ", " stupid "," absolute "," complete "," wierd "]
insult2=["hairy ", "smelly ","dirty ","ugly ","disjusting "]
insult3=["idiot ", "peanut ","blob ","trashcan ","moron "]
random_index1= random.randint(0, len(insult1)-1)
random_index2= random.randint(0, len(insult2)-1)
random_index3= random.randint(0, len(insult3)-1)

#options for a bad or good comment
input_text=input("Would you like a good comment or bad comment?:")
if input_text =="good":
    print("\r")
    print("You are so", end='')
    print(compliment[random_index])
elif input_text =="bad":
    print("\r")
    print("You are a", end='')
    print(insult1[random_index1], end='')
    print(insult2[random_index2], end='')
    print(insult3[random_index3])
else:
    print("Do you want a good or bad comment")
