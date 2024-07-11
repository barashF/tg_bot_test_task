import datetime
from Google_sheets.manager_sheets import input_value_sheet

#пробуем ввести дату
async def input_date(date):
    try:
        date_format = "%d.%m.%Y"
        datetime.datetime.strptime(date, date_format)
        input_value_sheet(date)

        return "succes"
    
    except ValueError:
        return "error"