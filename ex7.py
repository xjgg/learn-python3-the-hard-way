print("Mary had a little lamb.") #字符串用单引号或双引号皆可。不过通常单引号用在短字符串上。
print("Its fleece was white as {}.".format('snow')) # format()形式的格式化
print("And everywhere that Mary went.")
print("." * 10) #what'd that do?  #10个.:..........

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') #,end=' ' 
print(end7 + end8 + end9 + end10 + end11 + end12)