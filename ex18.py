# this one is like your scripts with argv
def print_two(*args):  #def: define；函数名不能数字开头；*args即所有参数放进args这个list
	arg1,arg2=args #定义的一部分内容，缩进四个空格，参数解包
	print(f"arg1:{arg1},arg2:{arg2}") 
	
# ok, that *arg is actually pointless,we can just do this
def print_two_again(arg1,arg2):  #不需解包
	print(f"arg1:{arg1},arg2:{arg2}")

#this just takes one argument
def print_one(arg1):  #自定义函数print_one(arg1) 意思为打印参数arg1的值
	print(f"arg1:{arg1}")
#this one takes no arguments
def print_none():
	print("i got nothing.")

print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first!")
print_none()

