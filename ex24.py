print("Let's practice everything.")
print('You\'d need to know \'bout eacapes with \\ that do:')
print('\n newlines and \t tabs.') # \n换行 \t缩进

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion form intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 50
	jars = jelly_beans / 100
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point  = 10000
beans, jars, crates = secret_formula(start_point) #解包

#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)  #formula为一个list
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))