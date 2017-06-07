#!/usr/bin/env python
from setuptools import setup
from bep_pcb_check import __version__

entry_points = {'console_scripts': 'bep_pcb_check = bep_pcb_check.bep_pcb_check:main'}

url = 'https://github.com/acisops/bep_pcb_check/tarball/{}'.format(__version__)

setup(name='bep_pcb_check',
      packages=["bep_pcb_check"],
      version=__version__,
      description='ACIS Thermal Model for BEP PCB Temperature',
      author='John ZuHone',
      author_email='jzuhone@gmail.com',
      url='http://github.com/acisops/bep_pcb_check',
      download_url=url,
      include_package_data=True,
      classifiers=[
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
      ],
      entry_points=entry_points,
      )
