from setuptools import find_packages,setup
from typing import List

xx = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if xx in requirements:
            requirements.remove(xx)

    return requirements    


setup(
name='mlproject',
version='0.0.1',
author='Aarohi',
author_email='aarohi.july@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)