print("you are stuck in a room and there are two doors. do you go left or right?")
answer=raw_input()
if answer=="left":
	print("good choice! you left the room safely")
elif answer=="right":
	print ("oh no! you did not pick the right door! you died!")
else:
	print("please choose right or left")
