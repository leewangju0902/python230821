# ChatGPT_ExcelSave.py
from openpyxl import Workbook
from datetime import datetime

sales_data = [
    ("Product A", 100, 10, "2023-08-01"),
    ("Product B", 200, 5, "2023-08-02"),
    # ... Add more data here ...
]

workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Sales Data"

worksheet.append(["Product Name", "Price", "Quantity", "Sale Date"])

for product, price, quantity, sale_date in sales_data:
    worksheet.append([product, price, quantity, sale_date])

file_path = r'c:\work\sales.xlsx'
workbook.save(file_path)
