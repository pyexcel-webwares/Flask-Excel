{%extends 'WEB-README.rst.jj2' %}

{%block header %}
Tested Flask Versions
========================

.. image:: https://img.shields.io/badge/Flask-0.12.2-green.svg
    :target: http://travis-ci.org/pyexcel/Flask-Excel

.. image:: https://img.shields.io/badge/Flask-0.11.1-green.svg
    :target: http://travis-ci.org/pyexcel/Flask-Excel

.. image:: https://img.shields.io/badge/Flask-0.10.1-green.svg
    :target: http://travis-ci.org/pyexcel/Flask-Excel


{%endblock%}


{% block usage %}

Usage
================================================================================

Here are some example codes:


.. literalinclude:: examples/tiny_example.py
   :lines: 7-31, 44-48

{% endblock %}
