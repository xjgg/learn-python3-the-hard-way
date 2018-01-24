# "I am 6'2\" tall." (escape double-qoute inside string)
# 'I am 6\'2" tall.' (escape single-quote inside string)
# eacape sequence 转义符：

tabby_cat = "\tI'm tabbed in." #\t 缩进
persian_cat = "I'm split\non a line." # \n 换行
backslash_cat = "I'm \\ a \\ cat." #\\返回一个\

fat_cat = """   
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""                      # 三个单引号也可

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)