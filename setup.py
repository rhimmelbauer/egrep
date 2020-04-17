from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='egrep',
    version='0.0.1',
    author='Roberto Himmelbauer',
    author_email='robertoh89@gmail.com',
    description='A simple library for exectuing egrep linux commando to files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sean-mcclure/datapeek_py',
    license='MIT',
    packages=['egrep'],
    zip_safe=False
)