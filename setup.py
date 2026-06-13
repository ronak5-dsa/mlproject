from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]: ## this is the function reads and installs all the dependencies present in requirement.txt
    requirements=[] # empty list , (file_path:str)->List[str] means input is file path in form of string output would be list of string(all the libraries)
    with open(file_path) as file_obj:

       requirements= file_obj.readlines
       requirements=[req.replace("\n","") for req in requirements]

       if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)

       return requirements
   



setup(
    name='mlproject', ## this is metadata information, setup.py provides metdata info about project
    version='0.0.1',
    author='Ronak',
    author_email='raunaksharma192005@gmail.com',
    install_requires=get_requirements('requirements.txt'), 
    packages=find_packages()
)