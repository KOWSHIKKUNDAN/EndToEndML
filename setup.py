from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    # Gets requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
        
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Kowshik',
    author_email='kkk13@iitbbs.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)