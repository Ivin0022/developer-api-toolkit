from collections import namedtuple
from types import SimpleNamespace

# return value

# named tuple
Person = namedtuple('Person', ['name', 'age', 'place'])


def make_person_with_tuple(name='', age=0, place='kerala'):

    # do somthing

    return Person(name, age, place)


person_tuple = make_person_with_tuple(name='ivin', age=27)

t_name = person_tuple.name
t_age = person_tuple.age
t_place = person_tuple.place

# NameSpace


def make_person_with_ns(name='', age=0, place='kerala'):
    return SimpleNamespace(name=name, age=age, place=place)


person_ns = make_person_with_ns(name='ivin', age=27)

ns_name = person_ns.name
ns_age = person_ns.age
ns_place = person_ns.place
