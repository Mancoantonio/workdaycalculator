import datetime
import calendar
import holidays
import argparse
import dateutil
import pytz
import tabulate
import json



def main():
    fecha_inicio = int(input("Cuál es la fecha de inicio (YYYYMMDD): "))
    work_days = int(input("Cuántos días laborales?: "))
    country_code = input("Cuál es el código de país (por ejemplo, US, ES, FR, etc)?: ")

    print("Calculando la fecha final...\n")

# Convertir la fecha de inicio a un objeto datetime
    fecha_str = str(fecha_inicio)
    start_date = datetime.datetime.strptime(fecha_str, "%Y%m%d").date()

# Calcular la fecha final
    current_date = start_date
    count = 0

    while count < work_days:
        current_date += datetime.timedelta(days=1)
        if current_date.weekday() < 5 and current_date not in holidays.CountryHoliday(country_code):
            count += 1

    print(f"La fecha final es: {current_date}") 

main()