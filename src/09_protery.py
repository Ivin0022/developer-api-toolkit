class Person:

    def __init__(
        self,
        first_name='',
        last_name='',
        age=0,
        place='kerala',
    ):
        self._first_name = first_name
        self.last_name = last_name
        self.age = age
        self.place = place

    @property
    def first_name(self):
        return self._first_name + self.last_name

    @first_name.setter
    def first_name(self, val):
        self._first_name  = val


p =Person()

a = p.first_name
b = p.last_name