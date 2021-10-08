import datetime as dt
import os
import pathlib as pl
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import calendario as cl
import correios
import importador


class MonitorFolder(FileSystemEventHandler):
    FILE_SIZE = 10000
    src_patch = '//192.163.1.179/HP_Transportes/Extrator/Dados/Distribuicao/'
    last_event = 0
    rel = ''



    def on_modified(self, event):

        time.sleep(1)
        '''if not event.src_path == last_event:
            last_event = event.src_path'''
        path = pl.Path(src_path)

        print(event.src_path, event.event_type)

        importador.IMPORTADOR.import_km()
        importador.IMPORTADOR.import_tarifa()
        importador.IMPORTADOR.import_demanda()
        importador.IMPORTADOR.import_km_prev()
        importador.IMPORTADOR.import_demanda_prev()
        importador.IMPORTADOR.import_receita_prev()

        if cl.Calendario.feriado() == False and cl.Calendario.util() == True:

            if event.src_path == '//192.163.1.179/HP_Transportes/Extrator/Dados/Distribuicao/KM.csv':
                for i in path.iterdir():
                    if (dt.datetime.fromtimestamp(i.stat().st_mtime).hour > MonitorFolder.last_event) or ((
                            dt.datetime.fromtimestamp(i.stat().st_mtime).hour + 12) > MonitorFolder.last_event) and \
                            MonitorFolder.rel != i.name:
                        if i.name == 'KM.csv':
                            c = correios.Entregador()
                            c.KM()
                            MonitorFolder.last_event = int(dt.datetime.fromtimestamp(i.stat().st_mtime).hour)
                            MonitorFolder.rel = i.name

                            break

            if event.src_path == '//192.163.1.179/HP_Transportes/Extrator/Dados/Distribuicao/PassageirosTranspArcoSul.csv':
                for i in path.iterdir():
                    if (dt.datetime.fromtimestamp(i.stat().st_mtime).hour > MonitorFolder.last_event) or ((
                          dt.datetime.fromtimestamp(i.stat().st_mtime).hour + 12) > MonitorFolder.last_event) and \
                            MonitorFolder.rel != i.name:
                        if i.name == 'PassageirosTranspArcoSul.csv':
                            c = correios.Entregador()
                            c.Demanda()
                            MonitorFolder.last_event = int(dt.datetime.fromtimestamp(i.stat().st_mtime).hour)
                            MonitorFolder.rel = i.name
                            break



if __name__ == "__main__":
    src_path = '//192.163.1.179/HP_Transportes/Extrator/Dados/Distribuicao/'

    event_handler = MonitorFolder()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    print("Monitoramento iniciado")
    observer.start()
    try:
        while (True):
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        observer.join()

    except FileNotFoundError:
        observer.stop()
        observer.join()
