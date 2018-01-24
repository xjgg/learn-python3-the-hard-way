#!user/bin/python
from sys import argv

script,filename = argv  #import 文件名

txt = open(filename)  #open()函数：打开文件

print(f"here's your file {filename}:")
print(txt.read())  #txt.read()函数：打开文件，读取内容

print("type the filename again:")
file_again = input(">")  #input 文件名

txt_again = open(file_again)
print(txt_again.read())

# 在win10 的command中运行： python ex15.py  ex15_sample.txt
