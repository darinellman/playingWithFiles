
import os
import fnmatch

#from openpyxl import Workbook
#from openpyxl import load_workbook



def find_files(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            yield os.path.join(path, file)

for f in find_files("C:", '.pdf'):
    print(f)

#for f in find_files("C:\\Users\\drnellman\\Desktop", 'pdf'):
#    print(f)


"""  
wb = Workbook()

ws = wb.active

ws['A1'] = 'empCode'
ws['B1'] = 'empName'
ws['C1'] = 'SPIFF'
ws['D1'] = 'commTotal'
ws['E1'] = 'EmpID'
ws['F1'] = 'LastName'
ws['G1'] = 'FirstName'

ws['C5'] = "you didn't copy amything"


#ws['E1'] = datetime.datetime.now()

for sku in range(len(slpl)):
    empCode, empName, qty, SPIFF, commTotal = slpl[slprsn]
    #for employee in range(len(empList)):

    #need to put if statement to find minus signs at end of strings
    #and then move them to the front
    #then convert number strings to floats
    ws['A' + str(sku + 2)] = empCode
    ws['B' + str(sku + 2)] = empName
    if SPIFF[-1] == '-':
        SPIFF = "-" + SPIFF[0:(len(SPIFF)-1)]
    ws['C' + str(sku + 2)] = float(SPIFF)
    if commTotal[-1] == '-':
        commTotal = "-" + commTotal[0:(len(commTotal)-1)]
    ws['D' + str(sku + 2)] = float(commTotal)

    print(empCode + ", " + empName + ", " + SPIFF + ", " + commTotal)

    slprsn += 1


wb.save("files.xlsx")

"""
