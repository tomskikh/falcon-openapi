#!/usr/bin/env python
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='falcon-openapi',
    python_requires='>3.5.0',
    version='0.1.6',
    description='Falcon router to map openapi spec to resources',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Sam Kleiner',
    author_email='sam@skleiner.com',
    license=license,
    url='https://github.com/StoicPerlman/falcon-openapi/',
    download_url = 'https://github.com/StoicPerlman/falcon-openapi/archive/0.1.6.tar.gz',
    keywords = ['falcon', 'openapi', 'api'],
    packages=['falcon_openapi'],
    install_requires=[
        'falcon',
        'pyyaml'
    ],
    extras_require={
        'dev': [
            'unittest'
        ]
    }
)
