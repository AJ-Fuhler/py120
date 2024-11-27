class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"


# When an instance of Pine is created, what value will its type attribute have?
# Why?

# The value will be 'Pine Tree'. The reason is that when we create an instance
# of Pine, We first call the super's initializer that originally sets self.type
# to 'Generic Tree'. However, on line 8, we override self.type and set its
# value to 'Pine Tree'.