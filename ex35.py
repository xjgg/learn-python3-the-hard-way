from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")
	
	choice = input("> ")
	if "0" in choice or "1" in choice:  #字符串choice中含有0或1时
		how_much = int(choice)  #字符串转换成整数
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)  #退出当前程序
	else:
		dead("You greedy bastard!")
		

def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False
	
	while True:   #无限循环，直到跳出
		choice = input("> ")
		
		if choice == "take honey": #输入的值必须完全为==右边的值才为True
			dead("The bear looks at you then slaps your face off.") #退出循环
		elif choice == "taunt bear" and not bear_moved: #True and True
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True  #重新赋值True  继续下一个循环
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:  #第二个循环输入open door时，elif为True
			gold_room()
		else:
			print("I got no idea what that means.")
#第一次输入 taunt bear时，执行第一个elif(因为是True),第二个循环继续输入taunt bear时，执行第二个elif,因为第一个elif变为False	
			
def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for you life or eat your head?")
	
	choice = input("> ")
	
	if "flee" in choice:  #字符串中含有flee即为True，可不止flee
		start()           #再从start()函数开始
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()  #其他选择时，函数内循环
		
	
def dead(why):
	print(why, "Good job!")
	exit(0)  #退出当前程序
	
def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")
	
	choice = input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room untill you strave.")
		

start()  #从start()函数开始脚本