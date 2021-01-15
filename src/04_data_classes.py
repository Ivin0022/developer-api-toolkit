from dataclasses import dataclass


class Person:
    def __init__(
        self,
        name='',
        age=0,
        place='kerala',
    ):
        self.name = name
        self.age = age
        self.place = place

    def __repr__(self):
        return (
            f'name = {self.name},\n'
            f'age = {self.age},\n'
            f'place = {self.place},\n'
        )

@dataclass
class Person:
    name: str
    age: int
    place: str


def make_person(name='', age=0, place='kerala') -> Person:
    return Person(name=name, age=age, place=place)


person = make_person(name='ivin', age=27)



