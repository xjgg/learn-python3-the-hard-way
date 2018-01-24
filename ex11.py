print("How old are you?", end=' ')  #end=' ' : not end the line with a newline character and go to the next line
age = input()
print("How tall are you?", end=' ')  # 输入的都是字符串，如果想转成可计算的数字，需 int(input())
height = input()
print("How much do you weight?", end=' ')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")