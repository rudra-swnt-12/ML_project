from setuptools import setup, find_packages
from typing import List

HYPEN_REQUIREMENT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    Reads the requirements file and returns a list of requirements.
    """
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
    # Remove any whitespace characters like `\n` at the end of each line
    requirements = [req.strip() for req in requirements if req.strip()]
    # -e . is used for local development, it allows you to install the package in editable mode.
    if HYPEN_REQUIREMENT in requirements:
        requirements.remove(HYPEN_REQUIREMENT)
    return requirements 

setup(
    name='ML_project',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements(file_path='requirements.txt'),
    entry_points={
        'console_scripts': [
            'run_model=src.main:main',
        ],
    },
    package_data={
        'src': ['data/*.csv', 'models/*.pkl'],
    },
    author='Rudra Sawant',
    author_email='rudra.vksawnt@gmail.com'
)