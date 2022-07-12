'''
@copyright: 2022 - Symas Corporation
'''
from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='py-fortress-sample',
      version='0.1.7',
      python_requires='>=3.6',
      description='RBAC for Python Test Samples',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/shawnmckinney/py-fortress-sample',
      author='Symas Corporation',
      author_email='smckinney@symas.com',
      license='Apache License 2.0',
      packages=['sample', 'sample.ldap'],
      package_data={
          # If any package contains *.txt or *.rst files, include them:
          '': ['*.md', '*.json'],
      },

      install_requires=[
          'py-fortress >= 0.1.7'
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Topic :: Security',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='authorization rbac security',
      zip_safe=False)
