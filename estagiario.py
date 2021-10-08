import collections
import locale
import pywhatkit

from connect import bdados

locale.setlocale(locale.LC_ALL, '')
'pt_BR.UTF-8'


class Relatorio:


    def quilometragem(tel='', nome=''):

        saudacao = f'Olá, *{nome}*! segue abaixo as informações de quilometragem:\n'
        title = saudacao + "DATA  / META  /  KM_OP /  DESV.(%) \n"
        msg = title
        banco = bdados()
        cur = banco.con.cursor()
        cur.execute(
            "SELECT A.DATA_RECEITA, b.MetaKM as META, round(a.KM_OP,1) as KM_OP, round(cast((a.KM_OP/b.MetaKM-1)*100 as FLOAT),2) as 'DESV(%)' FROM ((SELECT DATA_RECEITA, SUM(KM_LINHA) AS KM_OP, SUM(KM_OCIOSA) AS KM_OC,SUM(LITRO_LINHA) AS LITROS FROM KM GROUP BY DATA_RECEITA) a left join (select DATA_RECEITA, MetaKM FROM KM_PREV) b on a.DATA_RECEITA = b.DATA_RECEITA)")

        for l in cur:
            msg = msg + f'{l[0]} / {l[1]} / {l[2]} / {l[3]}\n'
        msg = msg + '\n *O KM Operacional pode aparecer zerado e o ocioso com valor elevado e isto é devido ao não fechamento do BDO* '
        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)

    def demanda(tel='', nome=''):

        saudacao = f'Olá, *{nome}*! segue abaixo as informações de demanda :\n'
        title = saudacao + "DATA  / META  /  DEMANDA /  DESV.(%) \n"
        msg = title
        banco = bdados()
        cur = banco.con.cursor()
        cur.execute(
            "select a.DATA_RECEITA, round(a.META) as META, ROUND(b.DEMANDA) AS DEMANDA,  round(cast((b.DEMANDA/a.META-1)*100 as FLOAT),2) as 'DESV(%)' from (SELECT DATA_RECEITA, META FROM DEMANDA_PREV WHERE SIGLA_EMPRESA = 'HP') a left JOIN  (select DATA_RECEITA, SUM(PASSAGEIROS_TOTAL) AS DEMANDA From demanda  where SIGLA_EMPRESA = 'HP' GROUP BY DATA_RECEITA) b   on a.DATA_RECEITA = b.DATA_RECEITA  GROUP BY a.DATA_RECEITA ORDER BY strftime('%s', a.DATA_RECEITA) DESC ")

        for l in cur:
            msg = msg + f'{l[0]} / {l[1]} / {l[2]} / {l[3]}\n'

        msg = msg + '\n\n *Os dados são de demanda faturada do Arco Sul correspondente à HP (50%)*'
        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)

    def receita(tel = '', nome = '' ):

        saudacao = f'Olá, *{nome}*! segue abaixo as informações de Receita :\n'
        title = saudacao + "DATA  / META  /  RECEITA /  DESV.(%) \n"

        msg = title + '\n'
        banco = bdados()
        cur = banco.con.cursor()
        cur.execute(
            "SELECT A.DATA_RECEITA, ROUND(A.META,2), ROUND(B.RECEITA,2), ROUND((B.RECEITA/A.META-1)*100,2) AS DESV FROM (SELECT DATA_RECEITA, SIGLA_EMPRESA, SUM(META_RECEITA) AS META FROM RECEITA_PREV WHERE SIGLA_EMPRESA = 'HP' GROUP BY DATA_RECEITA) A LEFT JOIN (SELECT DATA_RECEITA, SUM(RECEITA) AS RECEITA  FROM DEMANDA WHERE SIGLA_EMPRESA='HP' GROUP BY DATA_RECEITA) B ON A.DATA_RECEITA = B.DATA_RECEITA")

        for l in cur:
            msg = msg + f'{l[0]} / {l[1]} / {l[2]} / {l[3]}\n'
        msg = msg + '\n\n *Os dados são de receita faturada do Arco Sul correspondente à HP (50%)*'
        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)

    def ipk(tel='', nome=''):

        #Cabeçalho
        saudacao = f'Olá, *{nome}*! segue abaixo as informações de IPK :\n'
        title = saudacao + "DATA  / META  /  IPK /  DESV.(%) \n"
        msg = title + '\n'
        banco = bdados()
        cur = banco.con.cursor()
        cur.execute(
            "SELECT E.DATA_RECEITA,E.META_IPK,F.IPK, ROUND((F.IPK/E.META_IPK-1)*100,1) AS DESV FROM (SELECT A.DATA_RECEITA, ROUND(B.META_DEMANDA / A.MetaKM,3) AS META_IPK from (SELECT DATA_RECEITA, MetaKM FROM KM_PREV) A left join (SELECT DATA_RECEITA, META AS META_DEMANDA FROM DEMANDA_PREV WHERE SIGLA_EMPRESA = 'HP'  and PREV_KM_ID_SERVICO ='1') B on  A.DATA_RECEITA = B.DATA_RECEITA GROUP BY A.DATA_RECEITA) E LEFT JOIN (SELECT C.DATA_RECEITA, ROUND(D.DEMANDA/C.KM_T,3) AS IPK FROM (SELECT DATA_RECEITA, ROUND((SUM(KM_LINHA) ),1) AS KM_T FROM KM GROUP BY DATA_RECEITA) C LEFT JOIN (select DATA_RECEITA, ROUND(SUM(PASSAGEIROS_TOTAL)/2,1) AS DEMANDA  From demanda  GROUP BY DATA_RECEITA) D ON C.DATA_RECEITA = D.DATA_RECEITA GROUP BY C.DATA_RECEITA) F ON E.DATA_RECEITA = F.DATA_RECEITA ")

        for l in cur:
            msg = msg + f'{l[0]} / {l[1]} / {l[2]} / {l[3]}\n'


        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)


    def eqvl(tel='', nome=''):

        saudacao = f'Olá, *{nome}*! segue abaixo as informações de Equivalência Tarifária :\n'
        title = saudacao + "DATA  / META  /  EQVL /  DESV.(%) \n"
        msg = title + '\n'

        banco = bdados()
        cur = banco.con.cursor()
        cur.execute(
            "SELECT m.DATA_RECEITA,n.META,m.EQVL, ROUND((m.EQVL/n.META-1)*100,2) AS DESV FROM (SELECT a.DATA_RECEITA, round(a.RECEITA / (a.DEMANDA * b.TARIFA_CONVENCIONAL)*100,2) as EQVL FROM (select DATA_RECEITA, SUM(RECEITA) AS RECEITA,  SUM(PASSAGEIROS_TOTAL) AS DEMANDA from demanda GROUP BY DATA_RECEITA) a LEFT JOIN (SELECT DATA_RECEITA, TARIFA_CONVENCIONAL FROM TARIFA) b ON  a.DATA_RECEITA = b.DATA_RECEITA)m left join (select DATA_RECEITA, ROUND(Meta_Tarifa_Equivalente*100,2) as META from RECEITA_PREV WHERE SIGLA_EMPRESA='HP') n where m.DATA_RECEITA=n.DATA_RECEITA")

        for l in cur:
            msg = msg + f'{l[0]} / {l[1]} / {l[2]} / {l[3]}\n'

        msg = msg + '\n\n *Os dados são da equivalência tarifária do Arco Sul correspondente à HP (50%)*'
        pywhatkit.sendwhatmsg_instantly(tel, msg, 15, True)