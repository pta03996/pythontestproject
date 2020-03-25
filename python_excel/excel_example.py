import openpyxl as xl

workbook = xl.load_workbook('transactions.xlsx')
workbook_sheet = workbook['Sheet1']
workbook_cell = workbook_sheet['a1'] # diff code but same result workbook_cell = workbook_sheet.cell(1,1)
#get how many row in a sheet
print(workbook_sheet.max_row)
for row in range(1, workbook_sheet.max_row + 1):
    workbook_cell(row,3)