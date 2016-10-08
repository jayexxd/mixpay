import pip
from subprocess import call

for dependency in pip.get_installed_distributions():
    call("pip install -U " + dependency.project_name, shell=True)

call("pip freeze > requirements.txt", shell=True)
print(All done.) 
