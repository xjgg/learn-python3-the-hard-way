# close() -close the file
# read() -read the contents of the file
# readline() -read just one line of a text file
# truncate() -empty the file
# write('stuff') -write "stuff" to the file
# seek(0) -move the read/write location to the beginning of the file


from sys import argv

script, filename =argv

print(f"we're going to erase {filename}.")
print("if you don't want that, hit CTRL-C(^C).")
print("if you do want that, hit RETURE.")

input("?") #?后输入内容

print("opening the file...")
target=open(filename,'w')  #写的方式打开文件,open()默认read方式。其他： 'w'、'r'、'a'、'w+'、'r+'、'a+'

print("turncating the file. goodby!")
target.truncate()  #清空文件

print("now i'm going to ask you for three lines.")

line1=input("line 1: ") #变量赋值，用于下面的函数
line2=input("line 2: ")
line3=input("line 3: ")

print("i'm going to write these to the file.")

target.write(line1) #把input()的内容写入文件
target.write("\n") #换行符
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally,we close it.")
target.close()  #记得close文件