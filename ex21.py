def add(a,b):
	print(f"ADDING {a}+{b}") #print返回引号中的内容，不做计算
	return a+b  #返回a+b的计算结果

def subtract(a,b):
	print(f"SUBTRACTING {a}-{b}")
	return a-b
	
def multiply(a,b):
	print(f"MULTIPLYING {a}*{b}")
	return a*b

def divide(a,b):
	print(f"DIVIDING {a}/{b}")
	return a/b

print("let's do some math with just functions!")

age = add(30,5)   # 打印内容，并把返回的函数值赋给变量
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print(f"age:{age}, height:{height}, weight:{weight}, IQ:{iq}" )

# a puzzle for the extra credit, type it in anyway.
print("here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2)))) #用函数创建一个公式。从里到外打印内容，并计算值、赋值给变量

print("that becomes:",what,"can you do it by hand?")


#用输入的值做计算必须用：int(input()) or  float(input())


