#*-* coding:UTF-8 *-*
class C():
    def __init__(self,no):
        print 'init c'
        self.no=no
        print self.no
    def c(self,data):
        print 'c'
        print 'data'
        self.data=data
        print  self.data


class B(C):

    def __init__(self,no,data):
        C.__init__(self,data)
        print 'init b'
        self.no=no
        print self.no
    def b(self,data):
        print 'b'
        self.c(data)

d=B(100,'d').b(200)


class Book(object):
    def __new__(cls,a,c):
        print '__new__'
        return super(Book, cls).__new__(cls)
        #return cls

    def __init__(self,a,c):
        print '__init__'
        #super(Book, self).__init__(self)
        self.title = a
        self.detail = c

b = Book('The Django Book','hello world')
print b.title
print b.detail


class PositiveInteger(int):
    def __init__(self, value):
        super(PositiveInteger, self).__init__(self, abs(value))

i = PositiveInteger(-3)
print i


class PositiveInteger2(int):
    def __new__(cls, value):
        return super(PositiveInteger2, cls).__new__(cls, abs(value))

i = PositiveInteger2(-3)
print i