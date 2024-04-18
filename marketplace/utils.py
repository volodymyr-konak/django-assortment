import sqlite3
from openpyxl import Workbook

from django.conf import settings


def execute_query(query: str) -> list:
    connection = sqlite3.connect(settings.DATABASES['default']['NAME'])
    cursor = connection.cursor()
    query_result = cursor.execute(query)
    return query_result.fetchall()


def save_excel(data: list[list], included_header=None, file_path="sample.xlsx"):
    wb = Workbook()
    ws = wb.active
    if included_header:
        ws.append(included_header)
    for row in data:
        ws.append(row)
    wb.save(file_path)
