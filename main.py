import json
from os import path

friendList = []
filename  = 'friends.json'

#check existing if not create new
if path.isfile(filename) is False:
	#raise Exception("filenotfound")
	with open(filename,'w') as file:
		json.dump(friendList,file)
		print("Created : Success\n")


def strt():
	#load the json file to friendList
	with open(filename) as file:
		friendList = json.load(file)

	print("friends: "+ str(len(friendList)))	
	print("\nEnter 1 add friend")
	print("Enter 2: view friend")
	print("Enter 3: delete friend")
	print("Enter 4: Exit")

	n = int(input("\nEnter your pick\n"))

	if n == 1:
		add()
	elif n == 2:
		view(0)
	elif n == 3:
		delete()
	elif n == 4:
		quit()

	else:
		print("out of range\n\n\n")
		strt()


#view friendList
def view(chck):
	if chck == 0:
		print("Friends:" + str(len(friendList)))
		for i in range(len(friendList)):
			print(str((i+1)) +" : "+friendList[i]['name'])
		
		strt()
	elif chck ==1:
		print("Friends:" + str(len(friendList)))
		for i in range(len(friendList)):
			print(str((i+1)) +" : "+friendList[i]['name'])
		
#delete a friend from friendList
def delete():
	view(1)
	n = int(input("\n Enter The Count Of The Person\n"))
	if n < len(friendList):
		friendList.pop(n)

	#dump all the list unto JSON
	with open(filename,'w') as file:
		json.dump(friendList, file, indent=4, separators=(',',':'))
		print("removed: :)")
	strt()
	
#add friend
def add():
	name = input("name: ")
	age = input("age: ")
	F_color = input("favorite movie: ")
	F_movie = input("favorite movie: ")
	mobileN= input("mobile number: ")
	motto= input("motto: ")

	#append to the List
	friendList.append( {
		'name' : name,
		'age'	: age,
		'favorite_color' :F_color,
		'favorite_movie' :F_movie,
		'mobile_number'	: mobileN,
		'motto'	: motto
	})

	#dump all the list unto JSON
	with open(filename,'w') as file:
		json.dump(friendList, file, indent=4, separators=(',',':'))
		print("added friend")
	
	print("\n\n\n")
	strt()

if __name__ == "__main__":
	strt()
