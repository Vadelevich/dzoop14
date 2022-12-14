import timeit
from functools import partial


class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


class PersonTest:
    __slots__ = ('name', 'address', 'email')

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


def get_set_delete(person):
    """ читает данные атрибута, записывает данные в него, удаляет его"""
    person.name = 'Olga'
    del person.name
    person.name = 'Ivan'


def main():
    person = Person("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    person_test = PersonTest("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    old = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    new = min(timeit.repeat(partial(get_set_delete, person_test), number=1000000))
    print(f"Текущая реализация: {old}")
    print(f"Тестовая реализация: {new}")
    print(f"Улучшение производительности: {(old - new) / old:.2%}")

#
# Текущая реализация: 0.23294281400740147
# Тестовая реализация: 0.1800201460137032
# Улучшение производительности: 22.72%



if __name__ == "__main__":
    main()
