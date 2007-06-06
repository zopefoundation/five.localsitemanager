"""Setup for five.localsitemanager package

$Id$
"""
import os
from setuptools import setup, Extension

version = '0.1.2'

setup(name='five.localsitemanager',
      version=version,
      url='http://svn.zope.org/five.localsitemanager',
      license='ZPL 2.1',
      description='Local site manager implementation for Zope 2',
      author='Rocky Burt and Contributors',
      author_email='z3-five@codespeak.net',
      long_description="""\
five.localsitemanager attempts to provide a local site manager implementation
that is as close to Zope 3's implemenation as possible.  Some reservations
that do not conflict with Zope 3 have been made to easy the path with CMF.
""",

      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Zope2',
          'Framework :: Zope3',
          'License :: OSI Approved :: Zope Public License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='zope zope2 zope3 five sitemanager',

      packages=['five', 'five.localsitemanager'],
      package_dir = {'': 'src'},
      namespace_packages=['five',],
      include_package_data = True,
      install_requires=[
        'setuptools',
      ],
      zip_safe = False,
      )
