import openpyxl

class Worker:
    def __init__(self, first_name, last_name, workerID, paygrade):
        self.first_name = first_name
        self.last_name = last_name
        self.workerID = workerID
        self.paygrade = paygrade
        self.time_sheet_filename = f"{self.first_name} {self.last_name} time sheet.xlsx"
        self.time_sheet = openpyxl.Workbook()
        self.time_sheet.save(self.time_sheet_filename)


