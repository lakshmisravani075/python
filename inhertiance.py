#single inherentence


class person:
    def __init__(self,name):
        self.name=name
        print("hello")
class student(person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject  
    def study(self):
        print(f"{self.name} is pratcning {self.subject}")
        
        
obj1=student("sravani","maths")
obj1.study()



class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        print("this is shape")
class square(shape):
    def __init__(self,name):
        super().__init__(name)
    
    def area(self,side):
        self.side=side
        result=self.side*self.side
        print(f"{self.name} and the area is {result}")
        
    
obj1=square("square")
obj1.area(5)



class vehical:
    def __init__(self,name):
        self.name=name
    def start_engine(self):
        print("the vehical is start")
class ride(vehical):
    def __init__(self,name):
        super().__init__(name)
        print(f"{self.name} is rading on the road")
        
obj1=ride("Toyota Fortuner")
obj1.start_engine()

class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):  
        print(f"{self.name} is eating")
class mammal(Animal):
    def __init__(self,name):
        super().__init__(name)
        
    def walk(self): 
        print("  it is walking")
class Human(mammal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print(f"{self.name} is speaking")
        
        
obj1=Human("sravani")
obj1.speak()
obj1.walk()
           
        



class teacher:
    def __init__(self,name):
        self.name=name
    def teach(self,courses):
        self.courses=courses
        print(f"{self.name} is teaching {self.courses}")
class singer(teacher):
    def __init__(self,name,singing):
        super().__init__(name)
        self.singing=singing
    def sing(self):
        print(f"{self.name} is singing a song")
class person(singer):
     def __init__(self,name,singing,courses):
         super().__init__(name,singing)
         self.courses=courses
     def intro(self):   
         
         print(f"{self.name} is a teaching {self.courses} and singing {self.singing}")
         
obj1=person("sravani","songs","python")
obj1.intro()













