from setuptools import find_packages, setup
from typing import List

HYPHEN_E_NOT = '-e .'


def get_requirements(file_path: str) -> List[str]:

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_NOT in requirements:
            requirements.remove(HYPHEN_E_NOT)
    return requirements


setup(
    name='MLPROJECT',
    version='0.0.1',
    author='Rahbar',
    author_email='rahbareazam033@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
