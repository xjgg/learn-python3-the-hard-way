######  implicit #######
class Parent1(object):
	
    def implicit(self):
        print("PARENT1 implicit()")

class Child1(Parent1):   #nothing new in this class, only inherit all of its behavior from class Parent
    pass    # when there is an empty block

dad = Parent1()
son = Child1()

dad.implicit()
son.implicit()  # inherit function from Parent



##### override #####
class Parent2(object):

    def override(self):
        print("PARENT2 override()")
        
class Child2(Parent2):

    def override(self):
        print("CHILD2 override()")   #Child overrides that function by defining its own version

dad = Parent2()
son = Child2()

dad.override()
son.override()  # run Child's own function



##### alter before or after #####
class Parent3(object):

    def altered(self):
        print("PARENT3 altered()")

class Child3(Parent3):

    def altered(self):
        print("CHILD3, BEFORE PARENT altered()")
        super(Child3, self).altered()   # get the Parent version function
        print("CHILD3, AFTER PARENT altered()")

dad = Parent3()
son = Child3()

dad.altered()
son.altered()


##### composition ##### user other classes and modules, except inheriting
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):  #Child and Other don't have relationship of inherence

    def __init__(self):
        self.other = Other()  # class Other() is assigned to self.other

    def implicit(self):
        self.other.implicit()  # class Other's function: implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()  #class Other's function: altered()
        print("CHILD AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

    

