from openpyxl import Workbook
filename="empty.xlsx"
workbook = Workbook()   # this class s for writing into an excel file
workbook.save(filename=filename)
print(f"{filename} created successfully")