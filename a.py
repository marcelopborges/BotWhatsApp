import pandas as pd
import sqlite3


class IMPORTADOR:


    ###DADOS DE CONEXÃO###
    path = '//192.163.1.179/HP_Transportes/Extrator/Dados/Distribuicao/'
    conn = sqlite3.connect('bdados.db', check_same_thread=False)
    c = conn.cursor()

    def import_km():

        ####DADOS KM####
        dataKm = pd.read_csv(f'{IMPORTADOR.path}KM.csv', sep=';')
        baseKm = pd.DataFrame(dataKm)
        baseKm.to_sql('KM', IMPORTADOR.conn, if_exists='replace', index=False)

    def import_demanda():

        ####DADOS DEMANDA####
        dataDemanda = pd.read_csv(f'{IMPORTADOR.path}PassageirosTranspArcoSul.csv', sep=';')
        baseDemanda = pd.DataFrame(dataDemanda)
        baseDemanda.to_sql('DEMANDA', IMPORTADOR.conn, if_exists='replace', index=False)

    def import_tarifa():

        ####DADOS TARIFA####
        data_tarifa = pd.read_csv(f'{IMPORTADOR.path}Tarifa.csv', sep=';')
        base_tarifa = pd.DataFrame(data_tarifa)
        base_tarifa.to_sql('TARIFA', IMPORTADOR.conn, if_exists='replace', index=False)

    def import_demanda_prev():

        ####DADOS DEMANDA_PREV####
        data_demanda_prev = pd.read_csv(f'{IMPORTADOR.path}PrevPasTranspArcoSul.csv', sep=';')
        base_demanda_prev = pd.DataFrame(data_demanda_prev)
        base_demanda_prev.to_sql('DEMANDA_PREV',IMPORTADOR.conn, if_exists='replace', index=False)

    def import_km_prev():

        ####DADOS KM_PREV####
        data_km_prev = pd.read_csv(f'{IMPORTADOR.path}PrevKm.csv', sep=';')
        base_km_prev = pd.DataFrame(data_km_prev)
        base_km_prev.to_sql('KM_PREV',IMPORTADOR.conn, if_exists='replace', index=False)