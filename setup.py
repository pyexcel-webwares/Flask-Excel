try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

with open("README.rst", 'r') as readme:
    README_txt = readme.read()

dependencies = [
    'pyexcel>=0.2.0',
    'pyexcel-webio>=0.0.5',
    'Flask>=0.10.1',
]

extras = {
    'xls': ['pyexcel-xls>=0.1.0'],
    'xlsx': ['pyexcel-xlsx>=0.1.0'],
    'ods': ['pyexcel-ods3>=0.1.0'],
}


setup(
    name='Flask-Excel',
    author='C.W.',
    version='0.0.5',
    author_email='wangc_2011 (at) hotmail.com',
    url='https://github.com/pyexcel/Flask-Excel',
    description='A flask extension that provides one application programming interface to read and write data in different excel file formats',
    install_requires=dependencies,
    extras_require=extras,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    long_description=README_txt,
    zip_safe=False,
    tests_require=['nose'],
    keywords=[
        'excel',
        'python',
        'pyexcel',
        'xls',
        'xlsx',
        'ods',
        'csv',
        'API',
        'Flask'
    ],
    license='New BSD',
    classifiers=[
        'Topic :: Office/Business',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)