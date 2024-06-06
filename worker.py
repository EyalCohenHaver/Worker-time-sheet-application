import openpyxl
from datetime import date, datetime, timedelta

class Worker:
    def __init__(self, first_name, last_name, workerID, paygrade):
        self.line_data = []
        self.first_name = first_name
        self.last_name = last_name
        self.workerID = workerID
        self.paygrade = paygrade
        self.time_sheet_filename = f"{self.first_name} {self.last_name} time sheet.xlsx"
        self.time_sheet = openpyxl.Workbook()
        self.time_sheet.save(self.time_sheet_filename)


    def clockIn(self):
        self.line_data = [date.today(), self.first_name, self.last_name, self.workerID, datetime.now().strftime("%H:%M")]


    def clockOut(self):
        self.line_data.append(datetime.now().strftime("%H:%M"))
        #TODO: fix the time delta
        self.line_data.append(self.line_data[5] - self.line_data[4])
        workbook = openpyxl.load_workbook(self.time_sheet_filename)
        sheet = workbook.active
        sheet.append(self.line_data)
        workbook.save(self.time_sheet_filename)
        self.line_data = []