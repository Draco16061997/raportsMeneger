import time
from datetime import datetime
import CreateExel
import getIsDatabase



c = CreateExel
g = getIsDatabase
d = str(datetime.now().date())

def period_to_now(days):
    # Получить текущую дату и время в формате timestamp
    current_time = time.time()

    # Вычислить новую дату, вычитая заданное количество дней
    new_time = current_time - days * 24 * 60 * 60

    # Преобразовать новую дату в объект datetime
    date_obj = datetime.fromtimestamp(new_time)

    # Преобразовать объект datetime в строку в формате "год-месяц-день"
    return date_obj.strftime("%Y-%m-%d")


if __name__ == "__main__":
    print(g.getNameDir())
    print(g.getNameJurn())
    print(g.getResurce())


    # CreateExel.createReportIsChanel('Дніпро Оперативний - життя великого міста', d, period_to_now(30))
    # CreateExel.createReportIsChanel('Наше Місто', d, period_to_now(30))
    # CreateExel.createReportIsChanel('Дніпровська Панорама', d, period_to_now(30))

    # с.createReportIsTimeAndName("Малихіна", d, period_to_now(30))
    # с.createReportIsTimeAndName('Ткач', d, period_to_now(30))
    # с.createReportIsTimeAndName('Глущенко', d, period_to_now(30))
    # с.createReportIsTimeAndName('Сухоніс', d, period_to_now(30))
    # с.createReportIsTimeAndName('Нікітін', d, period_to_now(30))

    # с.createReportIsTimeAndName('Скрипніченко', d, period_to_now(30))
    # с.createReportIsTimeAndName('Бездільний', d, period_to_now(30))
    # с.createReportIsTimeAndName('Тарасов', d, period_to_now(30))
    # с.createReportIsTimeAndName('Тейлор', d, period_to_now(30))
    # с.createReportIsTimeAndName('Нікітін', d, period_to_now(30))

    CreateExel.createReportIsTime(d, period_to_now(30))





