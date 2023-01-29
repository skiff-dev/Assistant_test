from setuptools import setup, find_packages

setup(name='ANS-Assistant',
    version='0.0.8',
    description= 'Addressbook, notebook, clean folder',
    url='https://github.com/DenBilokon/Assistant',
    author='Denis Bilokon, Kirill Sheremeta, Denys Zaycev, Dmytro Marchenko, Maria Palona',
    author_email='greenjuiced@gmail.com',
    license='MIT',
    packages=find_packages(include=['addressbook_classes.py', 'decorators.py']),
    entry_points= {'console_scripts': ['assistant = assistant.addressbook:run']}
          )