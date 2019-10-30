import random

class Patient():
  def __init__(self, p_id, first_name, last_name, age, records=[]):
    self.id = p_id
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.records = records