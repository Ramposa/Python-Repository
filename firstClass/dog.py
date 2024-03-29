class Dog:
  species = "Canis familiaris"
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Instance method
  def description(self):
    return f"{self.name} is {self.age} years old"

  # Another instance method
  def speak(self, sound):
    return f"{self.name} says {sound}"

class JackRusselTerrier(Dog):
  def speak(self, sound="Arf"):
    return f"{self.name} says {sound}"

class Bulldog(Dog):
  def speak(self, sound="Gruff"):
    return f"{self.name} says {sound}"