import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-misa',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'django>=1.11.15',
        'django-gfiles',
        'isatools',
        'django-mbrowse'
    ],
    include_package_data=True,
    license="GPLv3",
    description='ISA organisation for metabolomic studies with Django',
    long_description=README,
    url='https://mogi.readthedocs.io',
    author='Thomas N lawson',
    author_email='thomas.nigel.lawson@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
