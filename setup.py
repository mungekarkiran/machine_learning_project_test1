from setuptools  import find_packages, setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    '''
    Description : This function is going to return list of requirement 
    mention in requirements.txt file.

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file.
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