import xlrd
import time
import HtmlTestRunner
import unittest

class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            excel_path = r"C:\work\vcPyTest\WebTest\\Configure\ddtConfig.xls"
        
        if index == None:
            index = 0

        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]

    def get_lines(self):
        rows = self.table.nrows

        if rows >=1:
            return rows
        else:
            return None


    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        else:
            return None

    def get_col_value(self, row, col):
        data = None
        if row < self.get_lines() and row >=0:
            data = self.table.cell(row, col).get_col_value
          
        return data

    def write_value(self, row, col):
        pass
           
