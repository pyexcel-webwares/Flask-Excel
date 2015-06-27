"""
    flask_excel
    ~~~~~~~~~~~~~~~~~~~

    A flask extension that provides one application programming interface
    to read and write data in different excel file formats

    :copyright: (c) 2015 by Onni Software Ltd.
    :license: New BSD License
"""
from flask import Flask, Request, Response
import pyexcel as pe
import pyexcel_webio as webio

class ExcelRequest(webio.ExcelInputInMultiDict, Request):
    def get_file_tuple(self, field_name):
        filehandle = self.files[field_name]
        filename = filehandle.filename
        extension = filename.split(".")[1]
        return extension, filehandle
    

Flask.request_class = ExcelRequest
webio.ExcelResponse = Response

from pyexcel_webio import (
    make_response,
    make_response_from_array,
    make_response_from_dict,
    make_response_from_records,
    make_response_from_book_dict,
    make_response_from_a_table,
    make_response_from_query_sets,
    make_response_from_tables
)

__VERSION__ = '0.0.3'
