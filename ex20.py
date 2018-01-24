from sys import argv

script, input_file =argv

def print_all(f):  #定义函数：打印读取的文件内容; f: file 参数为文件
	print(f.read())  #读取完文件后，“指针”在文件内容最后。
	
def rewind(f):     #定义函数：move the file to the 0 byte.或理解为“指针”移到文件开始
	f.seek(0)
	
def print_a_line(line_count,f):   #打印两个参数：行数、行内容，行数和行内容无关
	print(line_count,f.readline()) # 去掉增加的\n: print(line_count,f.readline(),end = '') 引号内有空格的话，会返回空格
	
current_file = open(input_file)  #变量赋值：打开文件

print("first let's print the whole file:\n") #增加一个回车

print_all(current_file)  #打印读取的打开文件

print("now let's rewind, kind of like a tape.")

rewind(current_file)  #

print("let's print three lines:")

current_line=1
print_a_line(current_line,current_file)  #打印当前行数和行内容,“指针”停在句尾的\n后面，返回行内容和一个\n

current_line=current_line+1  #增加行数值 等同于 current_line += 1
print_a_line(current_line,current_file)  #从上次“指针”所在的位置继续读取一行

current_line=current_line+1
print_a_line(current_line,current_file)



