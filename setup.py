from setuptools import setup, find_packages

setup(
    name='simple-python-cga',
    version='0.1.0',
    author='Yahred Gastélum Velázquez',
    author_email='dr.yahred@outlook.com',
    description='Simple implementation of the compact genetic algorithm proposed by Harik et. al',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)