#need languages.txt file

import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
	line = language_file.readline() #读取文件中的一行，并赋给line
	
	if line:                                #如果line非空，进行冒号后的内容
		print_line(line,encoding,errors) #函数嵌套，编码和解码每一行，进行打印
		return main(language_file,encoding,errors) #打印后，首尾相接，循环main函数
		
def print_line(line, encoding, errors):
	next_lang = line.strip()  #去掉readline()返回的结果中多余的\n，赋值给next_lang
	raw_bytes = next_lang.encode(encoding, errors = errors) #对next_lang的结果进行编码，赋值给raw_bytes
	cooked_string = raw_bytes.decode(encoding, errors = errors) #对编码的内容进行解码，赋值给cooked_string
	
	print(raw_bytes,"<==>",cooked_string) #打印：编码内容 <==> 解码内容
	
languages = open("languages.txt", encoding="utf-8") #用utf-8的编码方式打开文件

main(languages, encoding, error)



# win10 command 输入： python ex23.py utf-8 strict
