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

def add_file_name(response, file_name, file_type):
    if file_name:
        response.headers["Content-Disposition"] = "attachment; filename=%s.%s" % (file_name, file_type)
    return response

def make_response(pyexcel_instance, file_type, status=200, file_name=None, **keywords):
    return add_file_name(webio.make_response(pyexcel_instance, file_type, status=status, **keywords), file_name, file_type)

def make_response_from_array(array, file_type, status=200, file_name=None, **keywords):
    return add_file_name(webio.make_response_from_array(array, file_type, status=status, **keywords), file_name, file_type)

def make_response_from_dict(adict, file_type, status=200, file_name=None, **keywords):
    return add_file_name(webio.make_response_from_dict(adict, file_type, status=status, **keywords), file_name, file_type)

def make_response_from_records(records, file_type, status=200, file_name=None, **keywords):
    return add_file_name(webio.make_response_from_records(records, file_type, status=status, **keywords), file_name, file_type)

def make_response_from_book_dict(adict, file_type, status=200, file_name=None, **keywords):
    return add_file_name(webio.make_response_from_book_dict(adict, file_type, status=status, **keywords), file_name, file_type)

def make_response_from_a_table(session, table, file_type, status=200, file_name=None, **keywords):
    return add_file_name(webio.make_response_from_a_table(session, table, file_type, status=status, **keywords), file_name, file_type)

def make_response_from_query_sets(query_sets, column_names, file_type, status=200, file_name=None, **keywords):
    return add_file_name(webio.make_response_from_query_sets(query_sets, column_names, file_type, status=status, **keywords), file_name, file_type)

def make_response_from_tables(session, tables, file_type, status=200, file_name=None, **keywords):
    return add_file_name(webio.make_response_from_tables(session, tables, file_type, status=status, **keywords), file_name, file_type)

__VERSION__ = '0.0.4'
