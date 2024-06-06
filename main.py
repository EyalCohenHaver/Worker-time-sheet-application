from worker import Worker
from datetime import date, datetime
import openpyxl
import pandas as pd


def main():
    john = Worker("John", "Walevsky", "123", 40)
    today = date.today()
    entryH = datetime.now().strftime("%H:%M:%S")




    workbook = openpyxl.load_workbook(john.time_sheet_filename)
    sheet = workbook.active


    
    data = [
        ["date", "name", "worker ID", "entry time"],
        [today, john.first_name, john.workerID, entryH],
    ]



    for row in data:
        sheet.append(row)
    workbook.save(john.time_sheet_filename)


if __name__ == "__main__":
    main()