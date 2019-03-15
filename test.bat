pip freeze
nosetests --with-coverage --cover-package flask_excel --cover-package tests tests --with-doctest --doctest-extension=.rst README.rst docs/source flask_excel
