class A:

    def __init__(self, a):
        self.a = a
    
    @classmethod
    def copy_of(cls, a):
        return cls(a)

    @staticmethod
    def print_something():
        return 'dasdasd'

    def print_thing():
        return 'dasdasd'
        