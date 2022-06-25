
class Dog:
  def __init__(self, name, age, friendliness) -> None:
    self.name = name
    self.age = age
    self.friendliness = friendliness
  
  def likes_walk(self):
    return True

class Samoyed(Dog):
  def __init__(self, name, age, friendliness) -> None:
    super().__init__(name, age, friendliness)

class Poodle(Dog):
  def __init__(self, name, age, friendliness) -> None:
    super().__init__(name, age, friendliness)
    
  def shedding_amount(self):
    return 2

class GoldenRetriver(Dog):
  def __init__(self, name, age, friendliness) -> None:
    super().__init__(name, age, friendliness)
    
  def fetch_ability(self):
    if self.age < 2:
      return 8
    elif self.age < 10:
      return 10
    else:
      return 7

class GoldenDoodle(Poodle, GoldenRetriver):
  def __init__(self, name, age, friendliness) -> None:
    super().__init__(name, age, friendliness)
    
# sammy = Samoyed('sammy', 2, 10)
# print(sammy.name, sammy.age, sammy.friendliness)
# print(sammy.likes_walk())

goldie = GoldenDoodle('goldie', 1, 10)
print(goldie.name, goldie.age, goldie.friendliness)
print(goldie.likes_walk())