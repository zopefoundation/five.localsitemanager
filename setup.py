from setuptools import setup


setup(
    name='five.localsitemanager',
    version='5.1.dev0',
    url='https://github.com/zopefoundation/five.localsitemanager',
    project_urls={
        'Issue Tracker': ('https://github.com/zopefoundation/'
                          'five.localsitemanager/issues'),
        'Sources': 'https://github.com/zopefoundation/five.localsitemanager',
    },
    license='ZPL-2.1',
    description='Local site manager implementation for Zope.',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope :: 5',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    keywords='zope five sitemanager',
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=[
        'Acquisition',
        'persistent',
        'setuptools',
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
