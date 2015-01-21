from flask import Flask, Request, Response
import pyexcel as pe
import pyexcel_webio as webio

class ExcelRequest(webio.ExcelInput, Request):
    def _get_file_tuple(self, field_name):
        filehandle = self.files[field_name]
        filename = filehandle.filename
        extension = filename.split(".")[1]
        return extension, filehandle

    def load_single_sheet(self, field_name=None, sheet_name=None, **keywords):
        file_type, file_handle = self._get_file_tuple(field_name)
        return pe.get_sheet(file_type=file_type,
                            content=file_handle.read(),
                            sheet_name=sheet_name,
                            **keywords)

    def load_book(self, field_name=None, **keywords):
        file_type, file_handle = self._get_file_tuple(field_name)
        return pe.get_book(file_type=file_type,
                           content=file_handle.read(),
                           **keywords)
    

Flask.request_class = ExcelRequest
webio.ExcelResponse = Response

from pyexcel_webio import (
    make_response,
    make_response_from_array,
    make_response_from_dict,
    make_response_from_records,
    make_response_from_book_dict,
    make_response_from_a_table,
    make_response_from_tables
)
