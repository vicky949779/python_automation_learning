import sys

''' ### output is print liside of list ### '''
# sys.path.append('07_functions') # it will add your coustem python file to as package directory
sys.path.insert(1,'07_functions') # This will insert the directory into the package with index position
print(sys.path) # these are the directory Pyhton interpreters reading for the modules and packages. below the package details
# ['/home/vicky/python_automation_learning/08_modules_packages', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/home/vicky/py_venv/py_automation_env/lib/python3.10/site-packages']

''' now you add your local package '''
from password_gen import user_cmd_gen # type: ignore

print(user_cmd_gen("just_try",100))