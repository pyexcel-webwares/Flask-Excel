try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

with open("README.rst", 'r') as readme:
    README_txt = readme.read()

dependencies = [
    'pyexcel>=0.1.2',
    'pyexcel-webio>=0.0.1',
    'Flask>=0.10.1'
]

setup(
    name='Flask-Excel',
    author="C. W.",
    version='0.0.1',
    author_email="wangc_2011@hotmail.com",
    url="https://github.com/chfw/Flask-Excel",
    description='A flask extension using pyexcel to read, manipulate and write data in different excel formats: csv, ods, xls, xlsx and xlsm.',
    install_requires=dependencies,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    long_description=README_txt,
    zip_safe=False,
    tests_require=['nose'],
    keywords=['API', 'Flask', 'Excel', 'pyexcel', 'xls', 'xlsx', 'ods', 'csv'],
    license='GNU GPLv3 or BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
