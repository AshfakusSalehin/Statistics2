import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(1, 0, 'ISBT New Delhi')
sheet1.write(2, 0, 'MMDU Hostel-2')
sheet1.write(3, 0, 'Engg. Block-1')
sheet1.write(4, 0, 'RAJPUR ROAD')
sheet1.write(5, 0, 'CLOCK TOWER')
sheet1.write(0, 1, 'ISBT AGRA')
sheet1.write(0, 2, 'MMDU Hostel-3')
sheet1.write(0, 3, 'Engg. Block-1')
sheet1.write(0, 4, 'RAJPUR ROAD')
sheet1.write(0, 5, 'CLOCK TOWER')

wb.save('example.xls')
