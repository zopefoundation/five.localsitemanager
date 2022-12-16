from setuptools import setup


version = '3.4'

setup(
    name='five.localsitemanager',
    version=version,
    url='https://github.com/zopefoundation/five.localsitemanager',
    project_urls={
        'Issue Tracker': ('https://github.com/zopefoundation/'
                          'five.localsitemanager/issues'),
        'Sources': 'https://github.com/zopefoundation/five.localsitemanager',
    },
    license='ZPL 2.1',
    description='Local site manager implementation for Zope.',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope :: 4',
        'Framework :: Zope :: 5',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    keywords='zope five sitemanager',
    packages=['five', 'five.localsitemanager'],
    package_dir={'': 'src'},
    namespace_packages=['five'],
    include_package_data=True,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    install_requires=[
        'Acquisition',
        'persistent',
        'setuptools',
        'six',
        'zope.component',
        'zope.event',
        'zope.interface >= 3.8',
        'zope.location',
        'zope.lifecycleevent',
        'zope.site',
        'zope.testing',
        'Zope >= 4.0b1',
    ],
    zip_safe=False,
)
