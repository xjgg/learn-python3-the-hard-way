from sys import argv
from os.path import exists # import exists()函数，以文件名字符串作为参数，判断是否存在

script,from_file, to_file = argv
print(f"copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file) #默认只读模式
indata = in_file.read() #读取文件内容，并传给变量indata

print(f"the input file is {len(indata)} bytes long")
print(f"does the output file exist?{exists(to_file)}") #判断to_file是否存在
print("ready,hit RETURN to continue, CTRL-C to abort.") #判断是否继续
input()

out_file = open(to_file,'w')  #用写入的方式打开to_file
out_file.write(indata)        #将变量值写入to_file

print("alright, all done.")

out_file.close() #close文件s
in_file.close()



#commands: python ex17.py test.txt new_file.txt


# 一行代码解决： open(to_file,'w').write(open(from_file).read())
