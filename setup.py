from setuptools  import find_packages, setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    '''
    Description : 

    return 
    '''
    with open(REQUIREMENT_FILE_NAME) as REQUIREMENT_FILE:
        return REQUIREMENT_FILE.readlines().remove('-e .')

setup(
    name = "housing_predictor",
    version = "0.0.3",
    author = "Kiran K. Mungekar",
    description = "This is first CI/CD ML Project",
    packages = find_packages(), # ['housing'],
    install_requires = get_requirements_list()
)