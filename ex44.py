# "inheritance" lets you put a common functionality in the parent class and all child classes will inherit it
# class Foo(Bar) creates class Foo that inherits from Bar; so you can put specifics on Foo and common things on Bar

# there are three ways in which parent and child classes can interact

# 1, implicit inheritance
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit() # although implicit FUNCTION is not defined in child class, it inherits it implicitly from parent

# 2, explicit override
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):
    
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override() # child class created a FUNCTION with the same name as the one on parent, so it overrides it (innermost/local scope overrides outer scope)

# 3, alter before or after
class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered() # calling super function with Foo parameter means "call bar() method from the class that is the parent of Foo" 
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# all three combined
class Parent(object):

    def override(self):
        print("PARENT override()")
        
    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

# multiple inheritance and MRO
# problem if one class inherits from more than one parent; in this case, Python has to look up the possible function in the class hierarchy
# this is done using method resolution order (MRO) and an algorithm called C3
# you use super() FUNCTION to help finding the right function; most common use is with __init__ functions in base classes
# Zed: "this is usually the only place where you need to do some things in a child, then complete the initialization in the parent"
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

# another way to do the same thing as in inheritance is COMPOSITION
# instead of writing new code to REPLACE (explicit override) or ALTER (super()) you can call functions in a module
class Other(object):

    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

# PROBLEM: you don't want to have duplicated code all over the software; both INHERITANCE and COMPOSITION solve it
# I by creating implied features, C by giving modules and capacity to call functions in other classes