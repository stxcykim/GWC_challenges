print ("Welcome to the MOM MADNESS GAME!")
print ("You just woke up in your room. You came back home SUPER LATE and night before and your mom knows.")
print("Will your try to deal with your mother or will you attempt to escape her fiery wrath? There is a door and window in your room.How will you leave your room?")


input_text=input("Type door or window and press enter:")
if input_text== "door":
    print("UH OH! your mother is waiting outside of your room.")
elif input_text=="window":
    print("GOOD TRY! Your mom knew your plan and is waiting outside the house")
else:
    print("come on. You can't avoid this... it's either the door or window. Which one?")


print("Your mother is furious! She becomes so triggered that her superpower comes out... THE NAGGING! Will you nag back at her? Or will you try to distract her with a compliment?")


plan=input("type in compliment or nag and press enter:")
if plan=="compliment":
    print()
elif plan =="nag":
    print("OH NO! Your mom sees you giving her an attitude and NAGS YOU TO DEATH!")
else:
    print("come on... you need to do something. Nag or compliment?")


print("Do you want to fight them, or run away?")


decision=input("Type in runaway or fight and press enter:")
if decision== "fight":
    print("lol... you really thought you could fight them? You're funny. Sorry you died.")
if decision=="runaway":
    print("good move! They would've killed you if you didn't runaway")

print()
