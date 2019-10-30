from employees import Employee
from colorama import init
init()
from colorama import Fore
import os
# from patients import Patient

class Hospital():
  auth_level = {
    'Admin': [1,2,3,4,5,6,7,8,9,10,0],
    'Doctor': [1,2,3,4,5,6,7,0],
    'Nurse': [1,2,3,5,6,0],
    'Patient': [1,0]
  }
  options = {
    1: 'View Patient Records',
    2: 'View All Patients',
    3: 'Add New Patient',
    4: 'Delete Patient',
    5: 'View All Patients Records',
    6: 'Add Patient Records',
    7: 'Delete Patient',
    8: 'View All Employees',
    9: 'Add Employee',
    10: 'Delete Employee',
    0: 'Logout'
  }
  def __init__(self, name, address, employees=[], patients=[]):
    self.name = name
    self.address = address
    self.employees = employees
    self.patients = patients

  def login(self, username, password):
    current_user = None
    for employee in self.employees:
      if employee.username == username:
        if employee.check_password(password):
          current_user = employee
    return current_user

  def print_menu(self, user):
    menu_options = []
    if user.position == 'Admin':
      menu_options = self.auth_level['Admin']
    elif user.position == 'Doctor':
      menu_options = self.auth_level['Doctor']
    elif user.position == 'Nurse':
      menu_options = self.auth_level['Nurse']
    elif user.position == 'Patient':
      menu_options = self.auth_level['Patient']

    print(Fore.RED + "()()()()()()()()()()()()()()()()()")
    for option in menu_options:
      print(Fore.MAGENTA + f"()() {option}. {self.options[option]}")
    print(Fore.RED + "()()()()()()()()()()()()()()()()()")

  def validate_auth(self, user, response):
    if response in self.auth_level[user.position]:
      return True
    else:
      return False

  def view_patient_records(self):
    os.system('clear')
    print(Fore.RED + "()()()()()()()()()()()()()()()()()")
    print(Fore.RED + "()() View Patient Records")
    print(Fore.RED + "()()()()()()()()()()()()()()()()()")
    patient_number = input(Fore.GREEN + '()() Enter Patient ID No: ')
    print(Fore.RED + "()()()()()()()()()()()()()()()()()")
    for patient in self.patients:
      if patient.id == patient_number:
        print(Fore.RED + "()()()()()()()()()()()()()()()()()")
        print(Fore.CYAN + f'Records for Patient {patient.id} - {patient.first_name} {patient.last_name}')
        print(Fore.RED + "()()()()()()()()()()()()()()()()()")
        for record in patient.records:
          print('')
          print(Fore.CYAN + f"() Record No: {patient.records.index(record) + 1}")
          print(Fore.CYAN + f"() Doctor Seen: {record['Doctor']}")
          print(Fore.CYAN + f"() Illness: {record['Illness']}")
          print(Fore.CYAN + f"() Medicine Prescribed: {record['Prescribed']}")
          print(Fore.CYAN + f"() ====================================== ")
    continue_program = False
    while not continue_program:
      print(Fore.RED + "()()()()()()()()()()()()()()()()()")
      response = input(Fore.GREEN + 'Would you like to return to main menu? (y/n) ').lower()
      if response == 'y':
        continue_program = True
        os.system('clear')

    

