# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',  #州与缩写的映射
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan has: ", states['Michigan'])
print("Florida has: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])#dict嵌套，两个映射
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):  #一对元素；dict与list的转化
	print(f"{state} is abbreviated {abbrev}")
	
# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}") #嵌套

print('-' * 10)
# safely get a abbreviation by state that might not be there 
state = states.get('Texas')  #dict.get(key, default=None) 返回指定的键值，若值不存在，返回默认值

if not state:  #not state即True
	print("Sorry, no Texas.")
	
#get a city with a default value
city = cities.get('TX', 'Does Not Exist') #返回默认键值
print(f"The city for the state 'TX' is: {city}") 

#list有order，可以用cardinal number搜寻元素，dict无order，不能这样做