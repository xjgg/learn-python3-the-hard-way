i = 0
numbers = []

while i < 6:
	print(f"At the top i is {i}")  #循环检查
	numbers.append(i)
	
	i = i + 1
	print("Numbers now: ", numbers)  #循环检查
	print(f"At the bottom i is {i}") #循环检查
	
print("The numbers: ")

for num in numbers:
	print(num)

# while-loop 会执行循环直到False，易死循环，可做循环检查。建议多用for循环，少用while循环
#该语句可用以下函数替换： numbers = range(0, 6)
#CTRL-C 可终止循环
