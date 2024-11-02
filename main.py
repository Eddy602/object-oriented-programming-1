     #activity 1
# class student:
#     grade=10
#     print("my name is Edward","i am in grade",grade)
# obj=student()    
       #activity 2
# class student:
#     grade=10
#     name="Edward"

#     def details(self):
#         print("my name is",self.name,"i am in grade",self.grade)
# obj1=student()
# obj1.details()       
       #activity 3
class parrot:
    species="birds"
    def __init__(self,name,age,):
        self.name= name
        self.age= age
blue=parrot("blue",8)
print("blue is a",blue.species)
print("hello i am ",blue.name,"and my age is",blue.age)

red=parrot("red",7)
print("red is a",red.species)
print("hello i am",red.name,"my age is",red.age)