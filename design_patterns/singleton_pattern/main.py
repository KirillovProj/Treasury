from .singleton import SingleObject

one = SingleObject()
two = SingleObject()
three = SingleObject()

print(id(one))
print(id(two))
print(id(three))

one.do_something()
two.do_something()
three.do_something()

print(one.counter)
print(two.counter)
print(three.counter)
