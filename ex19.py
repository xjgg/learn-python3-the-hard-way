#函数中的变量和脚本中的变量不同
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print(f"you have {cheese_count} cheese !")
	print(f"you have {boxes_of_crackers} boxes of crackers!")
	print("man that's enough for a party!")
	print("get a blanket.\n")
	
print("we can just give the function numbers directly:")
cheese_and_crackers(20,30) #在函数直接赋值

print("or,we can use variables from our script:")
amount_of_cheese=10  
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers) #在函数中使用临时变量

print("we can even do math inside too:")
cheese_and_crackers(10+20,5+6)   #在函数中做计算

print("and we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers) #混合使用

#函数中的值可以是直接的数字、变量、可混合计算数字和变量

