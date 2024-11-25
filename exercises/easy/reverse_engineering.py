class Transform:
    def __init__(self, string):
        self._string = string

    @property
    def string(self):
        return self._string
    
    @string.setter
    def string(self, new_string):
        self._string = new_string

    def uppercase(self):
        return self.string.upper()
    
    @staticmethod
    def lowercase(str_):
        return str_.lower()
    

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz