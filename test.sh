

pip freeze
nosetests --with-cov --cover-package Flask_excel --cover-package tests --with-doctest --doctest-extension=.rst tests README.rst docs/source Flask_excel && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
