ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') #用split函数拆分字符串
more_stuff = ["Day", "Night", "Song", "Frisbee",
				"Corn", "Banana", "Girl", "Boy"]  #可换行写

while len(stuff) != 10:
	next_one = more_stuff.pop() #选list中最后一个
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")
	
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) #list中第二个
print(stuff[-1]) #whoa! fancy  list中倒数第一个
print(stuff.pop())
print(' ' .join(stuff)) #what? cool! 用' '连接stuff
print('#'.join(stuff[3:5])) #super stellar! 从listh中提取第3到第5个元素