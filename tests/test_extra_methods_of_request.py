from testapp import app
import pyexcel as pe
import json
from _compact import OrderedDict, BytesIO
    
class TestSheet:
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.data = [
            ['X', 'Y', 'Z'],
            [1, 2, 3],
            [4, 5, 6]
        ]

    def test_array(self):
        test_sample = {
            "array": {u'result': [[u'X', u'Y', u'Z'], [1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]},
            "dict": {u'result': {u'Y': [2.0, 5.0], u'X': [1.0, 4.0], u'Z': [3.0, 6.0]}},
            "records": {u'result': [{u'Y': 2.0, u'X': 1.0, u'Z': 3.0}, {u'Y': 5.0, u'X': 4.0, u'Z': 6.0}]}
        }
        for struct_type in test_sample.keys():
            io = BytesIO()
            sheet = pe.Sheet(self.data)
            sheet.save_to_memory('xls', io)
            io.seek(0)
            response = self.app.post('/respond/%s' % struct_type, buffered=True,
                                     data={"file": (io, "test.xls")},
                                     content_type="multipart/form-data")
            expected = test_sample[struct_type]
            assert json.loads(response.data.decode('utf-8')) == expected


class TestBook:
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.content = OrderedDict()
        self.content.update({"Sheet1": [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]})
        self.content.update({"Sheet2": [[4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]]})
        self.content.update({"Sheet3": [[u'X', u'Y', u'Z'], [1, 4, 7], [2, 5, 8], [3, 6, 9]]})

    def test_book(self):
        test_sample = ["book", "book_dict"]
        expected = {u'result': {u'Sheet1': [[1.0, 1.0, 1.0, 1.0], [2.0, 2.0, 2.0, 2.0], [3.0, 3.0, 3.0, 3.0]], u'Sheet3': [[u'X', u'Y', u'Z'], [1.0, 4.0, 7.0], [2.0, 5.0, 8.0], [3.0, 6.0, 9.0]], u'Sheet2': [[4.0, 4.0, 4.0, 4.0], [5.0, 5.0, 5.0, 5.0], [6.0, 6.0, 6.0, 6.0]]}}
        for struct_type in test_sample:
            io = BytesIO()
            book = pe.Book(self.content)
            book.save_to_memory('xls', io)
            io.seek(0)
            response = self.app.post('/respond/%s' % struct_type, buffered=True,
                                     data={"file": (io, "test.xls")},
                                     content_type="multipart/form-data")
            assert json.loads(response.data.decode('utf-8')) == expected
