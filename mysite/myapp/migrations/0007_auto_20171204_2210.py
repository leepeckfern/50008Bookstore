# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 14:10
from __future__ import unicode_literals

from django.db import migrations, connection
import os

def load_data_from_sql(filename):
    file_path = os.path.join(os.path.dirname(__file__), '../sql/', filename)
    sql_statement = open(file_path).read()
    with connection.cursor() as c:
        c.execute(sql_statement)

book_data = lambda x,y: load_data_from_sql('book.sql')

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20171204_2206'),
    ]

    operations = [
        migrations.RunPython(book_data),
    ]