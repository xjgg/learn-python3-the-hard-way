cars = 100 #=给变量赋值，==确定两边是否相等；好习惯：在运算符左右留一个空格
space_in_a_car = 4.0  #_ uderscore character;4.0为floating point number
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #变量运算
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")  #文本与变量组合的字段，用，隔开
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

