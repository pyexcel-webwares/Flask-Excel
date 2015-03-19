For tiny_example.py, please upload only file that ends with 'csv', 'tsv', 'csvz', 'tsvz'. And if you upload any other formats, your browser will get::

    Internal Server Error

    The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.

So in these cases, please insert in the tiny_example.py the following imports according to your file:

import pyexcel.ext.xls # for xls file
import pyexcel.ext.xlsx # for xlsx file
import pyexcel.ext.ods # for ods file

