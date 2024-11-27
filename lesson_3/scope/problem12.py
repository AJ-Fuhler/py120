class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound()) # roar

# since we called make_sound with Lion as the caller, cls is the Lion class.
# The return value will be the value of Lion.sound