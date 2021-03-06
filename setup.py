from setuptools import setup, find_packages

setup(name='perseuspy',
        version='0.1',
        description='Utilities for integrating python scripts into Perseus workflows',
        url='http://www.github.com/jdrudolph/perseuspy',
        author='Jan Rudolph',
        author_email='jan.daniel.rudolph@gmail.com',
        license='MIT',
        packages=find_packages(),
        install_requires=['pandas >= 0.19'],
        test_suite = 'nose.collector',
        test_require= ['nose']
) 

