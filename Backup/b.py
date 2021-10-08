import sqlite3

from connect import bdados


class b:

    def km ():
        banco = bdados()
        cur = banco.con.cursor()
        cur.execute(
            "SELECT DATA_RECEITA, SUM(KM_LINHA) AS KM_OP, SUM(KM_OCIOSA) AS KM_OC,SUM(LITRO_LINHA) AS LITROS FROM KM GROUP BY DATA_RECEITA")
        dadosKM = []
        i = 0
        for l in cur:

            var = var + f'{l[0]}, {l[1]}, {l[2]}, {l[3]}\n'
        cur.close()
        return print(dadosKM)

    def demanda ():
        banco = bdados()
        cur = banco.con.cursor()
        cur.execute(
            "select a.DATA_RECEITA, round(a.META) as META, ROUND(b.DEMANDA) ,  round(cast((b.DEMANDA/a.META-1)*100 as FLOAT),2) as 'DESV(%)' from (SELECT DATA_RECEITA, META FROM DEMANDA_PREV WHERE SIGLA_EMPRESA = 'HP') a left JOIN (select DATA_RECEITA, SUM(PASSAGEIROS_TOTAL) AS DEMANDA From demanda where SIGLA_EMPRESA = 'HP' GROUP BY DATA_RECEITA) b on a.DATA_RECEITA = b.DATA_RECEITA WHERE b.DEMANDA > 0")
        dadosDemanda = {}
        i = 0
        for l in cur:
            var = var + f'{l[0]}, {l[1]}, {l[2]}, {l[3]}\n'
        cur.close()
        return print(dadosKM)

    def receita ():
        banco = bdados()
        cur = banco.con.cursor()
        cur.execute(
            "SELECT A.DATA_RECEITA, ROUND(A.META,2), ROUND(B.RECEITA,2), ROUND((B.RECEITA/A.META-1)*100,2) AS DESV FROM (SELECT DATA_RECEITA, SIGLA_EMPRESA, SUM(META_RECEITA) AS META FROM RECEITA_PREV WHERE SIGLA_EMPRESA = 'HP' GROUP BY DATA_RECEITA) A LEFT JOIN (SELECT DATA_RECEITA, SUM(RECEITA) AS RECEITA  FROM DEMANDA WHERE SIGLA_EMPRESA='HP' GROUP BY DATA_RECEITA) B ON A.DATA_RECEITA = B.DATA_RECEITA")
        dadosReceita = {}
        i = 0
        for l in cur:
            var = var + f'{l[0]}, {l[1]}, {l[2]}, {l[3]}\n'
        cur.close()
        return print(dadosKM)

    def ipk ():
        banco = bdados()
        cur = banco.con.cursor()
        cur.execute(
            "SELECT j.DATA_RECEITA, ROUND((j.META/k.META),3) AS META, ROUND((j.DEMANDA/k.KM_OP),3) AS IPK, ROUND(((ROUND((j.DEMANDA/k.KM_OP),3)/ROUND((j.META/k.META),3))-1)*100,2) as 'DESV(%)'  FROM (select a.DATA_RECEITA, round(a.META,0) as META, b.DEMANDA ,  round(cast((b.DEMANDA/a.META-1)*100 as FLOAT),2) as 'DESV(%)' from (SELECT DATA_RECEITA, META FROM DEMANDA_PREV WHERE SIGLA_EMPRESA = 'HP') a left JOIN (select DATA_RECEITA, SUM(PASSAGEIROS_TOTAL) AS DEMANDA From demanda where SIGLA_EMPRESA = 'HP' GROUP BY DATA_RECEITA) b on a.DATA_RECEITA = b.DATA_RECEITA WHERE b.DEMANDA > 0) j left join  (SELECT A.DATA_RECEITA, b.MetaKM as  META, a.KM_OP, round(cast((a.KM_OP/b.MetaKM-1)*100 as FLOAT),2) as 'DESV(%)' FROM ((SELECT DATA_RECEITA, SUM(KM_LINHA) AS KM_OP, SUM(KM_OCIOSA) AS KM_OC,SUM(LITRO_LINHA) AS LITROS FROM KM GROUP BY DATA_RECEITA) a left join (select DATA_RECEITA, MetaKM FROM KM_PREV) b on a.DATA_RECEITA = b.DATA_RECEITA)) k on j.DATA_RECEITA = k.DATA_RECEITA")
        dadosIPK = {}
        i = 0
        for l in cur:
            var = var + f'{l[0]}, {l[1]}, {l[2]}, {l[3]}\n'
        cur.close()
        return print(dadosKM)

    def eqvl ():
        banco = bdados()
        cur = banco.con.cursor()
        cur.execute("SELECT DATA_RECEITA, SUM(KM_LINHA) AS KM_OP, SUM(KM_OCIOSA) AS KM_OC,SUM(LITRO_LINHA) AS LITROS FROM KM GROUP BY DATA_RECEITA")
        dadosEQVL = {}
        i = 0
        for l in cur:
            var = var + f'{l[0]}, {l[1]}, {l[2]}, {l[3]}\n'
        cur.close()
        return print(dadosKM)