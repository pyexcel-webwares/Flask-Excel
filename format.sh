isort $(find Flask_Excel -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 Flask_Excel
black -l 79 tests
