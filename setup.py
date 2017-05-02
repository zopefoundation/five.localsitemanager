from setuptools import setup

__version__ = '2.0.6'

setup(
    name='five.localsitemanager',
    version=__version__,
    url='https://pypi.python.org/pypi/five.localsitemanager',
    license='ZPL 2.1',
    description='Local site manager implementation for Zope.',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Zope2',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    keywords='zope five sitemanager',
    packages=['five', 'five.localsitemanager'],
    package_dir={'': 'src'},
    namespace_packages=['five'],
    include_package_data=True,
    install_requires=[
        'Acquisition',
        'ZODB3',
        'setuptools',
        'zope.component',
        'zope.event',
        'zope.interface',
        'zope.location',
        'zope.lifecycleevent',
        'zope.testing',
        'Zope2 >= 2.12.0',
    ],
    zip_safe=False,
)
