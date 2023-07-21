# Python code for data encapsulation

class Person:
    def __init__(self):
        self._name = ""
        self._age = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")


if __name__ == "__main__":
    person = Person()
    person.set_name("John")
    person.set_age(30)

    print("Name:", person.get_name())
    print("Age:", person.get_age())
