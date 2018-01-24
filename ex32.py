the_count = [1, 2, 3, 4, 5]  #list 用方括号，逗号分隔，可嵌套list
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print(f"This is count {number}")

# same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it 
for i in change:
	print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []  #新建list

# then use the range function to do 0 to 5 counts
for i in range(0, 6):  #到最后一个停止，不执行
	print(f"Adding {i} to the list.")
	#append is a function that lists understand
	elements.append(i)  #在list最后继续添加元素

# now we can print them out too
for i in elements:
	print(f"Element was: {i}")
	
#二维list：[[1,2,3],[4,5,6]]
	
