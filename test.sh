pip freeze
nosetests --with-coverage --cover-package flask_excel --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source flask_excel && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
