
import os
import getIsDatabase
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook import Workbook




path = "./" # путь сохранение отчетов

def createReportIsTime(start, end):
    file_name = f"Звіт по сюжетам за период від {start} до {end}.xlsx"
    file_path = path + file_name

    if not os.path.exists(file_path):
        wb = load_workbook(file_path) if os.path.exists(file_path) else Workbook()
        sheet_title = f" отчёт {start} до {end}"
        wb.create_sheet(index=0, title=sheet_title)
        try:
            wb.remove(wb["Sheet"])
        except:
            pass

        sheet = wb[sheet_title]

        sheet.column_dimensions['A'].width = 15
        sheet.column_dimensions['B'].width = 23
        sheet.column_dimensions['C'].width = 100
        sheet.column_dimensions['D'].width = 50
        sheet.column_dimensions['E'].width = 25
        sheet.column_dimensions['F'].width = 25
        sheet.column_dimensions['G'].width = 50
        n = 1
        h = 20

        sheet.append(("📅Дата публікації ", "🗿Тип сюжету", "🎥Назва ", "📣ЮТУБ КАНАЛ", "📝Журналіст ", "🎬Монтував", "Url"))
        sheet.row_dimensions[n].height = h
        for i in getIsDatabase.getPeriod(start, end):
            sheet.append(i)
            n += 1
            sheet.row_dimensions[n].height = h
        sheet.append(("📊ВСЬОГО СЮЖЕТІВ", n - 1))
        sheet.row_dimensions[n + 1].height = h

        wb.save(file_path)


def createReportIsTimeAndName(name, start, end):
    file_name = f"Звіт від {start} до {end} {name}.xlsx"
    file_path = path + file_name

    if not os.path.exists(file_path):
        wb = load_workbook(file_path) if os.path.exists(file_path) else Workbook()
        sheet_title = f" отчёт {start} до {end}"
        wb.create_sheet(index=0, title=sheet_title)
        try:
            wb.remove(wb["Sheet"])
        except:
            pass

        sheet = wb[sheet_title]

        sheet.column_dimensions['A'].width = 15
        sheet.column_dimensions['B'].width = 23
        sheet.column_dimensions['C'].width = 100
        sheet.column_dimensions['D'].width = 50
        sheet.column_dimensions['E'].width = 25
        sheet.column_dimensions['F'].width = 25
        sheet.column_dimensions['G'].width = 50
        n = 1
        h = 20

        sheet.append(("📅Дата публікації ", "🗿Тип сюжету", "🎥Назва ", "📣ЮТУБ КАНАЛ", "📝Журналіст ", "🎬Монтував", "Url"))
        sheet.row_dimensions[n].height = h
        for i in getIsDatabase.getJurnForPeriod(name, start, end):
            sheet.append(i)
            n += 1
            sheet.row_dimensions[n].height = h
        sheet.append(("📊ВСЬОГО СЮЖЕТІВ", n - 1))
        sheet.row_dimensions[n + 1].height = h

        wb.save(file_path)

def createReportIsChanel(name, start, end):
    file_name = f"Звіт від {start} до {end} канал: {name}.xlsx"
    file_path = path + file_name

    if not os.path.exists(file_path):
        wb = load_workbook(file_path) if os.path.exists(file_path) else Workbook()
        sheet_title = f" отчёт {start} до {end}"
        wb.create_sheet(index=0, title=sheet_title)
        try:
            wb.remove(wb["Sheet"])
        except:
            pass

        sheet = wb[sheet_title]

        sheet.column_dimensions['A'].width = 15
        sheet.column_dimensions['B'].width = 23
        sheet.column_dimensions['C'].width = 100
        sheet.column_dimensions['D'].width = 50
        sheet.column_dimensions['E'].width = 25
        sheet.column_dimensions['F'].width = 25
        sheet.column_dimensions['G'].width = 50
        n = 1
        h = 20

        sheet.append(("📅Дата публікації ", "🗿Тип сюжету", "🎥Назва ", "📣ЮТУБ КАНАЛ", "📝Журналіст ", "🎬Монтував", "Url"))
        sheet.row_dimensions[n].height = h
        for i in getIsDatabase.getRecurceList(name, start, end):
            sheet.append(i)
            n += 1
            sheet.row_dimensions[n].height = h
        sheet.append(("📊ВСЬОГО СЮЖЕТІВ", n - 1))
        sheet.row_dimensions[n + 1].height = h

        wb.save(file_path)






if __name__ == "__main__":
    print("start Create Exel")
    # createReportIsTimeAndName("Ткач", "2023-10-14", "2023-10-10")
    # createReportIsTimeAndName("Сухоніс", "2023-10-14", "2023-10-05")
    createReportIsChanel("Дніпро Оперативний - життя великого міста", "2023-10-14", "2023-09-01")
    createReportIsTime("2023-10-14", "2023-09-01")
