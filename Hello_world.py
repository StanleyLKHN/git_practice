from typing import Type

if __name__ == '__main__':
    # TODO FIX Bug dkdkd
    print('Hello World!')
    print('Stanley')



class Person:
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f"name: {self.name}"


def method_name():
    alex = Person("alex")
    print(alex)


method_name()

