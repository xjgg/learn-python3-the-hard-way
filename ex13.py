from sys import argv   # argv: argument variable  参数变量   import the sys module
#read the WYSS section for how to run this 
script, first, second, third = argv  #打开包裹 unpack

script,first,second,third=argv
print("the script is called:",script)
print("your first variable is :",first)
print("your second variable is :",second)
print("your third variable is :",third)