import collections
import locale
import pandas as pd
import pywhatkit

locale.setlocale(locale.LC_ALL, '')
'pt_BR.UTF-8'


class Relatorio:
    """Criação de todos os DataFrames a serem utilizados. Foram feitos dentro de Relatório, para não ficar gastando
    memória desnecessariamente"""

    path = '//192.163.1.179/HP_Transportes/Extrator/Dados/Distribuicao/'  # Definição o caminho onde está o arquivo

    '''
    1 - Leitura do CSV
    2 - intanciamento dos dados do CSV
    3 - Importando DataFrame Pandas
    
    '''
    # Dados de Quilometragem
    kmCsv = pd.read_csv(f'{path}KM.csv', sep=";")  # 1
    dataKm = kmCsv  # 2
    baseKm = pd.DataFrame(dataKm)  # 3

    # Dados de Demanda
    demandaCsv = pd.read_csv(f'{path}PassageirosTranspArcoSul.csv', sep=";")  # 1
    dataDemanda = demandaCsv  # 2
    baseDemanda = pd.DataFrame(dataDemanda)  # 3

    # Dados de Tarifa
    tarifaCsv = pd.read_csv(f'{path}Tarifa.csv', sep=";")  # 1
    dataTarifa = tarifaCsv  # 2
    baseTarifa = pd.DataFrame(dataTarifa)  # 3

    # Dados de Km Previsto
    kmPrevCsv = pd.read_csv(f'{path}PrevKm.csv', sep=";")  # 1
    dataKmPrev = kmPrevCsv  # 2
    baseKmPrev = pd.DataFrame(dataKmPrev)  # 3

    # Dados de Demanda Prevista
    demandaPrevCsv = pd.read_csv(f'{path}PrevPasTranspArcoSul.csv', sep=";")  # 1
    dataDemandaPrev = demandaPrevCsv  # 2
    baseDemandaPrev = pd.DataFrame(dataDemandaPrev)  # 3

    # Dados de Receita prevista
    receitaPrevCsv = pd.read_csv(f'{path}PrevReceita.csv', sep=";")  # 1
    dataReceitaPrev = receitaPrevCsv  # 2
    baseReceitaPrev = pd.DataFrame(dataReceitaPrev)  # 3

    def quilometragem(tel='', nome=''):

        dfKm = Relatorio.baseKm[['DATA_RECEITA', 'KM_LINHA', 'KM_OCIOSA', 'LITRO_LINHA']]
        dfKm = dfKm.fillna(0)
        dfKm['KM_LINHA'] = dfKm['KM_LINHA'].str.replace(',', '.')
        dfKm['KM_OCIOSA'] = dfKm['KM_OCIOSA'].str.replace(',', '.')
        dfKm['KM_LINHA'] = pd.to_numeric(dfKm['KM_LINHA'])
        dfKm['KM_OCIOSA'] = pd.to_numeric(dfKm['KM_OCIOSA'])
        dfKm = (dfKm.groupby(by=['DATA_RECEITA']).sum())

        saudacao = f'Olá, *{nome}*! segue abaixo as informações de quilometragem:\n'
        title = saudacao + "Data / KM Total / KM OP  /  %KM Ocioso"

        msg = title + '\n'
        i = 0
        varData = []
        varKmTotal = []
        varOcioso = []

        for index, row in dfKm.iterrows():
            if row["KM_LINHA"] != 0:
                varData.append(f'{index[0:10]}')
                varKmTotal.append(row["KM_LINHA"])
                varOcioso.append(row["KM_OCIOSA"])
            else:
                varKmTotal.append(1)

        n = 0
        j = len(varData)

        while n < j:
            msg = msg + f'{varData[n]}  /  {round(varKmTotal[n], 1)}  /  {round(varKmTotal[n] - varOcioso[n], 1)}  /  {"{0:.2%}".format(varOcioso[n] / varKmTotal[n])}\n'
            n += 1
        msg = msg + '\n *O KM Operacional pode aparecer zerado e o ocioso com valor elevado e isto é devido ao não fechamento do BDO* '
        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)
        dfKm = ""
        varData = []
        varKmTotal = []
        varOcioso = []

    def demanda(tel='', nome=''):

        dfArcoSulPrev = Relatorio.baseDemandaPrev[['DATA_RECEITA', 'NOME_TN', 'SIGLA_EMPRESA', 'META']]
        dfArcoSulPrev = dfArcoSulPrev.fillna(0)
        dfArcoSulPrev = (dfArcoSulPrev.query('SIGLA_EMPRESA=="HP"'))
        dfArcoSulPrev = (dfArcoSulPrev.query('NOME_TN=="SERVIÇO CONVENCIONAL ( ESSENCIAL )"'))
        dfArcoSulPrev["META"] = dfArcoSulPrev["META"].str.replace(',', '.')
        dfArcoSulPrev["META"] = pd.to_numeric(dfArcoSulPrev["META"])
        dfArcoSulPrev = (dfArcoSulPrev.groupby(by=['DATA_RECEITA']).sum())

        dfArcoSul = Relatorio.baseDemanda[['DATA_RECEITA', 'SIGLA_EMPRESA', 'PASSAGEIROS_TOTAL', 'RECEITA']]
        dfArcoSul = dfArcoSul.fillna(0)
        #dfArcoSul = (dfArcoSul.query('SIGLA_EMPRESA=="HP"'))
        dfArcoSul["PASSAGEIROS_TOTAL"] = dfArcoSul["PASSAGEIROS_TOTAL"].str.replace(',', '.')
        dfArcoSul["RECEITA"] = dfArcoSul["RECEITA"].str.replace(',', '.')
        dfArcoSul["PASSAGEIROS_TOTAL"] = pd.to_numeric(dfArcoSul["PASSAGEIROS_TOTAL"])
        dfArcoSul["RECEITA"] = pd.to_numeric(dfArcoSul["RECEITA"])
        dfArcoSul = (dfArcoSul.groupby(by=['DATA_RECEITA']).sum())

        saudacao = f'Olá, *{nome}*! segue abaixo as informações de demanda :\n'
        title = saudacao + "Data / Demanda Prev. / Demanda Real  /  % Desv."

        msg = title + '\n'
        i = 0
        varData1 = []
        varData2 = []
        varDataX = []
        varDemanda = []
        varDemandaPrev = []

        for index, row in dfArcoSul.iterrows():
            if row["PASSAGEIROS_TOTAL"] != 0:
                varData1.append(f'{index[0:10]}')
                varDemanda.append(row["PASSAGEIROS_TOTAL"])

            else:
                varDemanda.append(1)

        for index, row in dfArcoSulPrev.iterrows():
            if row["META"] != 0:
                varData2.append(f'{index[0:10]}')
                varDemandaPrev.append(row["META"])

            else:
                varDemandaPrev.append(1)

        if collections.Counter(varData1) == collections.Counter(varData2):
            varDataX = varData1
        else:
            for i in list(set(varData1) & set(varData2)):
                varDataX.append(i)

        j = len(varDataX)
        n = 0

        # "Data / Demanda Total / KM OP  /  %KM Ocioso"
        while n < j:
            msg = msg + f'{varDataX[n]}  /  {round((varDemandaPrev[n] ), 1)}  /  {round(varDemanda[n]/2, 1)}  /  {"{0:.2%}".format((varDemanda[n]/2) / varDemandaPrev[n] - 1)}\n'
            n += 1
        msg = msg + '\n\n *Os dados são de demanda faturada do Arco Sul correspondente à HP (50%)*'
        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)
        dfArcoSul=''
        dfArcoSulPrev=''
        varData1 = []
        varData2 = []
        varDataX = []
        varDemanda = []
        varDemandaPrev = []

    def receita(tel = '', nome = '' ):

        dfReceitaPrev = Relatorio.baseReceitaPrev[['DATA_RECEITA', 'NOME_TN', 'SIGLA_EMPRESA', 'META_RECEITA']]
        dfReceitaPrev = dfReceitaPrev.fillna(0)
        dfReceitaPrev = (dfReceitaPrev.query('SIGLA_EMPRESA=="HP"'))
        dfReceitaPrev = (dfReceitaPrev.query('NOME_TN=="SERVIÇO CONVENCIONAL ( ESSENCIAL )"'))
        dfReceitaPrev["META_RECEITA"] = dfReceitaPrev["META_RECEITA"].str.replace(',', '.')
        dfReceitaPrev["META_RECEITA"] = pd.to_numeric(dfReceitaPrev["META_RECEITA"])
        dfReceitaPrev = (dfReceitaPrev.groupby(by=['DATA_RECEITA']).sum())

        dfReceita = Relatorio.baseDemanda[['DATA_RECEITA', 'SIGLA_EMPRESA', 'RECEITA']]
        dfReceita = dfReceita.fillna(0)
        dfReceita["RECEITA"] = dfReceita["RECEITA"].str.replace(',', '.')
        dfReceita["RECEITA"] = pd.to_numeric(dfReceita["RECEITA"])
        dfReceita = (dfReceita.groupby(by=['DATA_RECEITA']).sum())

        saudacao = f'Olá, *{nome}*! segue abaixo as informações de Receita :\n'
        title = saudacao + "Data / Receita Prev. / Receita Real  /  % Desv."

        msg = title + '\n'
        i = 0
        varData1 = []
        varData2 = []
        varDataX = []
        varReceita = []
        varReceitaPrev = []

        for index, row in dfReceita.iterrows():
            if row["RECEITA"] != 0:
                varData1.append(f'{index[0:10]}')
                varReceita.append(row["RECEITA"])

            else:
                varReceita.append(1)

        for index, row in dfReceitaPrev.iterrows():
            if row["META_RECEITA"] != 0:
                varData2.append(f'{index[0:10]}')
                varReceitaPrev.append(row["META_RECEITA"])

            else:
                varReceitaPrev.append(1)

        if collections.Counter(varData1) == collections.Counter(varData2) :
            varDataX = varData1
        else:
            for i in list(set(varData1) & set(varData2)):
                varDataX.append(i)
        j = len(varDataX)
        n = 0

        # "Data / Demanda Total / KM OP  /  %KM Ocioso"

        while n < j:
            msg = msg + f'{varDataX[n]}  /  {round(varReceitaPrev[n], 1)}  /  {round(varReceita[n]/2, 1)}  /  {"{0:.2%}".format((varReceita[n]/2) / varReceitaPrev[n] - 1)}\n'
            n += 1
        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)
        dfReceita=''
        dfReceitaPrev=''
        varData1 = []
        varData2 = []
        varDataX = []
        varReceita = []
        varReceitaPrev = []

    def ipk(tel='', nome=''):

        #Demanda Prevista
        dfArcoSulPrev = Relatorio.baseDemandaPrev[['DATA_RECEITA', 'NOME_TN', 'SIGLA_EMPRESA', 'META']]
        dfArcoSulPrev = dfArcoSulPrev.fillna(0)
        dfArcoSulPrev = (dfArcoSulPrev.query('SIGLA_EMPRESA=="HP"'))
        dfArcoSulPrev = (dfArcoSulPrev.query('NOME_TN=="SERVIÇO CONVENCIONAL ( ESSENCIAL )"'))
        dfArcoSulPrev["META"] = dfArcoSulPrev["META"].str.replace(',', '.')
        dfArcoSulPrev["META"] = pd.to_numeric(dfArcoSulPrev["META"])
        dfArcoSulPrev = (dfArcoSulPrev.groupby(by=['DATA_RECEITA']).sum())
        dfArcoSulPrev.sort_index()

        #Demanda Realizada
        dfArcoSul = Relatorio.baseDemanda[['DATA_RECEITA', 'SIGLA_EMPRESA', 'PASSAGEIROS_TOTAL']]
        dfArcoSul = dfArcoSul.fillna(0)
        #dfArcoSul = (dfArcoSul.query('SIGLA_EMPRESA=="HP"'))
        dfArcoSul["PASSAGEIROS_TOTAL"] = dfArcoSul["PASSAGEIROS_TOTAL"].str.replace(',', '.')
        dfArcoSul["PASSAGEIROS_TOTAL"] = pd.to_numeric(dfArcoSul["PASSAGEIROS_TOTAL"])
        dfArcoSul = (dfArcoSul.groupby(by=['DATA_RECEITA']).sum())
        dfArcoSul.sort_index()

        #KM Previsto
        dfKmPrev = Relatorio.baseKmPrev[['DATA_RECEITA', 'NOME_TN', 'MetaKM']]
        dfKmPrev = dfKmPrev.fillna(0)
        dfKmPrev = (dfKmPrev.query('NOME_TN=="SERVIÇO CONVENCIONAL ( ESSENCIAL )"'))
        #dfKmPrev["MetaKM"] = dfKmPrev["MetaKM"].str.replace(',', '.')
        dfKmPrev["MetaKM"] = pd.to_numeric(dfKmPrev["MetaKM"])
        dfKmPrev = (dfKmPrev.groupby(by=['DATA_RECEITA']).sum())
        dfKmPrev.sort_index()

        #Km Realizado
        dfKm = Relatorio.baseKm[['DATA_RECEITA', 'KM_LINHA', 'KM_OCIOSA', 'LITRO_LINHA']]
        dfKm = dfKm.fillna(0)
        dfKm['KM_LINHA'] = dfKm['KM_LINHA'].str.replace(',', '.')
        dfKm['KM_OCIOSA'] = dfKm['KM_OCIOSA'].str.replace(',', '.')
        dfKm['KM_LINHA'] = pd.to_numeric(dfKm['KM_LINHA'])
        dfKm['KM_OCIOSA'] = pd.to_numeric(dfKm['KM_OCIOSA'])
        dfKm = (dfKm.groupby(by=['DATA_RECEITA']).sum())
        dfKm.sort_index()

        #Cabeçalho
        saudacao = f'Olá, *{nome}*! segue abaixo as informações de IPK :\n'
        title = saudacao + "Data / IPK Prev. / IPK Real  /  % Desv."
        msg = title + '\n'

        #Variáveis
        i = 0
        varData1 = []
        varData2 = []
        varData3 = []
        varData4 = []
        varDataX = []

        varDemanda = []
        varDemandaPrev = []
        varKm = []
        varKmPrev = []

        for index, row in dfKmPrev.iterrows():
            if row["MetaKM"] != 0:
                varData1.append(f'{index[0:10]}')
                varKmPrev.append(row["MetaKM"])

            else:
                varKmPrev.append(1)

        for index, row in dfKm.iterrows():
            if row["KM_LINHA"] != 0:
                varData2.append(f'{index[0:10]}')
                varKm.append(row["KM_LINHA"])

            else:
                varKm.append(1)

        for index, row in dfArcoSul.iterrows():
            if row["PASSAGEIROS_TOTAL"] != 0:
                varData3.append(f'{index[0:10]}')
                varDemanda.append(row["PASSAGEIROS_TOTAL"])

            else:
                varDemanda.append(1)

        for index, row in dfArcoSulPrev.iterrows():
            if row["META"] != 0:
                varData4.append(f'{index[0:10]}')
                varDemandaPrev.append(row["META"])

            else:
                varDemandaPrev.append(1)

        if collections.Counter(varData1) == collections.Counter(varData2) and collections.Counter(varData1) == collections.Counter(varData3) and collections.Counter(varData1) == collections.Counter(varData4):
            varDataX = varData1
        else:
            for i in list(set(varData1) & set(varData2) & set(varData3) & set(varData4)):
                varDataX.append(i)
        j = len(varDataX)
        n = 0

        # "Data / IPK Prev. / IPK Real  /  % Desv."
        while n < j:
            msg = msg + f'{varDataX[n]}  /  {round(varDemandaPrev[n]/varKmPrev[n], 3)}  /  {round((varDemanda[n]/2)/varKm[n], 3)}  /  {"{0:.2%}".format(((varDemanda[n]/2)/varKm[n])/(varDemandaPrev[n]/varKmPrev[n]) - 1)}\n'
            n += 1
        msg = msg +'\n\n *Demanda transportada*'
        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)
        dfKm=''
        dfArcoSulPrev=''
        dfArcoSul=''
        dfArcoSul=''
        varData1 = []
        varData2 = []
        varData3 = []
        varData4 = []
        varDataX = []

        varDemanda = []
        varDemandaPrev = []
        varKm = []
        varKmPrev = []

    def eqvl(tel='', nome=''):

        dfEqvlPrev = Relatorio.baseReceitaPrev[['DATA_RECEITA', 'NOME_TN', 'SIGLA_EMPRESA', 'Meta_Tarifa_Equivalente']]
        dfEqvlPrev = dfEqvlPrev.fillna(0)
        dfEqvlPrev = (dfEqvlPrev.query('SIGLA_EMPRESA=="HP"'))
        dfEqvlPrev = (dfEqvlPrev.query('NOME_TN=="SERVIÇO CONVENCIONAL ( ESSENCIAL )"'))
        dfEqvlPrev["Meta_Tarifa_Equivalente"] = dfEqvlPrev["Meta_Tarifa_Equivalente"].str.replace(',', '.')
        dfEqvlPrev["Meta_Tarifa_Equivalente"] = pd.to_numeric(dfEqvlPrev["Meta_Tarifa_Equivalente"])
        dfEqvlPrev = (dfEqvlPrev.groupby(by=['DATA_RECEITA']).sum())

        dfArcoSul = Relatorio.baseDemanda[['DATA_RECEITA', 'SIGLA_EMPRESA', 'PASSAGEIROS_TOTAL']]
        dfArcoSul = dfArcoSul.fillna(0)
        dfArcoSul = (dfArcoSul.query('SIGLA_EMPRESA=="HP"'))
        dfArcoSul["PASSAGEIROS_TOTAL"] = dfArcoSul["PASSAGEIROS_TOTAL"].str.replace(',', '.')
        dfArcoSul["PASSAGEIROS_TOTAL"] = pd.to_numeric(dfArcoSul["PASSAGEIROS_TOTAL"])
        dfArcoSul = (dfArcoSul.groupby(by=['DATA_RECEITA']).sum())

        dfReceita = Relatorio.baseDemanda[['DATA_RECEITA', 'SIGLA_EMPRESA', 'RECEITA']]
        dfReceita = dfReceita.fillna(0)
        dfReceita = (dfReceita.query('SIGLA_EMPRESA=="HP"'))
        dfReceita["RECEITA"] = dfReceita["RECEITA"].str.replace(',', '.')
        dfReceita["RECEITA"] = pd.to_numeric(dfReceita["RECEITA"])
        dfReceita = (dfReceita.groupby(by=['DATA_RECEITA']).sum())

        dfTarifa = Relatorio.baseTarifa[['DATA_RECEITA', 'TARIFA_CONVENCIONAL']]
        dfTarifa = dfTarifa.fillna(0)
        dfTarifa["TARIFA_CONVENCIONAL"] = dfTarifa["TARIFA_CONVENCIONAL"].str.replace(',', '.')
        dfTarifa["TARIFA_CONVENCIONAL"] = pd.to_numeric(dfTarifa["TARIFA_CONVENCIONAL"])
        dfTarifa = (dfTarifa.groupby(by=['DATA_RECEITA']).sum().groupby(level=[0]).cumsum())

        # Cabeçalho
        saudacao = f'Olá, *{nome}*! segue abaixo as informações de Equivalência Tarifária :\n'
        title = saudacao + "Data / Eqvl. Prev. / Eqvl. Real  /  % Desv."
        msg = title + '\n'

        #Variáveis
        i = 0
        varData1 = []
        varData2 = []
        varData3 = []
        varData4 = []
        varDataX = []
        varEqvlPrev = []
        varReceita = []
        varDemanda = []
        varTarifa = []

        for index, row in dfEqvlPrev.iterrows():
            if row["Meta_Tarifa_Equivalente"] != 0:
                varData1.append(f'{index[0:10]}')
                varEqvlPrev.append(row["Meta_Tarifa_Equivalente"])

            else:
                varEqvlPrev.append(1)

        for index, row in dfArcoSul.iterrows():
            if row["PASSAGEIROS_TOTAL"] != 0:
                varData2.append(f'{index[0:10]}')
                varDemanda.append(row["PASSAGEIROS_TOTAL"])

            else:
                varDemanda.append(1)

        for index, row in dfReceita.iterrows():
            if row["RECEITA"] != 0:
                varData3.append(f'{index[0:10]}')
                varReceita.append(row["RECEITA"])

            else:
                varReceita.append(1)

        for index, row in dfTarifa.iterrows():
            if row["TARIFA_CONVENCIONAL"] != 0:
                varData4.append(f'{index[0:10]}')
                varTarifa.append(row["TARIFA_CONVENCIONAL"])

            else:
                varTarifa.append(1)

        if collections.Counter(varData1) == collections.Counter(varData2) and collections.Counter(
                varData1) == collections.Counter(varData3) and collections.Counter(varData1) == collections.Counter(
                varData4):
            varDataX = varData1
        else:
            for i in list(set(varData1) & set(varData2) & set(varData3) & set(varData4)):
                varDataX.append(i)
        j = len(varDataX)
        n = 0

            # "Data / Eqvl. Prev. / Eqvl. Real  /  % Desv."
        while n < j:
            msg = msg + f'{varDataX[n]}  /  {"{0:.2%}".format(varEqvlPrev[n])}  /  {"{0:.2%}".format(varReceita[n] / varDemanda[n] / varTarifa[n])}  /  {"{0:.2%}".format((varReceita[n] / varDemanda[n] / varTarifa[n]) / varEqvlPrev[n] -1)}\n'
            n += 1
        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)
        dfArcoSul=''
        dfReceita=''
        dfTarifa=''
        dfEqvlPrev=''
        varData1 = []
        varData2 = []
        varData3 = []
        varData4 = []
        varDataX = []
        varEqvlPrev = []
        varReceita = []
        varDemanda = []
        varTarifa = []
