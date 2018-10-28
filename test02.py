import xlwt
import xlrd


#escrita
head = ['ID','NOME','DEFINIDO','SOLICITADO']
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet(u'Simples')
for i in range(4):
    worksheet.write(0, i, u'{}'.format(head[i]))

workbook.save('simples.xlsx')

# leitura
#
# workbook = xlrd.open_workbook('/home/leonardo/Documentos/Férias 2018.xlsx')
# worksheet = workbook.sheet_by_index(1)
#
# for i in range(worksheet.nrows):
#     if i != 0 and i != 1:
#         row = worksheet.row_values(i)
#         print(row)
