# it will find all the packages in the MAchine Learning 
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

# get_requirements function to install the libraries
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirement 
    """
    requirements=[]

    # requirement mein hr line ke baad \n aayega usko bhi handle kr lenge
    with open(file_path) as file_obj:
      requirements = file_obj.readlines()
      requirements=[req.replace('\n','') for req in requirements]
      if HYPEN_E_DOT in requirements:
         requirements.remove(HYPEN_E_DOT)
    return requirements 




# we are setting the setup here  

setup(
    name='ML_Project',
    version='0.0.1',
    author='Aakash_modi',
    author_email='aakashgpt11@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)