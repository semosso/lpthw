## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    #SD 3: def test(self):
        #print("teste SD 3 - ANIMAL")
    pass

## ?? DOG IS-A ANIMAL
class Dog(Animal):

    def __init__(self, name):
        ## DOG HAS-NAME
        self.name = name
 # still have to figure out reason behind __init__; does this mean that class will not be instantiated without receiving name param?
 # maybe, but not like I was thinking; it seems to be that init function takes self and NAME parameter
 # SO: __init__ is the constructor in Python; when you instantiate the class, Python creates an object and passes it to __init__
 # Python doc: Called after the instance has been created, but before it is returned to the caller


## ?? CAT IS-A ANIMAL
class Cat(Animal):

    def __init__(self, name):
        ## ?? CAT HAS-A NAME
        self.name = name
    def teste(self):
        print("teste SD 3 - CAT")

## ?? PERSON IS-A OBJECT
class Person(object):

    def __init__(self, name):
        ## ?? PERSON HAS-A NAME
        self.name = name

        ##? PERSON HAS-A PET
        self.pet = None # i.e., object of the Person class may have a pet attribute, but not set yet?

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name) # WHAT does this do?
        ## ??
        self.salary = salary

# super() function: 1, with single inheritance; 2, with multiple inheritance (one class inheriting attributes from more than one parent class)
# 1: allows you to call the init of the parent class without having to repeat its name
# 2: python uses MRO (method resolution order) to define order in which it inherits methods from parents (first named comes first; derived calls before those of base class)
## see Evernote from 1/12/2019


## ?? 
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover") # this INSTANTIATES the class, i.e., creates an object from the class

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

# ??
mary.pet = satan # seems to answer my question from oop_test/ex 41: from MARY object, find the PET attribute and set it to satan (which is itself an object from class Cat)

## ??
frank = Employee("Frank", 120000)

# ??
frank.pet = rover

## ??
flipper = Fish()

## ?? 
crouse = Salmon()

## ?? 
harry = Halibut()

# SD 3: what happens when functions are in a "base class" and not in the specific class?
satan.teste() # if I have functions of the same name in both base and specific, only calls specific; if I don't have anything in specific but have in base, calls base
# i.e., child class inherits methods and attributes from parent clas

# TESTE: if object from specific class doesn't have an attribute from main class, and I try to get it? what happens?
frank.pet() # exception that NONEtype is not callable

# SD 5 and 6: make new relationships that are lists and dicts so you can also have "has-many" relationships? What about is-many? read about multiple inheritance