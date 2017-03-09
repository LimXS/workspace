class hello(object):
    x = 11
    def __init__(self, _x):
        self._x = _x
        print("hello.__init__")

    def haha(self):
        print "haha self"

    @classmethod
    def class_method(cls):
        print("class_method")
        #cls(1).haha(3)

  
    @staticmethod
    def static_method():
        print("static_method")
        #hello.haha()
        #hello(2342).haha(2234)
        #return 42




  
    @classmethod
    def getPt(cls):
        cls.class_method()
        cls.static_method()

class child(hello):
    def chfun(self):
        print

if "__main__" == __name__:

    print "child......................."
    #print child.getPt()

    ch=child(100)
    print ch.class_method()
    print child.class_method()
    #print child.haha()
    #print ch.haha(33242)








print "..........................................."

from random import choice
COLORS = ['Brown','Black','Golden']

class Animal(object):

    def __init__(self,color):
        self.color = color

    @classmethod
    def make_baby(cls):
        color = choice(COLORS)
        print cls
        return cls(color)

    @staticmethod
    def speak():
        print 'Rora'

class Dog(Animal):

    @staticmethod
    def speak():
        print "Bark!"

    @classmethod
    def make_baby(cls):
        print "making dog baby!"
        print cls
        return super(Dog,cls).make_baby()

class Cat(Animal):
    pass

d = Dog('Brown')
print d.color
pup = d.make_baby()

print pup.color