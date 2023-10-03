"""
WaterMark python modules.

Colin Page <cwpage@umich.edu>
"""

from setuptools import setup

setup(
    name='WaterMark',
    version='0.1.0',
    packages=['WaterMark'],
    include_package_data=True,
    install_requires=[
        'Pillow==10.0.1',
    ],
)
