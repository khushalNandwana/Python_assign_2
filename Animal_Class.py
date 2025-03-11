class Animal:
    def __init__(self, name, sound):
        self.name=name
        self.sound=sound
    def make_sound(self):
        return(f"{self.name} making the {self.sound}")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "bark")
class Cat(Animal):
    def __init__(self, name, ):
        super().__init__(name, "Meow")
dog_class=Dog("peter")
print(dog_class.make_sound())

cat_class=Cat("kitty")
print(cat_class.make_sound())

