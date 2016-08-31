
pip freeze
nosetests --with-cov --cover-package pyexcel_pyexcel --cover-package tests --with-doctest --doctest-extension=.rst tests README.rst  flask_excel && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
