import openpyxl
from datetime import date, datetime, timedelta
from time import sleep


class Worker:
    def __init__(self, first_name, last_name, workerID, paygrade):
        self.line_data = []
        self.first_name = first_name
        self.last_name = last_name
        self.workerID = workerID
        self.paygrade = paygrade
        self.time_sheet_filename = f"{self.first_name} {self.last_name} time sheet.xlsx"
        self.time_sheet = openpyxl.Workbook()
        sheet = self.time_sheet.active
        sheet.append(["Date", "First name", "Last name", "Worker ID", "Clockin time", "Clockout time", "Clocked time"])
        self.time_sheet.save(self.time_sheet_filename)


    def clockIn(self):
        self.line_data = [date.today(), self.first_name, self.last_name, self.workerID, datetime.now().strftime("%H:%M")]


    def clockOut(self):
        self.line_data.append(datetime.now().strftime("%H:%M"))
        h, m = self.line_data[5].split(":")
        h2, m2 = self.line_data[4].split(":")
        total = f"{int(h)-int(h2)}:{int(m)-int(m2)}"
        self.line_data.append(total)


    def submitLine(self):
        workbook = openpyxl.load_workbook(self.time_sheet_filename)
        sheet = workbook.active
        sheet.append(self.line_data)
        workbook.save(self.time_sheet_filename)
        self.line_data = []

def main():
    john = Worker("John", "Walevsky", "123", 40)
    john.clockIn()
    sleep(120)
    john.clockOut()
    john.submitLine()


if __name__ == "__main__":
    main()