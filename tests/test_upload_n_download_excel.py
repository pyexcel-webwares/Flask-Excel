from testapp import app
import pyexcel as pe
from _compact import BytesIO, PY2


FILE_TYPE_MIME_TABLE = {
    "csv": "text/csv",
    "tsv": "text/tab-separated-values",
    "csvz": "application/zip",
    "tsvz": "application/zip",
    "ods": "application/vnd.oasis.opendocument.spreadsheet",
    "xls": "application/vnd.ms-excel",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "xlsm": "application/vnd.ms-excel.sheet.macroenabled.12"
}


class TestExcelResponse:
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.data = [
            [1, 2, 3],
            [4, 5, 6]
        ]

    def test_download(self):
        for upload_file_type in FILE_TYPE_MIME_TABLE.keys():
            file_name = 'test.%s' % upload_file_type
            for download_file_type in FILE_TYPE_MIME_TABLE.keys():
                print("Uploading %s Downloading %s" % (upload_file_type, download_file_type))
                io = pe.save_as(dest_file_type=upload_file_type, array=self.data)
                if not PY2:
                    if not isinstance(io, BytesIO):
                        io = BytesIO(io.getvalue().encode('utf-8'))
                response = self.app.post('/switch/%s' % download_file_type,
                                         buffered=True,
                                         data={"file": (io, file_name)},
                                         content_type="multipart/form-data")
                assert response.content_type == FILE_TYPE_MIME_TABLE[download_file_type]
                sheet = pe.get_sheet(file_type=download_file_type,
                                     file_content=response.data)
                sheet.format(int)
                array = sheet.to_array()
                assert array == self.data

    def test_override_file_name(self):
        for file_type in FILE_TYPE_MIME_TABLE.keys():
            file_name = 'override_file_name'
            response = self.app.post('/file_name/%s/%s' % (file_type, file_name))
            assert response.content_type == FILE_TYPE_MIME_TABLE[file_type]
            assert response.headers.get("Content-Disposition", None) == ("attachment; filename=%s.%s" % (file_name, file_type))

