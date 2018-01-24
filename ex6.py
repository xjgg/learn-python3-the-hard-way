types_of_people = 10
x = f"There are {types_of_people} types of people." #变量赋值

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)  #打印变量
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'") #单引号只是个符号，不影响变量的格式化

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious)) #另一种形式的格式化

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)