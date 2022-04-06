'''class MyClass:
    x=5;
    print(MyClass)'''
    
    #Objects
    
    '''class MyClass:
        x=5
        p1 = MyClass()
        print(p1.x)
'''

#The __init__() Function

class Person:
    def __init__(safe, name, age):
        safe.name = name
        safe.age = age
    p1 = Person('John', 36)
    
    print(p1.name)
    print(p1.age)
    
    #Object Methods
    class Person:
      def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
