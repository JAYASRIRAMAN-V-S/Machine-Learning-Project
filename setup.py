from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the List of requirements
    '''
    requirements = []

    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Machine-Learning-Project',

    version='0.0.1',

    author='Jaya Sri Raman',

    author_email = 'jayasriraman2003@gmail.com',

    packages=find_packages(),

    install_requires= get_requirements('requirements.txt'),
)