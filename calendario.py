import holidays
from datetime import datetime
from workadays import workdays as wd


class Calendario:


    data = datetime.today().date()
    feriados = holidays.Brazil()
    folga = False

    def feriado():

        for feriado in Calendario.feriados[f'01-01-{datetime.today().year}': f'31-12-{datetime.today().year}']:
            if Calendario.data == feriado:
                Calendario.folga = True
        return Calendario.folga


    def util():
        e_dia_util = wd.is_workday(Calendario.data, country='BR', years=(datetime.today().year))
        return e_dia_util


# print(wd.is_holiday('12/10/2021', country='BR', years=dt.today().year))

print(Calendario.util())