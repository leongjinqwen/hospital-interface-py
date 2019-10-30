class Employee():
  def __init__(self, first_name, last_name, username, password, position):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.password = password
    self.position = position

  def check_password(self, password):
    if self.__validate_password(password):
      return True
    else:
      return False

  def __validate_password(self, password):
    if self.password == password:
      return True
    else:
      return False