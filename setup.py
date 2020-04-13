#!/usr/bin/env python
from setuptools import setup

try:
    from testr.setup_helper import cmdclass
except ImportError:
    cmdclass = {}

entry_points = {'console_scripts': 'bep_pcb_check = bep_pcb_check.bep_pcb_check:main'}

setup(name='bep_pcb_check',
      packages=["bep_pcb_check"],
      use_scm_version=True,
      setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
      description='ACIS Thermal Model for BEP PCB Temperature',
      author='John ZuHone',
      author_email='jzuhone@gmail.com',
      url='http://github.com/acisops/bep_pcb_check',
      include_package_data=True,
      entry_points=entry_points,
      zip_safe=False,
      tests_require=["pytest"],
      cmdclass=cmdclass,
      )
