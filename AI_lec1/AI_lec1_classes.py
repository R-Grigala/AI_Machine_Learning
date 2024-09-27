# Almost everything in python is object, A class is a way to create your own objects
class Person:
    def __init__(self,first,last):  # constructor  this function is called every time new Person object is created
        self.first = first  # setting class attributes
        self.last = last
        self.email = first+'.'+last+'@email'

    def full_name(self):  # class method we can call it as Person.full_name(person1)
        return self.first+' '+self.last


p1=Person('irakli','gugunashvili')  # creating our class objects
p2=Person('ირაკლი','გუგუნაშვილი')

print(p1.email)  # print specific class attributes
print(p2.email)

print(p1.full_name())  # this is the 2 different ways for calling class method
print(Person.full_name(p1))   # they do the same thing
