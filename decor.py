

'''
Decorator example
'''

class ClassName():
    """
    docstring for Decorator
    """

    def __init__(self, arg, another):
        self.arg = arg
        self.another = another

    def deco(foo):
        def innerdeco(self):
            print('before addfunc call ', foo.__name__)
            print(f'arg {self.arg} + another {self.another} = ', self.arg + self.another)
            foo(self)
            print('My mobile number is : ', self.number)
            print('After addfunc call ', foo.__name__)
        return innerdeco

    @deco
    def addfunc(self):
        self.text = "This is addfunc data"
        self.number = 9849156722
        return self.text, self.number

cobj = ClassName(30, 40)
cobj.addfunc()
