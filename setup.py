"""Setup for five.localsitemanager package

$Id$
"""
from setuptools import setup, Extension

version = '1.1dev'

setup(name='five.localsitemanager',
      version=version,
      url='http://svn.zope.org/five.localsitemanager',
      license='ZPL 2.1',
      description='Local site manager implementation for Zope 2',
      author='Rocky Burt and Contributors',
      author_email='zope-cmf@zope.org',
      long_description=open("README.txt").read() + "\n" + 
                       open("INSTALL.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Zope2',
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
        'zope.component < 3.5dev',
      ],
      zip_safe = False,
      )
