class Banner:
    def __init__(self, message, width=None):
        self.message = message
        self.width = width

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])
    
    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, message):
        self._message = message
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        self._width = self._validate_width(width)
    
    def _validate_width(self, width):
        if width is None:
            return len(self.message)
        
        if not isinstance(width, int):
            raise TypeError('Width must be an integer')
        
        if width > len(self.message):
            return len(self.message)
        
        return width if width > 0 else 0


    def _empty_line(self):
        return f"| {' ' * self.width} |"

    def _horizontal_rule(self):
        return f"+-{'-' * self.width}-+"

    def _message_line(self):
        return f"| {self.message[:self.width]} |"
    
# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('To boldly go where no one has gone before.', 18)
print(banner)
# +--------------------+
# |                    |
# | To boldly go where |
# |                    |
# +--------------------+

banner = Banner('To boldly go where no one has gone before.', 1000)
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('To boldly go where no one has gone before.', 1)
print(banner)
# +---+
# |   |
# | T |
# |   |
# +---+

banner = Banner('To boldly go where no one has gone before.', -10)
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+