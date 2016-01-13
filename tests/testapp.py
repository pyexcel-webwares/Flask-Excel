from flask import Flask, request, jsonify
from _compact import PY2
from flask.ext import excel
import pyexcel.ext.xls
import pyexcel.ext.ods3
import pyexcel.ext.xlsx
import pyexcel as pe
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime


app=Flask(__name__)

data = [
    [1, 2, 3],
    [4, 5, 6]
]

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


@app.route("/respond/<struct_type>", methods=['GET', 'POST'])
def respond_array(struct_type):
    if struct_type == "array":
        array = request.get_array(field_name='file')
        return jsonify({"result": array})
    elif struct_type == "dict":
        adict = request.get_dict(field_name='file')
        return jsonify({"result": adict})
    elif struct_type == "records":
        records = request.get_records(field_name='file')
        return jsonify({"result": records})
    elif struct_type == "book":
        book = request.get_book(field_name='file')
        return jsonify({"result": book.to_dict()})
    elif struct_type == "book_dict":
        book_dict = request.get_book_dict(field_name='file')
        return jsonify({"result": book_dict})

@app.route("/switch/<file_type>", methods=['POST'])
def switch(file_type):
    sheet = request.get_sheet(field_name='file')
    return excel.make_response(sheet, file_type)

@app.route("/file_name/<file_type>/<file_name>", methods=['POST'])
def swtich_file_name(file_type, file_name):
    return excel.make_response(pe.Sheet(["a", "b", "c"]), file_type, file_name=file_name)

@app.route("/exchange/<struct_type>", methods=['POST'])
def upload_array(struct_type):
    if struct_type == "array":
        array = request.get_array(field_name='file')
        return excel.make_response_from_array(array, 'xls')
    elif struct_type == "dict":
        adict = request.get_dict(field_name='file')
        return excel.make_response_from_dict(adict, 'xls')
    elif struct_type == "records":
        records = request.get_records(field_name='file')
        return excel.make_response_from_records(records, 'xls')
    elif struct_type == "book":
        book = request.get_book(field_name='file')
        return excel.make_response(book, 'xls')
    elif struct_type == "book_dict":
        book_dict = request.get_book_dict(field_name='file')
        return excel.make_response_from_book_dict(book_dict, 'xls')

@app.route("/upload/categories", methods=['POST'])
def upload_categories():
    def table_init_func(row):
        return Category(row['name'])
    request.save_to_database(field_name='file', session=db.session,
                             table=Category, initializer=table_init_func)
    return excel.make_response_from_a_table(db.session, Category, "xls")

@app.route("/upload/all", methods=['POST'])
def upload_all():
    def category_init_func(row):
        c = Category(row['name'])
        c.id = row['id']
        return c
    def post_init_func(row):
        # this is lessons learned that relation needs an object not a string
        c = Category.query.filter_by(name=row['category']).first()
        p = Post(row['title'], row['body'], c, row['pub_date'])
        return p
    request.save_book_to_database(field_name='file', session=db.session,
                                  tables=[Category, Post],
                                  initializers=[category_init_func, post_init_func])
    return excel.make_response_from_tables(db.session, [Category, Post], "xls")
