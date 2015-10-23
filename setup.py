try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

with open("README.rst", 'r') as readme:
    README_txt = readme.read()

dependencies = [
    'pyexcel>=0.1.5',
    'pyexcel-webio>=0.0.3',
    'Flask>=0.10.1'
]
extras = {
    'xls': ['pyexcel-xls==0.0.7'],
    'xlsx': ['pyexcel-xlsx==0.0.7'],
    'ods3': [
        'pyexcel-ods3==0.0.8',
        'git+https://github.com/T0ha/ezodf.git@2c69103e6c0715adb0e36562cb2e6325fd776112#egg=ezodf-master',
    ],
}

setup(
    name='Flask-Excel',
    author="C. W.",
    version='0.0.3',
    author_email="wangc_2011@hotmail.com",
    url="https://github.com/chfw/Flask-Excel",
    description='A flask extension that provides one application programming interface to read and write data in different excel file formats',
    install_requires=dependencies,
    extras_require=extras,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    long_description=README_txt,
    zip_safe=False,
    tests_require=['nose'],
    keywords=['API', 'Flask', 'Excel', 'pyexcel', 'xls', 'xlsx', 'ods', 'csv'],
    license='New BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
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
