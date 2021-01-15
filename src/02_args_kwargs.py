# function args and kwargs

def make_person(name='', age=0, place='kerala'):
    return {
        'name': name,
        'age': age,
        'place': place,
    }


p = make_person(name='ivin', age=27)

# wrong way


def make_user_bad(username='', name='', age=0, place=''):
    person = make_person(name=name, age=age, place=place)

    return {
        'username': username,
        'name': person['name'],
        'age': person['age'],
        'place': person['place'],
    }

# right way


def make_user_good(username, *args, **kwargs):
    return {
        'username': username,
        **make_person(*args, **kwargs)
    }


person = make_person(name='ivin', age=27)
user_bad = make_user_bad(username='ivin0022', name='ivin', age=27)
user_good = make_user_good('sam22', 'sam', age=27)
