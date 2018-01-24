formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4)) #把四个参数值通过函数format()传到formatter里
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter,formatter)) #不要少括号
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))