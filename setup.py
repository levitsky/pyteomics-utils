#!/usr/bin/env python

'''
setup.py file for aa_stats
'''

from setuptools import setup, find_packages

setup(
    name                 = 'pyteomics-utils',
    version              = '0.0.4',
    description          = '''Simple but handy CLI tools for everyday data analysis tasks.''',
    long_description     = (''.join(open('README.md').readlines())),
    author               = 'Lev Levitsky',
    author_email         = 'pyteomics@googlegroups.com',
    install_requires     = ['pyteomics'],
    extras_require       = {'XML': ['lxml', 'numpy']},
    classifiers          = ['Intended Audience :: Science/Research',
                            'Programming Language :: Python :: 3',
                            'Topic :: Education',
                            'Topic :: Scientific/Engineering :: Bio-Informatics',
                            'Topic :: Scientific/Engineering :: Chemistry',
                            'Topic :: Scientific/Engineering :: Physics',
                            'Topic :: Software Development :: Libraries'],
    license              = 'License :: OSI Approved :: Apache Software License',
    packages             = find_packages(),
    package_data         = {},
    entry_points         = {'console_scripts': ['pyteomics=pyteomics_utils.main:main']}
    )
