{%extends 'WEB-README.rst.jj2' %}

{% block usage %}

Usage
================================================================================

Here are some example codes:

.. code-block:: python

    from flask import Flask, request, jsonify
    from flask.ext import excel

    app=Flask(__name__)

    @app.route("/upload", methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            return jsonify({"result": request.get_array(field_name='file')})
        return '''
        <!doctype html>
        <title>Upload an excel file</title>
        <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
        <form action="" method=post enctype=multipart/form-data>
        <p><input type=file name=file><input type=submit value=Upload>
       </form>
        '''

    @app.route("/export", methods=['GET'])
    def export_records():
        return excel.make_response_from_array([[1,2], [3, 4]], "csv",
                                              file_name="export_data")

    if __name__ == "__main__":
        app.run()

{% endblock %}
