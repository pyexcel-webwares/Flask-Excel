============================================================
flask-excel - Let you focus on data, instead of file formats
============================================================

.. image:: https://api.travis-ci.org/chfw/flask-excel.svg?branch=master
   :target: http://travis-ci.org/chfw/flask-excel

.. image:: https://coveralls.io/repos/chfw/flask-excel/badge.png?branch=master 
   :target: https://coveralls.io/r/chfw/flask-excel?branch=master 

.. image:: https://readthedocs.org/projects/flask-excel/badge/?version=latest
   :target: http://flask-excel.readthedocs.org/en/latest/

.. image:: https://pypip.in/version/flask-excel/badge.png
   :target: https://pypi.python.org/pypi/flask-excel

.. image:: https://pypip.in/d/flask-excel/badge.png
   :target: https://pypi.python.org/pypi/flask-excel

.. image:: https://pypip.in/py_versions/flask-excel/badge.png
   :target: https://pypi.python.org/pypi/flask-excel

.. image:: http://img.shields.io/gittip/chfw.svg
   :target: https://gratipay.com/chfw/

**flask-excel** is based on `pyexcel <https://github.com/chfw/pyexcel>`_ and makes it easy to consume/produce information stored in excel files over HTTP protocol as well as on file system. This library can turn the excel data into Pythonic a list of lists, a list of records(dictionaries), dictionaries of lists. And vice versa. Hence it lets you focus on data in Flask based web development, instead of file formats.

The idea originated from the problem of the illiteracy of excel file formats of non-technical office workers: such as office assistant, human resource administrator. There is nothing with the un-deniable fact that some people do not know the difference among various excel formats. It becomes usability problem to those people when a web service cannot parse the excel file that they saved using Microsoft Excel. Instead of training those people about file formats, this library helps web developers to handle most of the excel file formats by unifying the programming interface to most of the excel readers and writers.

The highlighted features are:

#. turn uploaded excel file directly into Python data struture
#. pass Python data structures as an excel file download
#. provide data persistence as an excel file in server side
#. supports csv, tsv, csvz, tsvz by default and other formats are supported via the following plugins:

Available Plugins
=================

================ ========================================================================
Plugins          Supported file formats                                      
================ ========================================================================
`pyexcel-xls`_   xls, xlsx(r), xlsm(r)
`pyexcel-xlsx`_  xlsx
`pyexcel-ods`_   ods (python 2.6, 2.7)                                       
`pyexcel-ods3`_  ods (python 2.7, 3.3, 3.4)                                  
================ ========================================================================

.. _pyexcel-xls: https://github.com/chfw/pyexcel-xls
.. _pyexcel-xlsx: https://github.com/chfw/pyexcel-xlsx
.. _pyexcel-ods: https://github.com/chfw/pyexcel-ods
.. _pyexcel-ods3: https://github.com/chfw/pyexcel-ods3
.. _pyexcel-text: https://github.com/chfw/pyexcel-text


Known constraints
==================

Fonts, colors and charts are not supported. 

Installation
============
You can install it via pip::

    $ pip install flask-pyexcel


or clone it and install it::

    $ git clone http://github.com/chfw/flask-pyexcel.git
    $ cd flask-pyexcel
    $ python setup.py install

Installation of individual plugins , please refer to individual plugin page.


Usage
=========

Here are some example codes::

    from flask import Flask, request, jsonify
    from flask.ext import excel
    
    app=Flask(__name__)
    
    @app.route("/upload", methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            return jsonify({"result": request.get_array('file')})
        return '''
        <!doctype html>
        <title>Upload an excel file</title>
        <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
        <form action="" method=post enctype=multipart/form-data>
        <p><input type=file name=file><input type=submit value=Upload>
    	</form>
        '''
    
    @app.route("/download", methods=['GET'])
    def download_file():
        return excel.make_response_from_array([[1,2], [3, 4]], "csv")
    
    if __name__ == "__main__":
        app.run()


Dependencies
=============

* pyexcel

