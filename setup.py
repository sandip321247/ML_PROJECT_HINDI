from setuptools import find_packages, setup
from typing import List
#Declaring variables for setup functions
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements








setup(
    name = 'ml_project_hindi',
    author='sandip behera',
    version='0.0.1',
    gmail='sandipbehera321@gmail.com',
    package = find_packages(),
    install_requires = get_requirements('requirements.txt')
#get_requirements('requirements.txt') will return a 'list' of requirements after reading the requirements.txt file
)