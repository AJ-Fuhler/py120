What is the method resolution order and why is it important?

The method resolution order is the way that Python looks for Methods when a
method is called on an object. First it looks in the class that the object is
an instance of. If it finds it there, it will use that method. If not, it will
look for any classes that the first class inherited from. If there are mutliple
classes that the class inherited from, it will sequentially look through those
classes based on the order provided in the first class' definition. Inside each
inhertited class, Python will recursively look through that class, whether it
inherited from any other classes and look there for the method as well.
Eventually, if it hasn't found any method yet after sequentially going through
all those classes, Python will look in the 'object' class. This is the class
that every class inherits from. If it doesn't find it there, it will raise an
AttributeError. You can use the mro() class method to determine the mro for a
class' method resolution order. It return a list of all classes it will look
through sequentially.

print(Bulldog.mro())
# [<class '__main__.Bulldog'>, <class '__main__.Dog'>, <class
# '__main__.Pet'>, <class 'object'>]

a more readable way would be to use a list comprehension and only print out the
class names:

print([ cls.__name__ for cls in Bulldog.mro() ])
# ['Bulldog', 'Dog', 'Pet', 'object']