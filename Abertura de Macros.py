import time

import xlwings as xw
wb = xw.Book('Nome com Extensão do seu arquivo')

time.sleep(10)
#Nome da sua Macro
macro = wb.macro('Main.Macro1')
macro()