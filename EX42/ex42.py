## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal is a object
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal is a object
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Perosn is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person is-a object
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee is-a super and has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish is-a object
class Salmon(Fish):
    pass

## Halibut is-a fish is-a object
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet, pet is-a Satan is-a Cat
mary.pet = satan

## frank is-a employee has-a salary, salary is-a 120000
frank = Employee("Frank", 120000)

## frank has-a pet is-a rover, is-a Dog
frank.pet = rover

## flipper is-a fish
fipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
