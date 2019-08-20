import xlwings as xw

app= xw.App(visible=True, add_book=False)
wb=app.books.add()
# wb就是新建的工作簿(workbook)，下面则对wb的sheet1的A1单元格赋值
# wb.sheets['sheet1'].range('A1').value='人生'

wb.sheets['sheet1'].range('A1').value=["公众号","文章标题","时间" ,"链接"]



wb.save(r'公众号近期文章.xlsx')
wb.close()
app.quit()
