from setuptools import find_packages,setup
from typing import List

e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if e_dot in requirements:
            requirements.remove(e_dot)
    
    return requirements

setup()
name='smartphone_valuator'
version='0.0.1'
author='Deepesh'
author_email='dsh.2065@gamil.com'
packages=find_packages()
install_requires=get_requirements('requirements.txt')
