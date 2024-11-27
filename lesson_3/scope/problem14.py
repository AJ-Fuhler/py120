class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

# Without running this code, what will happen if you were to run it? Why?

# we will raise an AttributeError. b doesn't have a var_a instance variable.
# The reason it does not is because in the B class, we override the __init__
# method and don't call super().__init__. and instead of initializing a var_a
# variable, we initialize a var_b variable.