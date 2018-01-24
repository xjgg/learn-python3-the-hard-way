# Here's some new strange stuff, remember type it exactly.
#两种字符串多行显示的方法：\n  和""" """

days = "Mon Tue Wen Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
months2 = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)
print("Here are the months: ", months2)

print("""
There's something going on there.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""") #三个引号互相之间无空格。两个三引号之间可写多行
