# See license.txt for license details.
# Copyright (c) 2015 Simplistix Ltd

import os, sys

from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

setup(
    name='picky',
    version='0.9.2',
    author='Chris Withers',
    author_email='chris@simplistix.co.uk',
    license='MIT',
    description=(
        "A tool for checking versions of packages used by conda or pip "
        "are as specified in their requirements files."
    ),
    long_description=open(os.path.join(base_dir,'docs','description.rst')).read(),
    url='https://github.com/Simplistix/picky',
    classifiers=[],
    zip_safe=False,
    include_package_data=True,
)
