class Base:

    a = {
        'name': 'adsasdasd'
    }

    def something(self):
        return 'adsdads'

    def print_a(self):
        messages = {}
        for cls in reversed(self.__class__.__mro__):
            messages.update(getattr(cls, 'a', {}))
        print(messages)


class ChildMixin:

    def some_other_func(self):
        return 'dasdasd'


class Child(ChildMixin, Base):

    a = {
        'age': 10
    }
    def somthing(self):
        return super().a() 

    


class Sam(Child):
    """
    docstring
    """
    a = {
        'DOB': 10
    }
