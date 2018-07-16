class Person(object):
    """Person class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        """Return an introduction."""
        return "Hello, my name is %s and I'm %s." % (self.name, self.age)


def main():
    bob = Person("Robert", 35)  # Create a Person instance
    joe = Person("Joseph", 17)  # Create another
    joe.sport = "football"  # Assign a new attribute to one instance

    print("Person introspection: ", dir(Person))  # Attributes of the Person class
    print("bob object introspection: ", dir(bob))
    print("joe object introspection: ", dir(joe))

    print("bob intro: ", bob.intro())
    print("intro method: ", dir(bob.intro()))


if __name__ == '__main__':
    main()
