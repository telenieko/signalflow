# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='signalflow',
    version='0.0.1',
    description='Python signal based flow based programming',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/telenieko/signalflow',
    author='Marc Fargas',
    author_email='telenieko@telenieko.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='flow signal datapipe pipe development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={
        'dev': [],
        'test': ['pytest'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/telenieko/signalflow/issues',
        'Source': 'https://github.com/telenieko/signalflow/',
    },
)
