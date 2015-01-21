from testapp import app
import pyexcel as pe
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
        for struct_type in ["array", "dict", "records"]:
            print("Testing %s" % struct_type)
            io = BytesIO()
            sheet = pe.Sheet(self.data)
            sheet.save_to_memory('xls', io)
            io.seek(0)
            response = self.app.post('/exchange/%s' % struct_type,
                                     buffered=True,
                                     data={"file": (io, "test.xls")},
                                     content_type="multipart/form-data")
            assert response.content_type == "application/vnd.ms-excel"
            sheet = pe.load_from_memory('xls', response.data)
            assert sheet.to_array() == self.data



class TestBook:
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.content = OrderedDict()
        self.content.update({"Sheet1": [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]})
        self.content.update({"Sheet2": [[4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]]})
        self.content.update({"Sheet3": [[u'X', u'Y', u'Z'], [1, 4, 7], [2, 5, 8], [3, 6, 9]]})

    def test_book(self):
        for struct_type in ["book", "book_dict"]:
            io = BytesIO()
            book = pe.Book(self.content)
            book.save_to_memory('xls', io)
            io.seek(0)
            response = self.app.post('/exchange/%s' % struct_type,
                                     buffered=True,
                                     data={"file": (io, "test.xls")},
                                     content_type="multipart/form-data")
            assert response.content_type == "application/vnd.ms-excel"
            book2 = pe.load_book_from_memory('xls', response.data)
            assert book2.to_dict() == self.content
