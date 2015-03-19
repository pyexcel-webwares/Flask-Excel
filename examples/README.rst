For tiny_example.py, please upload only file that ends with 'csv', 'tsv', 'csvz', 'tsvz'. And if you upload any other formats, your browser will get::

    Bad Request

    The browser (or proxy) sent a request that this server could not understand.

So in these cases, please insert in the tiny_example.py the following imports according to your file:

import pyexcel.ext.xls # for xls file
import pyexcel.ext.xlsx # for xlsx file
import pyexcel.ext.ods # for ods file
