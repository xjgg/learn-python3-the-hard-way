from sys import argv

script,user_name = argv
prompt = '>'    #单引号、双引号都可

print(f"hi {user_name}, i'm the {script} script.")
print("i'd like to ask you a few questions.")
print(f"do you like me {user_name}?")
likes = input(prompt)  #input()中放入一个提示变量

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
alright, so you said {likes} about liking me.
you live in {lives}. not sure where that is.
and you have a {computer} computer. nice.
""")    #f后用三引号
