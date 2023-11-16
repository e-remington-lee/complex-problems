from os import read
import setuptools

# run pipreqs . to get a requirements.txt file 
requirements = []

def read_lines(file):
    while True:
        data = file.readline()
        if not data:
            break
        yield data

with open("requirements.txt", "r") as f:
    for line in read_lines(f):
        requirements.append(line)

setuptools.setup(name='PersonalWebBotPy',
version='0.1',
description='A package for WebBots',
url='#',
author='R',
install_requires=requirements,
author_email='',
packages=setuptools.find_packages(),
zip_safe=False)