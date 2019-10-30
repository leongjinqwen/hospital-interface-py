from hospitals import Hospital
from employees import Employee
from patients import Patient
from colorama import init
init()
from colorama import Fore, Back
import time
import os

def welcome_message(hospital):
  os.system('clear')
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  print(Fore.GREEN + f"() Welcome to {hospital.name} Hospital")
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  time.sleep(3)
  os.system('clear')

def login_to_hospital(hospital):
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  print(Fore.GREEN + "() Login To Your Account to Gain Access")
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  print('')
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  username = input(Fore.GREEN + "()() Enter you username: ")
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  password = input(Fore.GREEN + "()() Enter your password: ")
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  os.system('clear')
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  print(Fore.GREEN + "() Logging In... Please Wait...")
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  time.sleep(5)
  os.system('clear')
  user = hospital.login(username, password)
  if user:
    return user
  else:
    return False

def invalid_login(hospital):
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  print(Fore.GREEN + "() Invalid Login Credentials Provided")
  print(Fore.GREEN + "() Unable to Login User")
  print(Fore.GREEN + f"() Thank you for using {hospital.name} Hospital systems")
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  time.sleep(5)
  os.system('clear')

def valid_login(hospital, user):
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  print(Fore.GREEN + f"() Welcome back {user.position} {user.first_name} {user.last_name}")
  print(Fore.GREEN + "() What would you like to do today?")
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  time.sleep(2)

def logout(user, hospital):
  os.system('clear')
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  print(Fore.GREEN + f"() Goodbye {user.position} {user.first_name} {user.last_name}")
  print(Fore.GREEN + f"() Thank you for using {hospital.name} Hospital systems")
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  time.sleep(5)
  os.system('clear')

def auth_error():
  os.system('clear')
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  print(Fore.GREEN + "()() You are not authorized to perform this!")
  print(Fore.GREEN + "()() CONTACT ADMIN IF THIS SEEMS INCORRECT!")
  print(Fore.RED + "()()()()()()()()()()()()()()()()()")
  time.sleep(5)
  os.system('clear')


doctor1 = Employee('John', 'Smith', 'doctor1', 'superdoctor', 'Doctor')
admin = Employee('Matthew', 'Cross', 'admin', 'admin', 'Admin')
records = [{'Doctor': 'John Smith', 'Illness': 'Sore Throat', 'Prescribed': 'Asprin'}]
patient1 = Patient('1', 'Alice', 'Smith', 23, records)
hospital_patients = [patient1]
hospital_employees = [doctor1, admin]
hospital = Hospital('NEXT', 'Glomac Damansara', hospital_employees, hospital_patients)

########## DRIVER CODE ##########

##### Variables #####
logged_in = False
current_user = None

##### Program Logic #####
welcome_message(hospital)
current_user = login_to_hospital(hospital)
if current_user:
  logged_in = True
else:
  invalid_login(hospital)

while logged_in:
  valid_login(hospital, current_user)
  hospital.print_menu(current_user)
  response = int(input(Fore.MAGENTA + "Enter your response: "))
  if response == 1:
    if hospital.validate_auth(current_user ,1):
      hospital.view_patient_records()
    else:
      auth_error()
  elif response == 2:
    if hospital.validate_auth(current_user, 2):
      print('Validated!')
    else:
      auth_error()
  elif response == 3:
    if hospital.validate_auth(current_user, 3):
      print('Validated!')
    else:
      auth_error()
  elif response == 4:
    if hospital.validate_auth(current_user, 4):
      print('Validated!')
    else:
      auth_error()
  elif response == 5:
    if hospital.validate_auth(current_user, 5):
      print('Validated!')
    else:
      auth_error()
  elif response == 6:
    if hospital.validate_auth(current_user, 6):
      print('Validated!')
    else:
      auth_error()
  elif response == 7:
    if hospital.validate_auth(current_user, 7):
      print('Validated!')
    else:
      auth_error()
  elif response == 8:
    if hospital.validate_auth(current_user, 8):
      print('Validated!')
    else:
      auth_error()
  elif response == 9:
    if hospital.validate_auth(current_user, 9):
      print('Validated!')
    else:
      auth_error()
  elif response == 10:
    if hospital.validate_auth(current_user, 10):
      os.system('clear')
      print(Fore.RED + "()()()()()()()()()()()()()()()()()")
      print(Fore.RED + "()() Delete Employee Account")
      print(Fore.RED + "()()()()()()()()()()()()()()()()()")
      employee = input(Fore.GREEN + '()() Enter Employee Username: ')
      print(Fore.RED + "()()()()()()()()()()()()()()()()()")
      if employee == 'doctor1':
        os.system('clear')
        print(Fore.RED + "()()()()()()()()()()()()()()()()()")
        print(Fore.GREEN + "()() Doctor John Smith Succesfully removed!")
        print(Fore.RED + "()()()()()()()()()()()()()()()()()")
        time.sleep(3)
        os.system('clear')
      else:
        os.system('clear')
        print(Fore.RED + "()()()()()()()()()()()()()()()()()")
        print(Fore.GREEN + "()() INVALID USERNAME GIVEN TRY AGAIN!")
        print(Fore.RED + "()()()()()()()()()()()()()()()()()")
        time.sleep(3)
        os.system('clear')
    else:
      auth_error()
  elif response == 0:
    logged_in = False
    logout(current_user, hospital)


  

