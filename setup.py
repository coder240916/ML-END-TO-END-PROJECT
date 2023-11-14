from setuptools import find_packages,setup

def requirements(filename):
    with open(filename,'r') as file:
        lines = file.readlines()
        requirements = [line.replace("\n","").strip() for line in lines if "-e" not in line ]
    return requirements  

setup(
    name="DaimondPricePrediction",
    version='0.0.1',
    author='madhu',
    author_email="exaample@gmail.com",
    install_requires=requirements('requirements.txt'),
    packages=find_packages()
)
