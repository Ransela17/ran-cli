from setuptools import setup, find_packages

def read_requirements(): 
    with open ('requirements.txt') as req:
        content = req.read() 
        requirements = content.split('\n')
    return requirements #return list of strings


setup(
    name='ran',
    version='1.0',
    py_modules=["ran"],
    packages = find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
        'ran=ran_cli.cli:cli'
        ],
    },
)