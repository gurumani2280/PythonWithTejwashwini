from openpyxl import load_workbook
filename="HelloWorld.xlsx"
workbook = load_workbook(filename=filename)   # this load class is for writing in the samefile
sheet = workbook.active

c = sheet['A3']
c.value = "New Data 3th row"

sheet.append(["new Data1", "new Data2"])    #adds data in the next available last row

workbook.save(filename = filename)
print(f"{filename} updated with new data")